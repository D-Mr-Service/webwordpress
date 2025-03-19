from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from  ..logs.log import setup_logger
logger = setup_logger()
def page_title_action(driver):



    try:
        # 查找目标的 <a> 标签
        add_link = driver.find_element(By.CSS_SELECTOR, 'a.page-title-action')

        # 判断是否找到了该链接
        if add_link:
            logger.debug("找到了 '添加新网址' 链接，正在点击...")

            # 点击该链接
            add_link.click()

            # 等待页面跳转或者加载完成
            # time.sleep(3)

            # 判断页面是否成功跳转，检测新的 URL 或者某些页面元素是否存在
            if driver.current_url == 'https://d-mr.cn/wp-admin/post-new.php?post_type=sites':  # 替换为目标页面 URL
                logger.debug("点击成功，页面跳转成功！")
                # print()
            else:
                logger.debug("页面没有跳转，可能是点击失败。")

    except Exception as e:
        logger.debug(f"发生错误: {e}")



