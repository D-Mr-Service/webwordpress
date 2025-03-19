import socket
import requests
from src.app import setup_logger

logger = setup_logger()
def get_country_by_domain(domain):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        # 解析域名获取IP地址
        ip = socket.gethostbyname(domain)
    except socket.gaierror as e:
        return f"错误: 无法解析域名 '{domain}'，原因：{e}"

    try:
        # 请求IP地理信息
        response = requests.get(f"http://ip-api.com/json/{ip}", headers=headers)
        response.raise_for_status()  # 检查HTTP错误状态码
        data = response.json()

        if data.get('status') == 'success':
            return data.get('country', '未知国家')
        else:
            return f"错误: {data.get('message', '未知错误')}"
    except requests.exceptions.RequestException as e:
        return f"错误: 请求API失败 - {e}"
    except ValueError:
        return "错误: 解析API响应失败"

# 测试代码
def ipwebcountry(urls):

    url = urls.replace("https://", "").rstrip("/")
    result = get_country_by_domain(url)
    logger.info(result)
    return result
