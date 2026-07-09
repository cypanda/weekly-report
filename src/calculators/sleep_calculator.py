# 主要作用：计算day statistics中定义的sleep-hours和missing-hours

def calculate_sleep(day_statistics_list):

    for day in day_statistics_list:

        # 一整天完全没有记录
        if day.recorded_hours == 0:

            day.sleep_hours = 0

            day.missing_hours = 24

        else:

            day.sleep_hours = round(
                24 - day.recorded_hours,
                2
            )

            day.missing_hours = 0

    return day_statistics_list