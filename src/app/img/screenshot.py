#
# from playwright.async_api import async_playwright
# import asyncio
# import os
# import sys
# from urllib.parse import urlparse
# import re
# import subprocess
#
#
# def capture_webpage_screenshot(SAVE_DIR, target_urls):
#     def install_playwright():
#         print("正在初始化浏览器环境...")
#         env = os.environ.copy()
#         env["PLAYWRIGHT_DOWNLOAD_HOST"] = "https://npmmirror.com/mirrors/playwright"
#
#         try:
#             subprocess.run(
#                 [sys.executable, "-m", "pip", "install", "--upgrade", "playwright"],
#                 check=True,
#                 env=env
#             )
#             subprocess.run(
#                 [sys.executable, "-m", "playwright", "install", "chromium", "--force"],
#                 check=True,
#                 env=env
#             )
#             print("浏览器组件安装成功")
#         except subprocess.CalledProcessError as e:
#             print(f"安装失败，请手动执行：")
#             print("set PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/mirrors/playwright")
#             print("python -m playwright install chromium --force")
#             sys.exit(1)
#     install_playwright()
#
#     # 配置参数
#     TIMEOUT = 60000  # 延长至60秒
#     CONCURRENT_LIMIT = 3  # 降低并发数提高稳定性
#     RETRY_TIMES = 2  # 失败重试次数
#     USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#     VIEWPORT = {'width': 1920, 'height': 1080}  # 固定视口尺寸
#
#     def sanitize_filename(filename):
#         return re.sub(r'[\\/*?:"<>|]', '_', filename)
#
#     def generate_filename(url):
#         parsed = urlparse(url)
#         domain = parsed.netloc.replace('www.', '').split(':')[0]
#         path = parsed.path.replace('/', '_')[:50]
#         return sanitize_filename(f"{domain}{path}.png")
#
#     async def capture_single_page(url, save_path):
#         """改进后的截图函数"""
#         async with async_playwright() as p:
#             for attempt in range(RETRY_TIMES + 1):
#                 try:
#                     browser = await p.chromium.launch(
#                         headless=True,
#                         args=[
#                             '--disable-dev-shm-usage',
#                             '--no-sandbox',
#                             f'--user-agent={USER_AGENT}'
#                         ]
#                     )
#                     context = await browser.new_context(
#                         user_agent=USER_AGENT,
#                         viewport=VIEWPORT,  # 使用固定视口
#                         java_script_enabled=True,
#                         device_scale_factor=1  # 禁用缩放
#                     )
#                     page = await context.new_page()
#
#                     # 智能等待策略
#                     await page.goto(url, wait_until='networkidle', timeout=TIMEOUT)
#
#                     # 等待关键元素（可选）
#                     await page.wait_for_load_state('networkidle')
#                     await page.wait_for_timeout(1000)  # 额外等待1秒
#
#                     # 视口截图配置
#                     screenshot_args = {
#                         'path': save_path,
#                         'full_page': False,  # 关键修改：关闭全屏截图
#                         'animations': 'disabled',
#                         'clip': {
#                             'x': 0,
#                             'y': 0,
#                             'width': VIEWPORT['width'],
#                             'height': await page.evaluate('document.documentElement.clientHeight')
#                         }
#                     }
#
#                     await page.screenshot(**screenshot_args)
#                     await browser.close()
#                     return True
#                 except Exception as e:
#                     print(f"第{attempt+1}次尝试失败 {url}: {str(e)}")
#                     if attempt == RETRY_TIMES:
#                         return False
#                     await asyncio.sleep(2 ** attempt)
#
#     async def screenshot_worker(queue):
#         while True:
#             url = await queue.get()
#             if url is None:
#                 break
#
#             filename = generate_filename(url)
#             save_path = os.path.join(SAVE_DIR, filename)
#
#             print(f"正在处理: {url}")
#             success = await capture_single_page(url, save_path)
#
#             if success:
#                 print(f"成功保存: {save_path}")
#             else:
#                 print(f"最终失败: {url}")
#
#             queue.task_done()
#
#     async def main(urls):
#         os.makedirs(SAVE_DIR, exist_ok=True)
#         queue = asyncio.Queue()
#
#         for url in urls:
#             await queue.put(url)
#
#         workers = [
#             asyncio.create_task(screenshot_worker(queue))
#             for _ in range(CONCURRENT_LIMIT)
#         ]
#
#         await queue.join()
#
#         for _ in range(CONCURRENT_LIMIT):
#             await queue.put(None)
#
#         await asyncio.gather(*workers)
#
#     asyncio.run(main(target_urls))