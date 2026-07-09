import json
from openai import OpenAI
from engines.ai_prompt_builder import build_ai_prompt
from utils.config_loader import config

# 根据提示词生成周报模版中的核心投入项的分析，还有周总结

def call_deepseek(prompt):
    """
    调用 DeepSeek
    返回 JSON(dict)
    """

    client = OpenAI(
        api_key=config.ai["api_key"],
        base_url=config.ai["base_url"]
    )

    response = client.chat.completions.create(
        model=config.ai["model"],
        messages=[
            {
                "role": "system",
                "content": "你是一位专业的时间管理分析师。"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content

    print("\n========================")
    print("🤖 AI RESPONSE")
    print("========================")
    print(content)

    return json.loads(content)



def build_ai_report(report):
    """
    根据 WeekReport 自动生成 AI 分析结果

    输入：
        WeekReport

    输出：
        WeekReport
    """

    prompt = build_ai_prompt(report)

    try:

        ai = call_deepseek(prompt)

        report.ai_core_breakdown = ai.get("core_breakdown", {})

        report.ai_summary = ai.get("summary", {})

        return report

    except Exception as e:

        print("\n❌ AI 调用失败")
        print(e)

        report.ai_core_breakdown = {}

        report.ai_summary = {}

        return report