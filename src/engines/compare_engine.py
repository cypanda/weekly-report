def build_compare(this_week, last_week):
    """
    周数据对比

    输入：
        this_week : WeekStatistics
        last_week : WeekStatistics

    输出：
        {
            "投资(重要&不紧急)": {
                "this_hours": ...,
                "last_hours": ...,
                "diff_hours": ...,
                "this_minutes": ...,
                "last_minutes": ...,
                "this_average": ...,
                "last_average": ...,
                "this_record_ratio": ...,
                "last_record_ratio": ...,
                "this_awake_ratio": ...,
                "last_awake_ratio": ...
            },
            ...
        }
    """

    result = {}

    categories = (
        set(this_week.calendars.keys())
        | set(last_week.calendars.keys())
    )

    for category in categories:

        this_stat = this_week.calendars.get(category)
        last_stat = last_week.calendars.get(category)

        # ---------- 本周 ----------
        if this_stat:
            this_hours = this_stat.hours
            this_average = this_stat.average_per_day
            this_record_ratio = this_stat.record_ratio
            this_awake_ratio = this_stat.awake_ratio
        else:
            this_hours = 0
            this_average = 0
            this_record_ratio = 0
            this_awake_ratio = 0

        # ---------- 上周 ----------
        if last_stat:
            last_hours = last_stat.hours
            last_average = last_stat.average_per_day
            last_record_ratio = last_stat.record_ratio
            last_awake_ratio = last_stat.awake_ratio
        else:
            last_hours = 0
            last_average = 0
            last_record_ratio = 0
            last_awake_ratio = 0

        result[category] = {

            "this_hours": round(this_hours, 2),
            "last_hours": round(last_hours, 2),

            "diff_hours": round(this_hours - last_hours, 2),

            "this_minutes": round(this_hours * 60),
            "last_minutes": round(last_hours * 60),

            "this_average": round(this_average, 2),
            "last_average": round(last_average, 2),

            "this_record_ratio": round(this_record_ratio, 1),
            "last_record_ratio": round(last_record_ratio, 1),

            "this_awake_ratio": round(this_awake_ratio, 1),
            "last_awake_ratio": round(last_awake_ratio, 1),
        }

    return result