from pathlib import Path
import yaml
from dotenv import load_dotenv
import os
import sys

class Config:
    """
    项目配置
    """
    def __init__(self):
        # 核心改动：把路径指向用户家目录下的隐藏文件夹
        config_dir = Path.home() / ".weekly_report"
        
        # -------------------------
        # config.yaml
        # -------------------------
        config_path = config_dir / "config.yaml"
        
        # 防呆设计：如果没有找到配置文件，说明用户还没初始化
        if not config_path.exists():
            print("❌ 未找到配置文件！请先执行初始化命令完成配置。")
            sys.exit(1) # 安全退出程序

        with open(config_path, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

        # -------------------------
        # .env
        # -------------------------
        env_path = config_dir / ".env"
        
        # 加载 .env 变量到系统环境变量中
        if env_path.exists():
            load_dotenv(env_path)

        self.ai = {
            "provider": os.getenv("AI_PROVIDER"),
            "api_key": os.getenv("AI_API_KEY"),
            "base_url": os.getenv("AI_BASE_URL"),
            "model": os.getenv("AI_MODEL")
        }

    @property
    def calendars(self):
        return self.data["calendar"]["selected"]

    @property
    def focus_categories(self):
        return self.data["analysis"]["focus_categories"]

    @property
    def output_path(self):
        return self.data["report"]["output_path"]

    @property
    def sleep_mode(self):
        return self.data["time"]["sleep_mode"]

# 实例化单例，其他文件直接 from utils.config_loader import config 即可使用
config = Config()