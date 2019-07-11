# coding=utf-8
# import re
# import os
import threading
from queue import Queue
import requests
# from urllib import request
from lxml import etree
import csv
# csv.writer


class Producer(threading.Thread):
    def __init__(self, page_queue, txt_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.txt_queue = txt_queue
        self.link_url = "http://www.budejie.com"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

    def run(self):
        while True:
            if self.page_queue.empty():
                print("P-------完成测试！")
                break
            url = self.page_queue.get()
            # print(url)
            self.parse_url(url)

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        txts = html.xpath("//div[@class='j-r-list-c-desc']")
        for txt in txts:
            descs = txt.xpath(".//text()")
            # print(descs)
            desc = '\n'.join(descs).strip()
            # print(desc)
            prefix = 'href='
            link = prefix + self.link_url + txt.xpath(".//a/@href")[0]
            # print(link)
            test = '        '
            self.txt_queue.put((desc, test, link))
            # print(self.txt_queue.get())
        # url.split('/')[-1] 取出url中以/为区分的最后一个了元素
        print('='*30 + "第%s页下载完成！"%url.split('/')[-1] + "="*30)

class Consumer(threading.Thread):
    def __init__(self, txt_queue, writer, gLock, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.txt_queue = txt_queue
        self.writer = writer
        self.lock = gLock

    def run(self):
        while True:
            try:
                txt_info = self.txt_queue.get(timeout=4)
                # print(txt_info)
                desc, test, link = txt_info
                # print(desc)
                # print(link)
                self.lock.acquire()
                self.writer.writerow((desc, test, link))
                self.lock.release()
                print("一条保存成功！")
            except:
                break


def main():
    page_queue = Queue(150)
    txt_queue = Queue(1000)
    gLock = threading.Lock()
    fp = open("/home/jason/文档/multiprocess_spider/test_file/duanzi_bsbdj.cvs", 'a', newline='\r\n', encoding='utf-8')
    writers = csv.writer(fp)
    # writers.writer('\n')
    # writers.writerow
    writers.writerow(('content', 'link'))

    for i in range(1, 2):
        url = 'http://www.budejie.com/text/%d' % i
        page_queue.put(url)

    for x in range(15):
        p = Producer(page_queue, txt_queue)
        p.start()

    for y in range(15):
        c = Consumer(txt_queue, writers, gLock)
        c.start()



if __name__ == '__main__':
    main()