"""
LinkAI 环境检测与启动模块
功能：1. 显示ASCII LOGO 2.环境检测 3.启动核心服务
"""

import sys
import platform
import socket
import pyfiglet


from linkai import  run
from app.logs.log import setup_logger
import sys
import os
# # 添加 src 目录到 sys.path 中
# sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

logger = setup_logger()

def show_banner():
    """显示ASCII艺术字"""
    try:
        ascii_art = pyfiglet.figlet_format("D-MR.CN", font="standard")
        print(f"\033[36m{ascii_art}\033[0m")  # 青色显示
    except pyfiglet.FontNotFound:
        logger.info("D-MR.CN")

def generate_environment_info():
    """生成环境信息字符串"""
    return (
        f"Python版本: {sys.version.split()[0]}\n"
        f"操作系统: {platform.system()} {platform.release()}\n"
        f"主机名: {socket.gethostname()}"
    )

def run_linkai_logic():
    """运行D-MR.CN核心服务"""
    logger.info("🟢 D-MR.CN 正在运行")
    run()


def main():
    """主程序入口"""
    # 显示ASCII标识
    show_banner()

    # 显示环境信息
    env_info = generate_environment_info()
    logger.info(f"{'-'*40}\n环境检测结果：\n{env_info}\n{'-'*40}")

    # 运行核心逻辑
    try:
        run_linkai_logic()
    except KeyboardInterrupt:
        logger.info("\n🛑 接收到停止信号")
    except Exception as e:
        logger.error(f"❌ 核心服务运行失败: {str(e)}")

if __name__ == "__main__":
    main()