from dataclasses import dataclass, field
from models.period_statistics import PeriodStatistics
from models.day_statistics import DayStatistics

#主要作用：定义了周报模版所需的数据结构

@dataclass
class WeekReport:

    week: PeriodStatistics
    days: list[DayStatistics]

    # 原始事件
    events: list = field(default_factory=list)

    # 聚合后的事件（核心）
    same_events: dict = field(default_factory=dict)

    # 展示顺序
    category_order: list[str] = field(default_factory=list)

    # ai核心投入拆解
    ai_core_breakdown: dict = field(default_factory=dict)

    chart: dict = field(default_factory=dict)

    compare = None

    # ai周报总结
    ai_summary: str = ""