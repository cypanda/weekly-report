from collections import defaultdict

from models.calendar_statistics import CalendarStatistics


def summary_by_calendar(events):
    
    # 根据 Event 计算 calendar_statistics中CalendarStatistics的数据

    minutes_map = defaultdict(int)

    for event in events:
        minutes_map[event.calendar] += event.duration_minutes

    result = {}

    for calendar, minutes in minutes_map.items():

        result[calendar] = CalendarStatistics(

            calendar=calendar,

            minutes=minutes,

            hours=round(minutes / 60, 1)

        )

    return result