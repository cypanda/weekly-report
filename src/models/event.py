from dataclasses import dataclass
from datetime import datetime

# 主要作用：定义基础的event事件的数据格式

@dataclass
class Event:

    #从日历里接入数据后，转变成如下格式存储
    calendar: str  #子项分类
    title: str    #具体事件名称
    start: datetime
    end: datetime

    @property
    def duration_minutes(self):
        return int((self.end - self.start).total_seconds() / 60)

    @property
    def duration_hours(self):
        return self.duration_minutes / 60