# coding=utf-8

from selenium import webdriver
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
import re
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class LagouSpider(object):
    # chromedriver的绝对路径
    driver_path = r'/home/jason/chromedriver/chromedriver'
    def __init__(self):
        # 初始化一个driver， 并指定chromedriver的路径
        self.driver = webdriver.Chrome(executable_path=self.driver_path)
        # self.positions = list()
        # self.fp = open('lagou.csv', 'a', encoding='utf-8', newline='')
        # self.writer = csv.DictWriter(self.fp, ['title', 'salary', 'city', 'work_year',
        #                                        'education', 'company_website', 'desc',
        #                                        'acquire', 'origin_url', 'job_category'])
        # self.writer.writeheader()

    def run(self):
        url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.driver.get(url)
        while True:
            WebDriverWait(driver=self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'pager_next')]")))
            resource = self.driver.page_source
            self.parse_list_page(resource)
            next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
            if "pager_next_disabled" in next_btn.get_attribute('class'):
                break
            next_btn.click()
            time.sleep(2)


    def parse_list_page(self, resource):
        html = etree.HTML(resource)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.parse_detail_page(link)
            time.sleep(1)

    def parse_detail_page(self, url):
        self.driver.execute_script("window.open('"+url+"')")
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(2)
        WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//dd[@class='job_bt']")))
        resource = self.driver.page_source
        html = etree.HTML(resource)
        title = html.xpath("//h2[@class='name']/text()")[0]
        company = html.xpath("//em[@class='fl-cn']/text()")[0].strip()
        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_spans[0].xpath('.//text()')[0].strip()
        city_name = job_request_spans[1].xpath(".//text()")[0]
        city = re.sub(r"[/\s]", "", city_name)
        work = job_request_spans[2].xpath(".//text()")[0]
        work_years = re.sub(r"[/\s]", "", work)
        educations = job_request_spans[3].xpath(".//text()")[0]
        education = re.sub(r"[/\s]", "", educations)
        job_category = job_request_spans[4].xpath(".//text()")[0]
        company_website = html.xpath("//h4[@class='c_feature_name']/text()")[0]
        position_text = "".join(html.xpath("//dd[@class='job_bt']/div//text()")).strip()
        position_desc = re.sub(r"[/\s]", "", position_text)
        position = {
            'title': title,
            'city': city,
            'salary': salary,
            'company': company,
            'company_website': company_website,
            'education': education,
            'work_years': work_years,
            'desc': position_desc,
            'origin_url': url,
            'job_category': job_category
        }
        position_text = [
            (title, city, salary, company, company_website, education, work_years, position_desc, url, job_category)
        ]
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])
        time.sleep(0.5)
        print(position)
        # self.writer_position(position)
        self.save_file(position_text)

    # def writer_position(self, position):
    #     # self.positions.append(position)
    #     if len(self.positions) >= 100:
    #         self.writer.writerows(self.positions)
    #         self.positions.clear()
    #     self.positions.append(position)
    #     print(position)

    def save_file(self, position_text):
        with open ('/home/jason/文档/multiprocess_spider/ajax_chrome_spider/lagou.csv','a',newline='') as fp:
            # self.writer.writeheader()
            writer = csv.writer(fp)
            # n = 1
            # n = 1
            # while True:
            #     writer.writerow(sheaders)
            #     False
            # writer.writeheader(sheaders)
            writer.writerows(position_text)
            writer.writerows('\n')


def main():
    spider = LagouSpider()
    spider.run()


if __name__ == '__main__':
    main()
