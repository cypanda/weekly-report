def choose_focus_categories(calendars):
    """
    选择AI需要重点分析的分类
    """

    print()
    print("请选择需要 AI 深度分析的分类（建议选择1~2个）：")
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

            return [
                calendars[i]
                for i in indexes
            ]

        except ValueError:

            print("❌ 输入有误，请重新输入。")