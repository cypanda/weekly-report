import os
from pathlib import Path
import yaml

# 指向用户家目录下的隐藏文件夹
CONFIG_DIR = Path.home() / ".weekly_report"

def write_yaml(calendars, focus_categories, output_path):
    """
    生成并写入 config.yaml 文件
    """
    # 组装成标准的 Python 字典结构
    config_data = {
        "calendar": {
            "selected": calendars
        },
        "analysis": {
            "focus_categories": focus_categories
        },
        "report": {
            "output_path": output_path
        },
        "time": {
            "sleep_mode": "auto"
        }
    }
    
    # 确保文件夹存在 (parents=True 代表如果父目录不存在也会一并创建)
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    yaml_file = CONFIG_DIR / "config.yaml"
    
    # 使用 pyyaml 的 safe_dump 自动生成 YAML
    # allow_unicode=True 保证中文正常显示而不是转码成 \uXXXX
    # default_flow_style=False 和 sort_keys=False 保证排版换行且按我们字典的顺序输出
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.safe_dump(config_data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        
    return yaml_file

def write_env(ai_config):
    """
    生成并写入 .env 文件
    """
    lines = []
    for key, value in ai_config.items():
        lines.append(f"{key}={value}")
    
    env_content = "\n".join(lines) + "\n"
    
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    env_file = CONFIG_DIR / ".env"
    
    with open(env_file, "w", encoding="utf-8") as f:
        f.write(env_content)
        
    return env_file

def save_configuration(calendars, focus_categories, ai_config, report_config):
    """
    统筹保存所有配置的公共入口
    """
    print("\n正在生成配置文件...")
    
    yaml_path = write_yaml(calendars, focus_categories, report_config["output_path"])
    print(f"✅ YAML 配置已保存至: {yaml_path}")
    
    env_path = write_env(ai_config)
    print(f"✅ ENV  密钥已保存至: {env_path}")
    
    return True

if __name__ == "__main__":
    # 本地测试用的模拟数据
    mock_calendars = ["投资(重要&不紧急)", "消费(重要&紧急)"]
    mock_focus = ["投资(重要&不紧急)"]
    mock_ai = {
        "AI_PROVIDER": "deepseek",
        "AI_BASE_URL": "https://api.deepseek.com",
        "AI_API_KEY": "sk-test123456789",
        "AI_MODEL": "deepseek-chat"
    }
    mock_report = {"output_path": "/Users/cypanda/Desktop"}
    
    save_configuration(mock_calendars, mock_focus, mock_ai, mock_report)
    print("\n测试完成！")
    print("你可以去终端输入 `open ~/.weekly_report` 查看生成的文件。")