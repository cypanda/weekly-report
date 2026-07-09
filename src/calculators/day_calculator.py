from collections import defaultdict

from models.day_statistics import DayStatistics
from calculators.calendar_calculator import summary_by_calendar
from calculators.sleep_calculator import calculate_sleep
from datetime import timedelta

#主要作用：计算day statistics所需的数据

def build_day_statistics(events, start_date, end_date):

    """
    根据 日期 返回每天统计结果
    """
    day_events = defaultdict(list)

    for event in events:

        key = event.start.strftime("%Y-%m-%d")

        day_events[key].append(event)

    result = []

    current = start_date

    while current <= end_date:

        date_str = current.strftime("%Y-%m-%d")

        event_list = day_events.get(date_str, [])

        summary = summary_by_calendar(event_list)

        day = DayStatistics(date=date_str)

        day.calendars = summary

        day.recorded_hours = round(
            sum(item.hours for item in summary.values()),
            2
        )

        result.append(day)

        current += timedelta(days=1)

    # ============================
    # 自动计算睡眠/未记录
    # =========================
    result=calculate_sleep(result)

    return result