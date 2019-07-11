# coding=utf-8
from selenium import webdriver
import csv
from time import sleep
import pytesseract
from PIL import Image
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from lxml import etree
from urllib import request


class Boss_soider(object):
    driver_path = '/home/jason/chromedriver/chromedriver'
    def __init__(self):
        # 初始化driver, 并指定chromedriver的路径
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        self.url = 'https://www.zhipin.com/job_detail/?query=python&city=101280600&industry=&position='
        self.domain = "https://www.zhipin.com"
        fp = open('boss_file.csv', 'a', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(fp, ['name', 'company_name', 'salary', 'city', 'work_years',
                                          'education', 'desc'])
        self.writer.writeheader()

    def run(self):
        self.driver.get(self.url)
        while True:
            if len(self.driver.find_element_by_id('captcha')) > 0:
                self.fill_captcha()
                sleep(2)
                continue
            source = self.driver.page_source
            self.parse_list_page(source)
            next_btn = self.driver.find_element_by_xpath("")


    def fill_captcha(self):
        captchaInput = self.driver.find_element_by_id("captcha")
        captchaImg = self.driver.find_element_by_class_name("code")
        submitBtn = self.driver.find_element_by_class_name("btn")
        src = captchaImg.get_attribute("src")
        request.urlretrieve(self.domain + src, '/home/jason/文档/multiprocess_spider/pytesseract_images/captcha.png')
        image = Image.open("/home/jason/文档/multiprocess_spider/pytesseract_images/captcha.png")
        text = pytesseract.image_to_string(image)
        captcha = re.sub(r"[\s/]", "", text)
        captchaInput.send_keys(captcha)
        submitBtn.click()


    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("//h3[@class='name']/a/@href")
        for link in links:
            self.request_detail_page(self.domain + link)
            sleep(1)


    def request_detail_page(self, url):
        self.driver.execute_script("window.open('%s')" % url)
        self.driver.switch_to_window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        name = html.xpath("//div[@class='name']/h1/text()")[0]
        salary = html.xpath("//div[@class='name']/span[@class='salary']/text()")[0]
        infos = html.xpath("//div[@class='job-banner']//div[@class='info-primary']/p//text()")
        city = infos[0]
        work_years = infos[1]
        educations = infos[2]
        company_name = html.xpath("//div[@class='company-info']/a[last()]/@title")[0].strip()
        descs = html.xpath("//div[@class='detail-content']//div[@class='text']/text()")
        desc = "\n".join(descs).strip()
        position = {
            'name': name,
            'company_name': company_name,
            'salary': salary,
            'city': city,
            'work_years': work_years,
            'education': educations,
            'desc': desc
        }
        self.write_position(position)

    def write_position(self, position):
        self.writer.writerows(position)
        print(position)


if __name__ == '__main__':
    spider = Boss_soider()
    spider.run()


