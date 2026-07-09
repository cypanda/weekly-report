from dataclasses import dataclass

@dataclass
class CalendarStatistics:

    #主要作用：定义了日历的5类子项的统计信息的数据格式
    
    calendar: str

    hours: float = 0
    minutes: int = 0

    # 占记录时间
    record_ratio: float = 0

    # 占清醒时间
    awake_ratio: float = 0

    # 平均每天
    average_per_day: float = 0