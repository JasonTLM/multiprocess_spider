# coding=utf-8
from selenium import webdriver
import time

driver_path = r"/home/jason/chromedriver/chromedriver"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")
time.sleep(3)

# 调用driver.close()只关闭当前一个页面，不关闭其他页面
driver.close()
# 调用driver.quit()关闭整个浏览器，即为关闭所有页面
# driver.quit()



