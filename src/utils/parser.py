import re
from datetime import datetime
from models.event import Event

# 主要作用：将读取的格式为字符串的日历数据，转化为python定义的event的格式。

def parse_chinese_datetime(text):
    """
    输入：
    2026年6月22日 星期一 15:00:00
    """

    m = re.search(
        r"(\d+)年(\d+)月(\d+)日.*?(\d+):(\d+):(\d+)",
        text
    )

    if not m:
        raise ValueError(f"无法解析日期：{text}")

    y, mo, d, h, mi, s = map(int, m.groups())

    return datetime(y, mo, d, h, mi, s)


def parse_events(raw_data):

    events = []

    if not raw_data:
        return events

    for line in raw_data.splitlines():

        if "|||" not in line:
            continue

        calendar, title, start_str, end_str = line.split("|||")

        events.append(
            Event(
                calendar=calendar.strip(),
                title=title.strip(),
                start=parse_chinese_datetime(start_str),
                end=parse_chinese_datetime(end_str)
            )
        )

    return events