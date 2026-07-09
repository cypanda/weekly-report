from models.calendar_statistics import CalendarStatistics
from models.period_statistics import PeriodStatistics

# 主要作用：计算period statistics所需的数据

def build_period_statistics(day_statistics):
    
    if not day_statistics:
        return PeriodStatistics(
            start_date="",
            end_date=""
        )
    
    period_statistics = PeriodStatistics(
        start_date=day_statistics[0].date,
        end_date=day_statistics[-1].date
    )

    period_days = len(day_statistics)
    period_hours = period_days * 24

    period_statistics.period_days = period_days
    period_statistics.period_hours = period_hours
    
    for day in day_statistics:

        period_statistics.record_hours += day.recorded_hours
        period_statistics.sleep_hours += day.sleep_hours
        period_statistics.missing_hours += day.missing_hours

        for calendar, stat in day.calendars.items():

            if calendar not in period_statistics.calendars:

                period_statistics.calendars[calendar] = CalendarStatistics(
                    calendar=calendar,
                )

            period_statistics.calendars[calendar].minutes += stat.minutes

    period_statistics.awake_hours = period_statistics.record_hours + period_statistics.missing_hours

    period_statistics.average_record_hours = round(
        period_statistics.record_hours / period_statistics.period_days,
        1
    )

    period_statistics.average_awake_hours = round(
        period_statistics.awake_hours / period_statistics.period_days,
        1
    )

    for stat in period_statistics.calendars.values():

        # 小时
        stat.hours = round(
            stat.minutes / 60,
            1
        )

        # 平均每天
        stat.average_per_day = round(
            stat.hours / period_statistics.period_days,
            2
        )

        # 占记录时间
        if period_statistics.record_hours > 0:
            stat.record_ratio = round(
                stat.hours / period_statistics.record_hours * 100,
                1
            )

        # 占清醒时间
        if period_statistics.awake_hours > 0:
            stat.awake_ratio = round(
                stat.hours / period_statistics.awake_hours * 100,
                1
            )

    return period_statistics