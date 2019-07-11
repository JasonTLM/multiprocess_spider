# coding=utf-8
from selenium import webdriver
from time import sleep

driver_path = r'/home/jason/chromedriver/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

# driver.get('https://www.douban.com/')

# 使用execute_script("window.open('url')") 来打开新的窗口页面
driver.execute_script("window.open('https://douban.com/')")
# print(driver.window_handles[0])


# 使用switch_to_window(driver.window_handles[i]) 来切换进入打开窗口
driver.switch_to_window(window_name=driver.window_handles[1])
# for cookie in driver.get_cookies():
#     print(cookie)


# print(driver.page_source)
print(driver.current_url)






sleep(10)
driver.quit()
