import json

# 主要作用：生成ai所需的提示词

def build_ai_prompt(report):
    """
    根据 WeekReport 构建发送给 AI 的 Prompt
    """

    data = {}

    # ==========================
    # 分类统计
    # ==========================
    statistics = {}

    for category in report.category_order:

        if category not in report.week.calendars:
            continue

        stat = report.week.calendars[category]

        statistics[category] = {
            "hours": stat.hours,
            "average_per_day": stat.average_per_day,
            "record_ratio": stat.record_ratio,
            "awake_ratio": stat.awake_ratio
        }

    data["statistics"] = statistics

    # ==========================
    # 同名事件聚合
    # ==========================
    data["same_events"] = report.same_events

    # ==========================
    # 周对比
    # ==========================
    data["compare"] = report.compare

    # ==========================
    # Prompt
    # ==========================
    prompt = """
你是一名时间管理教练。

下面是一份用户一周时间统计数据。

请完成两个任务。

========================
任务一：核心投入拆解
========================

根据 same_events。

不要直接照抄事件名称。

请将相似事件进行语义合并，归纳成本周真正的核心投入。

例如：

创建Upwork简历
完善Upwork简历
查看Upwork任务

可以合并为：

Upwork接单准备

要求：

1. 每个分类输出3~5个核心投入（不足则全部输出）
2. 每个核心投入包含：
   - topic
   - hours
   - items
3. hours 为所有 items 的总时长

========================
任务二：周总结
========================

根据：

statistics

compare

写一段周总结。

要求包括：

1、本周最大的变化

2、本周做得好的地方

3、本周存在的问题

4、下周建议

控制在100~300字。

========================
输出格式
========================

请只返回 JSON。

格式如下：

{
    "core_breakdown": {
        "投资(重要&不紧急)": [
            {
                "topic": "Upwork接单准备",
                "hours": 6.5,
                "items": [
                    "创建简历",
                    "技能标签",
                    "查看任务"
                ]
            }
        ]
    },

    "summary": {
        "overall": "本周最大的变化是运动时间增加。",

        "good": [
            "投资时间依旧保持第一，占记录时间39.8%。",
            "开始恢复运动。"
        ],

        "bad": [
            "刷抖音时间增加。",
            "消费类时间下降较多。"
        ],

        "suggestions": [
            "限制抖音时间。",
            "保持运动。",
            "继续推进Upwork。"
        ]
    }
}

========================
下面是数据
========================

"""

    prompt += json.dumps(
        data,
        ensure_ascii=False,
        indent=2
    )

    return prompt
