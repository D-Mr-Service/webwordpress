import requests
from bs4 import BeautifulSoup

def get_website_title(url):
    try:
        # 发送 HTTP 请求
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查请求是否成功

        # 解析 HTML 内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 提取标题标签内容
        title_tag = soup.find('title')

        if title_tag:
            return title_tag.text.strip()
        else:
            return False

    except requests.exceptions.RequestException as e:
        return False
    except Exception as e:
        return False

