import os
import requests
import urllib3
from urllib.parse import urlparse
from src.app import setup_logger

logger = setup_logger()
# 禁用SSL警告（生产环境请配置有效证书）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def validate_url(url):
    """验证URL格式有效性"""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def check_accessibility(url):
    """检测URL可达性"""
    if not validate_url(url):
        return False

    try:
        response = requests.get(
            url,
            timeout=15,
            verify=False,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'},
            allow_redirects=True
        )
        return response.ok  # 自动处理2xx/3xx状态码
    except Exception as e:
        logger.info(f"检测失败 [{url}]：{str(e)[:100]}")
        return False

def process_target_directory(target_dir):
    # 创建失效记录目录
    false_dir = os.path.join(target_dir, "false")
    os.makedirs(false_dir, exist_ok=True)

    # 定义记录文件绝对路径
    record_file = os.path.join(false_dir, "url.txt")
    record_abs = os.path.abspath(record_file)

    # 预创建记录文件（如果不存在）
    if not os.path.exists(record_file):
        open(record_file, 'w', encoding='utf-8').close()

    # 遍历目录文件
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)

        # 跳过非处理目标
        if not filename.endswith('.txt'):
            continue
        if os.path.isdir(file_path):
            continue
        if os.path.abspath(file_path) == record_abs:
            continue

        logger.info(f"\n正在清理文件: {filename}")

        # 读写处理
        with open(file_path, "r+", encoding='utf-8') as f:
            original_urls = [line.strip() for line in f if line.strip()]

            valid_urls = []
            invalid_urls = []

            for url in original_urls:
                if check_accessibility(url):
                    valid_urls.append(url)
                else:
                    invalid_urls.append(url)

            # 更新当前文件
            f.seek(0)
            f.truncate()
            f.write("\n".join(valid_urls))

            # 记录失效链接
            if invalid_urls:
                with open(record_file, "a", encoding='utf-8') as log:
                    log.write("\n".join(invalid_urls) + "\n")
                logger.info(f"清理完成：删除{len(invalid_urls)}个失效链接")

def Clean_up_RLs(target_folder):



    # 增强目录校验
    if not os.path.exists(target_folder):
        raise FileNotFoundError(f"目标目录不存在: {target_folder}")
    if not os.path.isdir(target_folder):
        raise NotADirectoryError(f"路径不是目录: {target_folder}")

    process_target_directory(target_folder)
    logger.info("\n操作完成！所有文本文件已清除不可访问链接")
    return True