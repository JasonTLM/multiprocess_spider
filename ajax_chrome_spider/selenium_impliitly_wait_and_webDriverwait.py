# coding=utf-8

from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




driver_path = r"/home/jason/chromediver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.douban.com')
driver.get('https://www.baidu.com/')

# # 隐式等待
# driver.implicitly_wait(8)
# driver.find_element_by_name('hdjashdsjadjsakld')


# # 显示等待， 注意presence_of_element_located()方法传入为元组或者列表
# element = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.ID, 'sdsdsdsddsa')),
#     EC.presence_of_element_located((By.ID, 'form_email'))
# )
# print(element)

# 显示等待成功的案例

element = WebDriverWait(driver, 8).until(
    EC.presence_of_element_located((By.NAME, 'wd'))
)

print(element)

print("Test-----Test")

sleep(10)
driver.quit()