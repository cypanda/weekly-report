from dataclasses import dataclass, field
from typing import Dict

from models.calendar_statistics import CalendarStatistics

# 主要作用：定义日统计的数据格式

@dataclass
class DayStatistics:
    """
    一天的统计结果
    """

    date: str

    total_hours: float = 24

    recorded_hours: float = 0

    sleep_hours: float = 0

    missing_hours: float = 0

    calendars: Dict[str, CalendarStatistics] = field(default_factory=dict)