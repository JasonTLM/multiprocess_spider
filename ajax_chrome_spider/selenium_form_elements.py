# coding=utf-8
"""
常见的表单元素： input type='text/password/email/number'
            : button、input='submit'
            : checkbox: input='checkbox'
            : select: 下拉列表
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver_path = r"/home/jason/chromediver/chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

# # 操作输入框
# driver.get("https://www.baidu.com")
# #
# inputTag = driver.find_element_by_id('kw')
# inputTag.send_keys('pycharm')
#
# # driver.get("https://www.baidu.com")
# submitTag = driver.find_element_by_id('su')
# submitTag.click()

# 操作checkbox（复选框）
# driver.get("https://www.douban.com/")
# rememberBtn = driver.find_element_by_name('remember')
# rememberBtn.click()

# 操作select标签(友情链接类）
driver.get('http://www.dobai.cn/')
selectBtn = Select(driver.find_element_by_name('jumpMen'))
selectBtn.select_by_index(1)
selectBtn.select_by_value("http://m.95xiu.com/")
selectBtn.select_by_visible_text("95秀客户端")








sleep(20)
driver.quit()