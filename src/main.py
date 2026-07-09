import os
import json
import subprocess
from workflow.week_report_workflow import build_week_report_workflow
from datetime import timedelta
from utils.date_range import get_week_range

from utils.printer import (
    print_events,
    print_days,
    print_week,
    print_chart,
    print_ai,
    print_compare,
    print_report
)

from builders.markdown_builder import build_markdown
from writers.markdown_writer import save_markdown

from engines.ai_engine import (
    build_ai_report
)
from pathlib import Path
from utils.config_loader import config

DEBUG_USE_LAST_WEEK = False

def main():
    """
    生成周报的主函数，暴露给 CLI 调用
    """
    calendars = config.calendars

    # 时间范围
    if DEBUG_USE_LAST_WEEK:
        this_week_start, this_week_end = get_week_range(1)
    else:
        this_week_start, this_week_end = get_week_range(0)

    print("📊 正在锁定时间范围...")
    print(
        f"【统计区间】: "
        f"{this_week_start.strftime('%Y-%m-%d')} "
        f"至 "
        f"{this_week_end.strftime('%Y-%m-%d')}"
    )
    print("-" * 50)

    print("🚀 开始读取日历数据...\n")

    # =========================
    # 上周数据
    # =========================

    last_week_start = this_week_start - timedelta(days=7)
    last_week_end = this_week_end - timedelta(days=7)

    last_week_report = build_week_report_workflow(
        calendars,
        last_week_start,
        last_week_end
    )

    # =========================
    # 本周数据
    # =========================

    report = build_week_report_workflow(
        calendars,
        this_week_start,
        this_week_end,
        last_week_report
    )

    print_events(report.events)
    print_days(report.days)
    print_week(report.week)
    print_compare(report)
    print_report(report)
    print_chart(report)

    # =========================
    # AI
    # =========================

    report = build_ai_report(report)

    print_ai(report)

    # =========================
    # Markdown
    # =========================

    markdown = build_markdown(report)

    print(markdown)

    filename = (
        Path(config.output_path)
        / f"{report.week.start_date}_{report.week.end_date}.md"
    )

    os.makedirs(
        os.path.dirname(filename),
        exist_ok=True
    )

    save_markdown(
        markdown,
        filename
    )

    print(f"\n✅ 周报已保存：{filename}")
    
    # 返回文件路径，方便外部知道执行成功了
    return filename

if __name__ == "__main__":
    # 保留直接运行 main.py 的能力以供测试
    main()