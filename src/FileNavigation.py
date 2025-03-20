import os
import  json
from app.logs.log import setup_logger

logger = setup_logger()
from app.AI.Workflow import call_link_ai

from app.net.network import is_connected

import sys
import os
#
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))  # 添加当前目录到 sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))  # 添加 src 目录
from WebsiteContentSettings import websdata



def process_file(file_path,api_key,app_code,folder_path):



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















        max_retries = 3  # 最大重试次数
        retry_count = 0

        data = None  # 初始化

        while retry_count < max_retries:
            jsons = call_link_ai(api_key, app_code, url)
            try:
                data = json.loads(jsons)
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
                break  # 成功解析后退出循环
            except json.JSONDecodeError:
                retry_count += 1
                logger.info(f"第 {retry_count} 次重试...")

        if data is not None:
            logger.info("成功获取数据: %s", data)
        else:
            logger.info(f"超过 {max_retries} 次重试仍失败")
            from app.ftp.addweb import append_text_to_file
            print(folder_path)

            append_text_to_file(folder_path+"\\false\\url.txt", f"AI第{max_retries}不接受的网址："+url)

        # 打印最终的结果
        print("数据")
        print(data)










def fileall(folder_path,api_key,app_code):
    if is_connected:
        print(folder_path,api_key,app_code)

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
            process_file(current_file_path,api_key,app_code,folder_path)
            # 删除处理完的 txt 文件
            os.remove(current_file_path)
    else:
        logger.info("没有网络")



