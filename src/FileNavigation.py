import os
import  json
from src.app import setup_logger

logger = setup_logger()
from src.app.AI.Workflow import call_link_ai



import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 添加当前目录到 sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))  # 添加 src 目录
from src.WebsiteContentSettings import websdata



def process_file(file_path,api_key,app_code):



    # 获取文件名（不含扩展名）
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    logger.info(base_name)  # 打印文件名

    # 读取所有网址（每行一个，不包含空行）
    with open(file_path, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    # 当文件内还有网址时，逐条打印并删除已打印的网址
    while urls:
        # 取出第一个网址
        url = urls.pop(0)
        print(url)
        jsons = call_link_ai(api_key, app_code, url)
        data = json.loads(jsons)

        print("数据")
        print(data)
        # 获取 Keywords 和 describe
        keywords = data.get("Keywords", "")
        description = data.get("describe", "")
        content = data.get("content", "")
        name = data.get("name", "")
        websdata(
            content,
            url,
            description,
            description,
            keywords,
            description,
            base_name,
            name
        )
        # 将剩余的网址写回文件，覆盖原有内容
        with open(file_path, "w", encoding="utf-8") as f:
            if urls:
                f.write("\n".join(urls))
            else:
                f.write("")

def fileall(folder_path,api_key,app_code):
    print(folder_path,api_key,app_code)
    #
    # 循环处理文件夹中的所有 txt 文件
    while True:
        # 获取所有 .txt 文件
        txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
        if not txt_files:
            logger.info("完成打印")
            break

        # 排序后取第一个 txt 文件
        txt_files.sort()
        current_file = txt_files[0]
        current_file_path = os.path.join(folder_path, current_file)

        # 处理当前 txt 文件
        process_file(current_file_path,api_key,app_code)
        # 删除处理完的 txt 文件
        os.remove(current_file_path)



