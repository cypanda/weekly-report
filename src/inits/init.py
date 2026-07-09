import sys
import os
from pathlib import Path

# 路径魔法：确保 Python 能顺利找到 src 目录下的所有模块
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
sys.path.append(str(project_root))

from inits.calendar_init import init_calendar
from inits.focus_category_init import choose_focus_categories
from inits.ai_init import init_ai
from inits.report_init import init_report_dir
from inits.config_writer import save_configuration

def check_existing_config():
    """
    步骤 ①：检测是否已有配置
    """
    config_dir = Path.home() / ".weekly_report"
    config_file = config_dir / "config.yaml"
    
    if config_file.exists():
        print(f"\n⚠️ 检测到已存在配置文件：{config_dir}")
        while True:
            choice = input("是否覆盖现有配置并重新初始化？(y/n): ").strip().lower()
            if choice == 'y':
                return True
            elif choice == 'n':
                print("已取消初始化操作。")
                sys.exit(0)  # 安全退出程序
            else:
                print("❌ 请输入 y 或 n。")
    return True

def main():
    """
    初始化主流程总控
    """
    print("========================================")
    print("        欢迎使用 Weekly Report          ")
    print("========================================")
    
    # 1. 检查历史配置
    check_existing_config()
    
    try:
        # 2. 配置日历 (读取 Mac 日历并让用户勾选)
        calendars = init_calendar()
        
        # 3. 选定深度分析分类 (基于上一步勾选的日历)
        focus_categories = choose_focus_categories(calendars)
        
        # 4. 配置 AI (服务商、URL、Key、模型)
        ai_config = init_ai()
        
        # 5. 配置输出目录 (弹 Finder 窗口)
        report_config = init_report_dir()
        
        # 6. 保存所有配置到 ~/.weekly_report
        save_configuration(calendars, focus_categories, ai_config, report_config)
        
        print("\n🎉 初始化大功告成！现在你可以使用生成周报的功能了。")
        print("========================================\n")
        
    except KeyboardInterrupt:
        # 优雅处理用户中途按下 Ctrl+C 强行退出的情况
        print("\n\n🛑 初始化已中断。")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 初始化过程中发生未知错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()