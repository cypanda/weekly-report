import subprocess

def init_report_dir():
    """
    呼出 Mac 的 Finder 让用户选择周报保存目录
    """
    print("\n==========================")
    print("输出目录配置")
    print("==========================\n")
    print("即将打开 Finder (访达)，请选择你的周报保存文件夹...")
    
    # 这段 AppleScript 会弹出一个文件夹选择框，并把选中的结果转换成标准的 Unix 路径 (POSIX path)
    script = 'return POSIX path of (choose folder with prompt "请选择周报保存目录：")'
    
    while True:
        try:
            # 运行 AppleScript
            result = subprocess.run(
                ['osascript', '-e', script],
                capture_output=True,
                text=True,
                check=True
            )
            
            # 清理苹果脚本返回数据自带的换行符
            selected_path = result.stdout.strip()
            
            if selected_path:
                print(f"✅ 成功设定保存目录：{selected_path}")
                # 返回准备写入 config.yaml 的格式
                return {
                    "output_path": selected_path
                }
                
        except subprocess.CalledProcessError:
            # 当用户在弹窗里点击了“取消”按钮时，AppleScript 会报错退出
            print("\n⚠️ 你取消了选择。")
            print("生成周报必须指定一个保存位置，请重新选择。")
            input("按回车键再次打开 Finder...")

if __name__ == "__main__":
    # 本地测试代码
    report_config = init_report_dir()
    print("\n最终返回的配置：")
    print(report_config)