from workflow.calendar_workflow import fetch_events
from workflow.statistics_workflow import build_statistics

from builders.report_builder import build_week_report

# 主要作用：生成周报流程的组装，将数据获取流程、统计流程、生成周报三个过程组装起来，能直接生成周报。

def build_week_report_workflow(
    calendars,
    start_date,
    end_date,
    last_week_report=None
):
    """
    Calendar
        ↓
    Event
        ↓
    PeriodStatistics
        ↓
    WeekReport
    """

    events = fetch_events(
        calendars,
        start_date,
        end_date
    )

    days, period_statistics = build_statistics(
        events,
        start_date,
        end_date
    )

    report = build_week_report(
        period_statistics,
        days,
        events,
        last_week_report
    )

    return report