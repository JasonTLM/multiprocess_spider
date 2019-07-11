# coding=utf-8
import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading


class Producer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

    def run(self):
        while True:
            if self.page_queue.empty():
                print("P---测试成功")
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url, headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']"
                          "//img[@class!='gif']")
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt_name = re.sub(r'[?？，。！*/.]', '', alt)
            # 获取后缀suffix,通过os.path.splitext()方法获取
            suffix = os.path.splitext(img_url)[1]
            filename = alt_name + suffix
            self.img_queue.put((img_url, filename))


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue
        self.headers = [
            ('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')
        ]

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                # print(self.img_queue)
                # print(self.page_queue)
                print("C----测试成功")
                break
            img_url, filename = self.img_queue.get()
            opener = request.build_opener()
            opener.addheaders = self.headers
            request.install_opener(opener)
            request.urlretrieve(url=img_url, filename='/home/jason/文档/multiprocess_spider/images/' + filename)
            print(filename + "                 下载成功！")
            # opener = request.build_opener()
            # # request.build_opener()
            # """Create an opener object from a list of handlers.
            #
            # The opener will use several default handlers, including support
            # for HTTP, FTP and when applicable HTTPS.
            #
            # If any of the handlers passed as arguments are subclasses of the
            # default handlers, the default handlers will not be used.
            # """
            # # addheaders 只能传入
            # opener.addheaders = [
            #     ('User-Agent',
            #      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')
            # ]
            # # opener.addheaders = {
            # #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
            # # }
            # request.install_opener(opener)
            # request.urlretrieve(url=img_url,
            #                     filename='/home/jason/文档/multiprocess_spider/images/' + filename)
            # print(filename + '       下载成功！')


def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for i in range(1, 101):
        url = "http://www.doutula.com/photo/list/?page=%d" % i
        page_queue.put(url)

    for x in range(10):
        p = Producer(page_queue, img_queue)
        p.start()

    for y in range(10):
        c = Consumer(page_queue, img_queue)
        c.start()


if __name__ == '__main__':
    main()