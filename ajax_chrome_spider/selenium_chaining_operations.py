# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


driver_path = r"/home/jason/chromediver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com/")
"""
先使用find_element_by_id指定位置，分别赋值给inputTag、 submitBtn
再将diver传入ActionChains()方法中，赋值为actions（此可理解为鼠标）
使用move_to_element()方法
"""
inputTag = driver.find_element_by_id('kw')
submitBtn = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag, 'PyCharm')
actions.move_to_element(submitBtn)
actions.click(submitBtn)
actions.perform()


sleep(10)
driver.quit()