import logging
import os

def setup_logger():
    # 获取当前脚本所在的目录
    log_directory = os.path.dirname(os.path.abspath(__file__))
    log_file_path = os.path.join(log_directory, 'output.log')  # 在当前目录下创建日志文件

    # 创建或获取 'my_logger' 记录器
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # 创建文件处理器，指定 'mode' 为 'w' 以清空文件（覆盖模式）
    file_handler = logging.FileHandler(log_file_path, mode='w', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)

    # 创建控制台处理器，指定编码为 utf-8
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将处理器添加到记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
