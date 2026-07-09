from collections import defaultdict

# 主要作用：将event中的事件名称相同的时长统计起来，给到ai去再一次根据语义将事件进行合并。

def group_events_by_calendar(events):
    """
    按 calendar 分组

    输入：
        List[Event]

    输出：
        Dict[str, List[Event]]
    """

    grouped = defaultdict(list)

    for event in events:
        grouped[event.calendar].append(event)

    return grouped


def build_same_events(events):
    """
    根据所有 Event

    生成：

    {
        "投资":{
            "创建简历":3.5,
            "学习英语":2.0
        }
    }

    输入：
        List[Event]

    输出：
        Dict[str, Dict[str,float]]
    """

    calendar_groups = group_events_by_calendar(events)

    result = {}

    for calendar, event_list in calendar_groups.items():

        title_hours = defaultdict(float)

        for event in event_list:

            title_hours[event.title] += event.duration_hours

        result[calendar] = dict(title_hours)

    return result
