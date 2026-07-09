from models.week_report import WeekReport
from engines.compare_engine import build_compare
from groupers.group_same_events import build_same_events

#主要作用：计算weekreport所需的数据

def build_week_report(
    week_statistics,
    day_statistics,
    events,
    last_week_report=None
):

    report = WeekReport(
        events=events,
        week=week_statistics,
        days=day_statistics
    )

    report.same_events = build_same_events(events)

    # 计算chart
    report.chart = {
        cat: sum(items.values())
        for cat, items in report.same_events.items()
    }

    report.category_order = [
        "投资(重要&不紧急)",
        "消费(重要&紧急)",
        "消耗(不重要&紧急)",
        "浪费(不重要&不紧急)",
        "运动健身(重要&不紧急)"
    ]

    report.compare = None

    if last_week_report:
        report.compare = build_compare(
            report.week,
            last_week_report.week
        )

    return report