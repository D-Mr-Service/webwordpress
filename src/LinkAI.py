
import json


from src.FileNavigation import fileall
from app import Clean_up_RLs

def run():


    # 打开并读取 config.json 文件
    with open('./config.json', 'r') as file:
        config = json.load(file)
    # 访问里面的参数
    app_code = config["code"]
    api_key = config["key"]
    filed = config["file"]

    if Clean_up_RLs(filed):
        fileall(filed,api_key,app_code)



