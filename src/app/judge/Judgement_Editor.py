from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from  ..logs.log import setup_logger
logger = setup_logger()

def je(driver,newurl):
    # 查找包含特定 href 值的 <a> 标签
    try:
        element = driver.find_element(By.XPATH, '//a[@href='+newurl+']')
        if element:
            logger.debug(f"找到链接，继续执行下一步")
            # print("找到链接，继续执行下一步")
            # 这里可以继续你的下一步操作，比如点击这个链接
            element.click()
    except Exception as e:
        logger.debug(f"链接未找到，错误：{e}")



