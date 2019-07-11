# coding=utf-8
from selenium import webdriver

driver_path = r"/home/jason/chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')
print(driver.page_source)
