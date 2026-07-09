import sys
import os
import traceback
from datetime import datetime
from pathlib import Path

# 导入初始化模块的主函数
from inits.init import main as init_main

def record_log(command, status, message=""):
    """
    极简日志记录器：将每次运行结果追加到 ~/.weekly_report/history.log
    """
    try:
        config_dir = Path.home() / ".weekly_report"
        config_dir.mkdir(parents=True, exist_ok=True)
        log_file = config_dir / "history.log"
        
        # 核心魔法：通过检查环境变量，判断是终端运行还是快捷指令运行
        run_source = os.getenv("WEEKLY_REPORT_SOURCE", "Terminal/Cursor")
        
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{time_str}] [来源: {run_source}] [指令: {command.upper()}] [结果: {status}] {message}\n"
        
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_line)
    except Exception as e:
        # 日志写入本身不能影响主程序运行，所以如果报错就默默打印一下
        print(f"⚠️ 写入运行日志失败: {e}")

def main():
    """
    CLI 命令行总入口
    """
    if len(sys.argv) < 2:
        print("用法错误！请使用以下命令：")
        print("  weekly-report init  -> 初始化配置")
        print("  weekly-report run   -> 生成本周周报")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "init":
        print("⚙️ 开始执行初始化向导...")
        init_main()
        # 记录日志
        record_log("init", "SUCCESS", "完成了初始化配置")
        
    elif command == "run":
        print("🚀 开始收集日历数据并呼叫 AI...")
        try:
            import main as run_main
            output_file = run_main.main()
            
            # 记录成功日志
            record_log("run", "SUCCESS", f"周报生成成功: {output_file}")
            
        except ImportError as e:
            error_msg = f"找不到核心模块: {e}"
            print(f"\n❌ 运行失败，{error_msg}")
            record_log("run", "FAILED", error_msg)
        except Exception as e:
            print(f"\n❌ 糟糕，运行过程中出现了错误：")
            traceback.print_exc()
            # 记录失败日志，把简短的错误原因写进去
            record_log("run", "FAILED", f"运行时异常: {str(e)}")
    else:
        print(f"未知命令: {command}")
        record_log(command, "INVALID", "输入了未知的命令")

if __name__ == "__main__":
    main()