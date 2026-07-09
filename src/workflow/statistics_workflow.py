from calculators.day_calculator import build_day_statistics
from calculators.period_calculator import build_period_statistics

# 主要作用：统计流程的组装，从events获取数据到day statistics，再到period statistics。

def build_statistics(
    events,
    start_date,
    end_date
):
    """
    统计流程：

    Event
        ↓
    DayStatistics
        ↓
    PeriodStatistics

    返回：
        days,
        period_statistics
    """

    days = build_day_statistics(
        events,
        start_date,
        end_date
    )

    period_statistics = build_period_statistics(
        days
    )

    return days, period_statistics