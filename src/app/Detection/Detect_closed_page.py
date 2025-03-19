from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from  ..logs.log import setup_logger
logger = setup_logger()

def check_and_close_browser(driver):

    # 设置一个循环，每 2 秒检查一次
    try:
        while True:
            # 获取指定的 div 元素
            try:
                post_publish_div = driver.find_element(By.CSS_SELECTOR, "div.components-panel__body.post-publish-panel__postpublish-header.is-opened")
                # 检查 div 中的文本内容
                if "已被发布。" in post_publish_div.text:
                    logger.debug("页面已发布，关闭浏览器")

                    driver.quit()  # 关闭浏览器
                    break
            except:
                logger.debug("没有找到该元素，继续检测...")


            # 每 2 秒检测一次
            time.sleep(2)

    except KeyboardInterrupt:
        logger.debug("检测终止")
        driver.quit()  # 退出浏览器
