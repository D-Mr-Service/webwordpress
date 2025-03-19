"""
LinkAI 环境检测与HTTP服务模块
功能：1. 显示ASCII LOGO 2.环境检测 3.启动HTTP服务
"""

import sys
import platform
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import pyfiglet
from LinkAI import run
from src.app import setup_logger

logger = setup_logger()
class HealthCheckHandler(BaseHTTPRequestHandler):
    """自定义HTTP请求处理器"""

    def do_GET(self):
        """处理GET请求并返回环境信息"""
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        env_info = self.generate_environment_info()
        self.wfile.write(env_info.encode())

    @staticmethod
    def generate_environment_info():
        """生成环境信息字符串"""
        return (
            f"Python版本: {sys.version.split()[0]}\n"
            f"操作系统: {platform.system()} {platform.release()}\n"
            f"主机名: {socket.gethostname()}"
        )

def show_banner():
    """显示ASCII艺术字"""
    try:
        ascii_art = pyfiglet.figlet_format("D-MR.CN", font="standard")
        print(f"\033[36m{ascii_art}\033[0m")  # 青色显示
    except pyfiglet.FontNotFound:
        logger.info("D-MR.CN")  # 备用显示

def run_linkai_logic():
    """运行D-MR.CN"""

    run()
    logger.info("🟢 D-MR.CN 正在运行")


def start_http_server(port=8080):
    """启动HTTP服务器"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, HealthCheckHandler)


    logger.info(f"🛑 按 CTRL+C 停止服务\n{'-'*40}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info("\n🛑 接收到停止信号")
    finally:
        httpd.server_close()
        logger.info("✅ HTTP服务已安全关闭")

def main():
    """主程序入口"""
    # 显示ASCII标识
    show_banner()

    # 运行核心逻辑
    run_linkai_logic()

    # 显示环境信息
    env_info = HealthCheckHandler.generate_environment_info()
    logger.info(f"{'-'*40}\n环境检测结果：\n{env_info}\n{'-'*40}")

    # 启动HTTP服务
    try:
        start_http_server(port=8080)
    except PermissionError:
        logger.info(f"❌ 错误：端口8080需要管理员权限")
    except Exception as e:
        logger.info(f"❌ 服务启动失败：{str(e)}")

if __name__ == "__main__":
    main()