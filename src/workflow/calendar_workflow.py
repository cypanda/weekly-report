from pathlib import Path
import os
import subprocess

from utils.parser import parse_events

# 主要作用：数据获取流程的组装，从日历获取数据到形成events。

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def fetch_events_from_mac(
    cal_name,
    start_date,
    end_date
):
    """
    从 Apple Calendar 读取指定日历事件
    """

    script_path = str(
        PROJECT_ROOT / "scripts" / "calendar.scpt"
    )

    args = [
        "osascript",
        script_path,
        cal_name,
        str(start_date.year),
        str(start_date.month),
        str(start_date.day),
        str(end_date.year),
        str(end_date.month),
        str(end_date.day),
    ]

    # print(args)
    # print(script_path)
    # print(os.path.exists(script_path))

    try:

        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout.strip()

    except subprocess.CalledProcessError as e:

        print("========== AppleScript Error ==========")
        print("returncode:", e.returncode)
        print("stderr:", e.stderr)
        print("stdout:", e.stdout)

        return ""



def fetch_events(
    calendars,
    start_date,
    end_date
):
    all_events = []

    for calendar in calendars:

        raw = fetch_events_from_mac(
            calendar,
            start_date,
            end_date
        )

        print(f"\n====== {calendar} ======")

        if not raw:
            print("没有读取到数据")
            continue

        # print(raw[:300])     # 打印前300个字符

        events = parse_events(raw)

        print(f"解析得到：{len(events)} 条")

        all_events.extend(events)

    print(f"\n总 Event 数：{len(all_events)}")

    return all_events