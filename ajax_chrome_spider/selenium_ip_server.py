# coding=utf-8
from selenium import webdriver
from time import sleep

driver_path = r"/home/jason/chromedriver/chromedriver"
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://218.75.69.50:53078")

driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
driver.get("http://httpbin.org/ip")




sleep(10)
driver.quit()