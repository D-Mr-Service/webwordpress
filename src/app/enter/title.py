import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from ..logs.log import setup_logger

logger = setup_logger()

def Article_title_input(driver, url, title,elements):
    while True:
        # 获取当前页面的 URL
        current_url = driver.current_url

        # 判断当前页面是否是目标页面
        if current_url != url:
            logger.debug(f"当前页面 {current_url} 不是目标页面 {url}, 等待 1 秒后重新检查...")
            time.sleep(1)  # 等待 1 秒再检查
            continue  # 继续检查
        else:
            logger.debug(f"已进入目标页面 {url}, 开始操作")
            break  # 目标页面，跳出循环

    # 页面是目标页面，继续操作
    wait = WebDriverWait(driver, 10)

    try:
        if elements == "//p[@contenteditable='true']":
            # 等待 p 元素加载，选择 contenteditable="true" 的 p 元素
            appender_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "block-editor-default-block-appender__content")))

        # 点击该元素
            appender_element.click()
            logger.debug(f"开始编辑内容")
            p_element = wait.until(EC.presence_of_element_located((By.XPATH, elements)))
            p_element.click()
            p_element.send_keys(title)
        # 等待 h1 元素加载并判断是否可编辑
        elif elements == "//h1[@contenteditable='true']":
            h1_element = wait.until(EC.presence_of_element_located((By.XPATH, elements)))
            # 点击该元素进行编辑
            h1_element.click()

            # 输入"标题"
            h1_element.send_keys(title)
            logger.debug("标题已输入")
        elif elements == "//input[@name='sites_post_meta[_sites_link]']":
            input_element = wait.until(EC.presence_of_element_located((By.XPATH, elements)))
            input_element.click()
            input_element.clear()  # 清空已有内容（如果需要）
            input_element.send_keys(title)
            logger.debug(f"网址输入框已输入: {title}")
        elif elements == "//textarea[@name='sites_post_meta[_sites_sescribe]']":
            textarea_element = wait.until(EC.presence_of_element_located((By.XPATH, elements)))
            textarea_element.click()
            textarea_element.clear()  # 清空已有内容（如果需要）
            textarea_element.send_keys(title)
            logger.debug(f"描述输入框已输入: {title}")
        elif elements == "//input[@name='sites_post_meta[_sites_language]']":
            text_element = wait.until(EC.presence_of_element_located((By.XPATH, elements)))
            text_element.click()
            text_element.clear()  # 清空已有内容（如果需要）
            text_element.send_keys(title)
            logger.debug(f"网址语言输入框已输入: {title}")
        elif elements == "//input[@name='sites_post_meta[_sites_country]']":
            text_element = wait.until(EC.presence_of_element_located((By.XPATH, elements)))
            text_element.click()
            text_element.clear()  # 清空已有内容（如果需要）
            text_element.send_keys(title)
            logger.debug(f"网址国家地区输入框已输入: {title}")
        elif elements == "//input[@name='post-seo_post_meta[_seo_title]']":
            text_element = wait.until(EC.presence_of_element_located((By.XPATH, elements)))
            text_element.click()
            text_element.clear()  # 清空已有内容（如果需要）
            text_element.send_keys(title)
            logger.debug(f"网址seo标题输入框已输入: {title}")
        elif elements == "//input[@name='post-seo_post_meta[_seo_metakey]']":
            text_element = wait.until(EC.presence_of_element_located((By.XPATH, elements)))
            text_element.click()
            text_element.clear()  # 清空已有内容（如果需要）
            text_element.send_keys(title)
            logger.debug(f"网址seo关键词输入框已输入: {title}")
        elif elements == "//textarea[@name='post-seo_post_meta[_seo_desc]']":
            text_element = wait.until(EC.presence_of_element_located((By.XPATH, elements)))
            text_element.click()
            text_element.clear()  # 清空已有内容（如果需要）
            text_element.send_keys(title)
            logger.debug(f"网址seo描述输入框已输入: {title}")
        elif elements == "//input[@name='sites_post_meta[_sites_preview]']":
            text_element = wait.until(EC.presence_of_element_located((By.XPATH, elements)))
            text_element.click()
            text_element.clear()  # 清空已有内容（如果需要）
            text_element.send_keys(title)
            logger.debug(f"网址首页截图url输入框已输入: {title}")
    except Exception as e:
        logger.debug("出现错误:", e)
