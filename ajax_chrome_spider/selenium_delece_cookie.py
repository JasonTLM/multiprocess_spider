# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


driver_path = r"/home/jason/chromediver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")

for cookie in driver.get_cookies():
    print(cookie)

print('<'*30 + '>'*30)

print(driver.get_cookie(name='BD_UPN'))


print('<'*30 + '>'*30)
driver.delete_cookie(name='BDORZ')

driver.delete_all_cookies()






time.sleep(20)
driver.quit()