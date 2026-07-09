from datetime import datetime, timedelta


def get_week_range(weeks_ago=0):
    """
    获取某一周（周一~周日）

    weeks_ago:
        0 = 本周
        1 = 上周
        2 = 上上周
    """

    today = datetime.today()

    monday = today - timedelta(days=today.weekday())

    monday = monday - timedelta(weeks=weeks_ago)

    sunday = monday + timedelta(days=6)

    return monday, sunday