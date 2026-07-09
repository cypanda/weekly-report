from dataclasses import dataclass, field
from typing import Dict

from models.calendar_statistics import CalendarStatistics

# 主要作用：定义了一定周期内的统计的数据格式，例如周统计、月统计。

@dataclass
class PeriodStatistics:
    """
    任意时间段统计结果
    """

    # 时间范围
    start_date: str
    end_date: str

    # 统计周期（小时）
    period_hours: float = 0

    # 统计周期（天）
    period_days: int = 0

    # 总统计
    record_hours: float = 0
    sleep_hours: float = 0
    missing_hours: float = 0
    awake_hours: float = 0

    # 平均每天
    average_record_hours: float = 0
    average_awake_hours: float = 0

    # 各分类统计
    calendars: Dict[str, CalendarStatistics] = field(default_factory=dict)