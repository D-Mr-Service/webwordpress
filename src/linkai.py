import json
import time


import sys
from pathlib import Path

from src.FileNavigation import fileall
from src.app.ftp.accessibleURL import Clean_up_RLs
from src.app.logs.log import setup_logger
from src.app.net.network import is_connected

# # 获取当前文件的绝对路径（假设 linkai.py 在 src 目录下）
# current_dir = Path(__file__).parent
# # 获取项目根目录（假设项目根目录是 src 的父目录 NavigationAutomatic）
# project_root = current_dir.parent
# # 将根目录添加到 Python 路径
# sys.path.append(str(project_root))

# 然后使用绝对路径导入
# from FileNavigation import fileall
logger = setup_logger()
def run():
    if is_connected():
        while True:
            try:
                # 打开并读取 config.json 文件
                with open('./config.json', 'r') as file:
                    config = json.load(file)

                # 访问里面的参数
                app_code = config["code"]
                api_key = config["key"]
                filed = config["file"]

                if Clean_up_RLs(filed) & is_connected():
                    fileall(filed, api_key, app_code)

                # 如果执行成功，退出循环
                break

            except Exception as e:
                logger.info(f"捕获到异常: {str(e)}")
                logger.info("5秒后重新开始...")
                time.sleep(5)  # 避免频繁重试，添加适当延迟
                logger.info("检测到本地网络连接")

    else:
        logger.info("未检测到网络连接")

run()

