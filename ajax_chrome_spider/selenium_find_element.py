# coding=utf-8
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By

from time import sleep


driver_path = r"/home/jason/chromediver/chromedriver"

driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")

# driver.page_source 查看源代码
print(driver.page_source)
# html = etree.HTML(driver.page_source)
# print(etree.tostring(html, encoding='utf-8').decode('utf-8'))

# driver.quit()
# inputTag = driver.find_element_by_id('kw')
# inputTag.send_keys('pycharm')

# inputTag = driver.find_element_by_name('wd')
# inputTag.send_keys('谍影重重')

# inputTag = driver.find_elements(By.CSS_SELECTOR, '.bg>'
#                                                  'input')[0]
# inputTag.send_keys('我爱罗')

inputTag = driver.find_element_by_class_name('s_ipt')
inputTag.send_keys('死神')

sleep(40)
driver.quit()