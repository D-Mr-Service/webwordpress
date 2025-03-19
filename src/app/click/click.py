from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_element_by_partial_id(driver,seotitle,seokeywords,seodescription):
    try:
        # 显式等待并点击「网址」选项卡按钮
        tab_button = WebDriverWait(driver, 2000).until(
            EC.element_to_be_clickable((By.ID, "tabs-0-edit-post/document"))
        )
        tab_button.click()

        # 显式等待输入框加载（使用NAME定位）
        input_field_title = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "post-seo_post_meta[_seo_title]"))
        )

        # 输入文字
        input_field_title.send_keys(seotitle)


        input_field_key = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "post-seo_post_meta[_seo_metakey]"))
        )

        # 输入文字
        input_field_key.send_keys(seokeywords)


        input_field_desc = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "post-seo_post_meta[_seo_desc]"))
        )

        # 输入文字
        input_field_desc.send_keys(seodescription)

        # 可选：添加提交操作（如果需要）
        # driver.find_element(By.TAG_NAME, 'form').submit()

    finally:
        # 保持浏览器打开用于调试，实际使用时可能需要关闭
        # driver.quit()
        pass