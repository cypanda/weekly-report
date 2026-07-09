from utils.text_utils import align_text, display_width
from utils.config_loader import config

# 主要作用：按照周报模版组装markdown的数据

def build_markdown(report):

    week = report.week

    lines = []

    # =========================
    # 标题
    # =========================
    lines.append(
        f"# 时间周报（{week.start_date} ~ {week.end_date}）"
    )
    lines.append("")

    # =========================
    # 一、本周时间分布
    # =========================
    lines.append("## 一、本周时间分布")
    lines.append("")

    lines.append(f"- 📝 已记录：{week.record_hours:.1f}h")
    lines.append(f"- 🛏️ 睡觉：{week.sleep_hours:.1f}h")
    lines.append(f"- ⏳ 未记录：{week.missing_hours:.1f}h")
    lines.append("")

    for calendar in report.category_order:

        if calendar not in week.calendars:
            continue

        stat = week.calendars[calendar]

        lines.append(
            f"- {calendar}：{stat.hours:.1f}h"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    # =========================
    # 二、核心投入拆解（AI优先）
    # =========================
    lines.append("## 二、核心投入拆解")
    lines.append("")

    use_ai = bool(report.ai_core_breakdown)

    if use_ai:

        breakdown = report.ai_core_breakdown

        # calendar = "投资(重要&不紧急)"
        for calendar in config.focus_categories:

            if calendar not in breakdown:
                continue

            lines.append(f"### {calendar}")
            lines.append("")

            for index, item in enumerate(breakdown[calendar], start=1):

                lines.append(
                   f"#### {index}、**{item['topic']}：{item['hours']:.2f}h**"
                )

                for event in item["items"]:
                    lines.append(f"  - {event}")

                lines.append("")

    else:

        # AI失败，退回原来的统计

        for calendar in config.focus_categories:

            if calendar not in report.same_events:
                continue

            lines.append(f"### {calendar}")

            items = sorted(
                report.same_events[calendar].items(),
                key=lambda x: x[1],
                reverse=True
            )

            for title, hours in items:

                lines.append(
                    f"- {title}：{hours:.2f}h"
                )

            lines.append("")

    lines.append("---")
    lines.append("")

    # =========================
    # 三、本周事件图谱
    # =========================
    lines.append("## 三、本周事件图谱")
    lines.append("")

    max_width = max(display_width(x) for x in report.category_order)

    for calendar in report.category_order:

        if calendar not in report.chart:
            continue

        hours = report.chart[calendar]

        bar = "█" * max(1, round(hours / 2))

        label = align_text(calendar, max_width)

        lines.append(
            f"{label} │ {bar} {hours:.1f}h"
        )

    lines.append("")
    lines.append("---")
    lines.append("")

    # =========================
    # 四、本周与上周数据对比
    # =========================
    lines.append("## 四、本周与上周数据对比")
    lines.append("")

    if report.compare:

        for calendar in report.category_order:

            if calendar not in report.compare:
                continue

            item = report.compare[calendar]

            diff = item["diff_hours"]

            if diff > 0:
                diff_text = f"↑ 增加 {diff:.1f}h"
            elif diff < 0:
                diff_text = f"↓ 减少 {abs(diff):.1f}h"
            else:
                diff_text = "无变化"

            lines.append(f"### {calendar}")
            lines.append("")

            lines.append("|     | 总小时（h） | 总分钟（min） | 平均每天（h） | 占记录时间 | 占清醒时间 | 环比 |")
            lines.append("| --- | ---------- | ------------ | ------------ | ---------- | ---------- | ---- |")

            lines.append(
                f"| 本周 | "
                f"{item['this_hours']:.1f}h | "
                f"{item['this_minutes']} | "
                f"{item['this_average']:.1f}h | "
                f"{item['this_record_ratio']:.1f}% | "
                f"{item['this_awake_ratio']:.1f}% | "
                f"{diff_text} |"
            )

            lines.append(
                f"| 上周 | "
                f"{item['last_hours']:.1f}h | "
                f"{item['last_minutes']} | "
                f"{item['last_average']:.1f}h | "
                f"{item['last_record_ratio']:.1f}% | "
                f"{item['last_awake_ratio']:.1f}% | "
                f" |"
            )

            lines.append("")

    else:

        lines.append("（暂无上周数据）")

    lines.append("")
    lines.append("---")
    lines.append("")

    # =========================
    # 五、本周总结（AI优先）
    # =========================
    lines.append("## 五、本周总结")
    lines.append("")

    if report.ai_summary:

        summary = report.ai_summary

        # 总体评价
        if summary.get("overall"):
            lines.append(summary["overall"])
            lines.append("")

        # 做得好的
        if summary.get("good"):

            lines.append("### 1、做得好的")

            for item in summary["good"]:
                lines.append(f"- {item}")

            lines.append("")

        # 存在的问题
        if summary.get("bad"):

            lines.append("### 2、存在的问题")

            for item in summary["bad"]:
                lines.append(f"- {item}")

            lines.append("")

        # 下周建议
        if summary.get("suggestions"):

            lines.append("### 3、下周建议")

            for index, item in enumerate(summary["suggestions"], start=1):
                lines.append(f"{index}. {item}")

            lines.append("")

    else:

        lines.append("（AI总结生成失败）")

    return "\n".join(lines)