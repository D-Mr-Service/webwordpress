from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from src.app import setup_logger

logger = setup_logger()
def chebox(driver, target_labels=['AI工具', 'AI换脸', 'AI绘画']):
    """
    通过标签文本点击多个复选框
    :param driver: 已初始化的WebDriver实例
    :param target_labels: 要点击的复选框标签文本列表
    """
    for label in target_labels:
        try:
            # 构造动态XPath定位器
            xpath = f"//label[normalize-space()='{label}']"

            # 显式等待元素可点击（最多10秒）
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )

            # 滚动到元素可见位置
            driver.execute_script("arguments[0].scrollIntoViewIfNeeded(true);", element)

            # 执行点击操作
            element.click()
            logger.info(f"✅ 成功点击 [{label}]")


        except TimeoutException:
            logger.debug(f"❌ 找不到 [{label}] 对应的复选框")

            continue

