def choose_ai_provider():
    """
    让用户选择 AI 服务商
    """
    providers = {
        1: {"name": "DeepSeek 官方", "provider_id": "deepseek", "base_url": "https://api.deepseek.com"},
        2: {"name": "OpenAI 官方", "provider_id": "openai", "base_url": "https://api.openai.com/v1"},
        3: {"name": "OpenRouter", "provider_id": "openrouter", "base_url": "https://openrouter.ai/api/v1"},
        4: {"name": "SiliconFlow (硅基流动)", "provider_id": "siliconflow", "base_url": "https://api.siliconflow.cn/v1"},
        5: {"name": "火山方舟", "provider_id": "volcengine", "base_url": "https://ep.api.volcengine.com/api/v3"},
        6: {"name": "阿里百炼", "provider_id": "dashscope", "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1"},
        7: {"name": "其他 OpenAI 兼容平台", "provider_id": "custom", "base_url": ""}
    }

    print("\n==========================")
    print("AI 配置")
    print("==========================\n")
    print("请选择AI服务：\n")

    for key, val in providers.items():
        print(f"{key}. {val['name']}")

    while True:
        print()
        selected = input("请输入编号：").strip()

        try:
            index = int(selected)
            if index not in providers:
                raise ValueError
            
            return providers[index]

        except ValueError:
            print("❌ 输入有误，请重新输入 1-7 的数字。")


def init_ai():
    """
    初始化 AI 配置，返回字典格式的配置项，供后续写入 .env
    """
    provider_info = choose_ai_provider()
    
    provider_id = provider_info["provider_id"]
    base_url = provider_info["base_url"]
    name = provider_info["name"]

    print()
    
    # 如果用户选择自定义平台，需要额外输入 Base URL
    if provider_id == "custom":
        while True:
            custom_url = input("请输入 Base URL (例如 https://api.example.com/v1)：\n> ").strip()
            if custom_url:
                base_url = custom_url
                break
            print("❌ Base URL 不能为空，请重新输入。")
        print()

    # 输入 API Key
    while True:
        api_key = input(f"请输入 {name} 的 API Key：\n> ").strip()
        if api_key:
            break
        print("❌ API Key 不能为空，请重新输入。")
    print()

    # 输入 Model
    while True:
        print("请输入模型名称 (例如 deepseek-chat, gpt-4o, kimi-k2 等)：")
        model = input("> ").strip()
        if model:
            break
        print("❌ 模型名称不能为空，请重新输入。")

    # 返回结构化的配置数据，等待后续 config_writer.py 写入 .env
    return {
        "AI_PROVIDER": provider_id,
        "AI_BASE_URL": base_url,
        "AI_API_KEY": api_key,
        "AI_MODEL": model
    }


if __name__ == "__main__":
    # 简单的本地测试逻辑
    ai_config = init_ai()
    print("\n✅ AI 配置获取成功：")
    print(ai_config)