import requests

from src.app.logs.log import setup_logger

logger = setup_logger()
def call_link_ai(api_key, app_code, web_url):
    """
    调用 Link-AI API 的简化封装函数

    参数：
        api_key: API 密钥（字符串）
        app_code: 应用代码（字符串）
        web_url: 请求内容（字符串）

    返回：
        API 返回的文本结果，如果请求失败则返回 None
    """
    url = "https://api.link-ai.tech/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key  # 注意：Bearer 后面必须有一个空格
    }
    payload = {
        "app_code": app_code,
        "messages": [
            {"role": "user", "content": web_url}
        ]
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        reply = response.json().get("choices")[0]['message']['content']
        logger.info("ai返回结构成功")
        logger.info(reply)
        # print(reply)
        return reply
    else:
        error = response.json().get("error", {})
        logger.debug(f"请求异常, 错误码={response.status_code}, 错误类型={error.get('type')}, 错误信息={error.get('message')}")

        return None

