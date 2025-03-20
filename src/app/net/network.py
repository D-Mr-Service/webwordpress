import socket

def is_connected(host="8.8.8.8", port=53, timeout=3):
    """
    检测网络是否可用。

    参数:
    - host: 默认使用 Google 的 DNS 服务器 IP 8.8.8.8
    - port: 默认端口 53
    - timeout: 连接超时时间（秒）

    返回:
    - True: 检测到网络连接
    - False: 未检测到网络连接
    """
    try:
        # 设置连接超时时间
        socket.setdefaulttimeout(timeout)
        # 创建一个 socket 对象，并尝试连接
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        return True
    except OSError:
        return False


