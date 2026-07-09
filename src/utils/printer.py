from models.day_statistics import DayStatistics
from models.period_statistics import PeriodStatistics
import json

def print_events(events):

    print("\n===== Event 调试 =====")

    for event in events:
        print(
            f"[{event.calendar}] "
            f"{event.title} | "
            f"{event.start.strftime('%Y-%m-%d %H:%M')} ~ "
            f"{event.end.strftime('%H:%M')} | "
            f"{event.duration_hours:.2f}h"
        )


def print_days(days: list[DayStatistics]):

    print("\n========================")
    print("DayStatistics")
    print("========================")

    for day in days:

        print(day.date)

        print(f"记录：{day.recorded_hours:.1f}h")
        print(f"睡觉：{day.sleep_hours:.1f}h")
        print(f"未记录：{day.missing_hours:.1f}h")

        print()

        for stat in day.calendars.values():
            print(f"   {stat.calendar}: {stat.hours:.1f}h")

        print("------------------------")


def print_week(week: PeriodStatistics):

    print("\n========================")
    print("WeekStatistics")
    print("========================")

    print(f"开始日期：{week.start_date}")
    print(f"结束日期：{week.end_date}")

    print()

    print(f"记录：{week.record_hours:.1f}h")
    print(f"睡觉：{week.sleep_hours:.1f}h")
    print(f"未记录：{week.missing_hours:.1f}h")
    print(f"清醒：{week.awake_hours:.1f}h")

    print()

    for stat in week.calendars.values():

        print(stat.calendar)
        print(f"{stat.hours:.1f}h")
        print("--------------------")


def print_compare(report):

    print("\n========================")
    print("📈 WEEK COMPARE DEBUG")
    print("========================")

    if not report.compare:
        print("暂无上周数据")
        return

    for category in report.category_order:

        if category not in report.compare:
            continue

        item = report.compare[category]

        print(f"\n【{category}】")

        print(
            f"本周："
            f"{item['this_hours']}h "
            f"({item['this_minutes']}min)"
        )

        print(
            f"上周："
            f"{item['last_hours']}h "
            f"({item['last_minutes']}min)"
        )

        print(
            f"平均每天："
            f"{item['this_average']}h"
            f" → "
            f"{item['last_average']}h"
        )

        print(
            f"记录占比："
            f"{item['this_record_ratio']}%"
            f" → "
            f"{item['last_record_ratio']}%"
        )

        print(
            f"清醒占比："
            f"{item['this_awake_ratio']}%"
            f" → "
            f"{item['last_awake_ratio']}%"
        )

        diff = item["diff_hours"]

        if diff > 0:
            print(f"环比：↑ +{diff:.2f}h")
        elif diff < 0:
            print(f"环比：↓ {diff:.2f}h")
        else:
            print("环比：0h")


def print_chart(report):

    print("\n========================")
    print("📊 CHART DEBUG")
    print("========================")

    for k, v in report.chart.items():
        print(f"{k}: {v:.2f}h")


def print_ai(report):

    print("\n========================")
    print("AI JSON")
    print("========================")

    if not report.ai_core_breakdown:
        print("AI 未生成结果")
        return

    print(json.dumps(
        {
            "core_breakdown": report.ai_core_breakdown,
            "summary": report.ai_summary
        },
        ensure_ascii=False,
        indent=2
    ))

def print_report(report):

    print("\n========================")
    print("📦 REPORT DEBUG")
    print("========================")

    print("same_events:", list(report.same_events.keys()))
    print("compare:", report.compare is not None)
    print("chart:", list(report.chart.keys()))
    print("ai_core:", list(report.ai_core_breakdown.keys()))
    print("summary:", bool(report.ai_summary))