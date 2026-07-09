import subprocess

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


def get_all_calendars():
    """
    读取Mac所有Calendar分类
    """

    script = PROJECT_ROOT / "scripts" / "get_calendars.scpt"

    result = subprocess.run(
        [
            "osascript",
            str(script)
        ],
        capture_output=True,
        text=True,
        check=True
    )

    calendars = [
        x.strip()
        for x in result.stdout.split(",")
        if x.strip()
    ]

    return calendars


def choose_calendars(calendars):
    """
    用户选择需要统计的Calendar
    """

    print()
    print("请选择需要统计的日历：")
    print()

    for index, calendar in enumerate(calendars, start=1):
        print(f"{index}. {calendar}")

    while True:

        print()

        selected = input(
            "请输入编号（多个请用英文逗号分隔）："
        )

        try:

            indexes = [
                int(x.strip()) - 1
                for x in selected.split(",")
            ]

            if any(i < 0 or i >= len(calendars) for i in indexes):
                raise ValueError

            return [calendars[i] for i in indexes]

        except ValueError:

            print("❌ 输入有误，请重新输入。")


def init_calendar():
    """
    初始化Calendar配置
    """

    calendars = get_all_calendars()

    selected = choose_calendars(calendars)

    return selected