from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app import check_and_close_browser,page_title_action,Article_title_input,je,setup_logger,click_element_by_partial_id,chebox,ipwebcountry,get_website_title
from app.language.languageweb import urlsweb
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
def websdata(content,websurl,MaintexSeoTdeoDescription,seotitle,seokeywords,seodescription,Classification,name):
    # 获取 'my_logger' 记录器
    logger = setup_logger()


    # 打开并读取 config.json 文件
    with open('./config.json', 'r') as file:
        config = json.load(file)
    # 访问里面的参数
    web = config["web"]
    # 打开目标页面
    NewWeb = config["NewWeb"]
    NewUrl = config["newurl"]
    cookies = config["cookies"]


# 创建 ChromeOptions 对象
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # 启用无头模式
#     chrome_options.add_argument("--disable-gpu")  # 解决某些系统下的兼容性问题
#     chrome_options.add_argument("--no-sandbox")  # 适用于 Linux，避免权限问题
#     chrome_options.add_argument("--disable-dev-shm-usage")  # 适用于 Linux，防止资源不足
    # chrome_options.add_argument("--window-size=1920x1080")  # 设置窗口大小，避免某些网页响应式调整
# ,options=chrome_options
    # 设置 Chrome 浏览器驱动
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    driver.get(web+NewWeb)
    # 将 cookies 添加到浏览器中
    for name, value in cookies.items():
        driver.add_cookie({"name": name, "value": value})
    # 重新加载页面以使 cookies 生效
    driver.get(web+NewWeb)
    try:
        title = driver.title  # 获取网页标题
        logger.info(f"浏览器已经启动")

    except Exception as e:
        logger.debug(f"浏览器启动失败或者cookies失效:", e)















    #================
    # 判断网页编辑器是否展示
    je(driver,web+NewUrl)
    #逻辑判断 点开网址编辑器
    page_title_action(driver)
    #输入标题





    # chebox(driver)
    Article_title_input(driver, web+NewUrl,content,"//p[@contenteditable='true']")
    Article_title_input(driver, web+NewUrl, websurl, "//input[@name='sites_post_meta[_sites_link]']")
    Article_title_input(driver, web+NewUrl, MaintexSeoTdeoDescription, "//textarea[@name='sites_post_meta[_sites_sescribe]']")
    Article_title_input(driver, web+NewUrl, urlsweb(web), "//input[@name='sites_post_meta[_sites_language]']")
    Article_title_input(driver, web+NewUrl, ipwebcountry(web), "//input[@name='sites_post_meta[_sites_country]']")
    # Article_title_input(driver, web+NewUrl, "https://网址首页截图输入.png", "//input[@name='sites_post_meta[_sites_preview]']")

    # 调用方法打开页面并进行操作
    titles = get_website_title(websurl)
    result = titles if isinstance(titles, str) else name
    Article_title_input(driver, web+NewUrl,result,"//h1[@contenteditable='true']")
    click_element_by_partial_id(driver,seotitle,seokeywords,seodescription)

    chebox(driver, [Classification])









    # 点击第一个按钮（打开发布面板）
    first_button_selector = (
        "button.components-button.editor-post-publish-panel__toggle"
    )
    first_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, first_button_selector))
    )
    first_button.click()

    # 点击第二个按钮（确认发布）
    second_button_selector = (
        "button.components-button.editor-post-publish-button"
    )
    second_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, second_button_selector))
    )
    second_button.click()





    #================





    #关闭浏览器
    check_and_close_browser(driver)



    # 截图网址
    # target_urls = [
    #     'https://d-mr.cn',
    #     'https://www.baidu.com',
    # ]
    # capture_webpage_screenshot(file,target_urls)


    # 上传ftp
