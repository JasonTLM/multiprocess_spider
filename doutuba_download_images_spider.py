# coding=utf-8
import requests
from lxml import etree
from urllib import request
import os
import re


def parse_page(url):
    headers= {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    # print(response.text)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//"
                      "img[@class!='gif']")
    # print(imgs)
    for img in imgs:
        # print(etree.tostring(img))
        img_url = img.get('data-original')
        # print(img_url)
        alt = img.get('alt')
        # print(alt)
        alt_name = re.sub(r'[?？.，。！!*]', '', alt)
        # print(alt_name)
        suffix = os.path.splitext(img_url)[1]
        # print(suffix)
        filename = alt_name + suffix
        # print(filename)
        # request.urlretrieve(headers=headers)
        opener = request.build_opener()
        # request.build_opener()
        """Create an opener object from a list of handlers.

        The opener will use several default handlers, including support
        for HTTP, FTP and when applicable HTTPS.

        If any of the handlers passed as arguments are subclasses of the
        default handlers, the default handlers will not be used.
        """
        # addheaders 只能传入
        opener.addheaders=[
            ('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')
        ]
        # opener.addheaders = {
        #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        # }
        request.install_opener(opener)
        request.urlretrieve(url= img_url,
                            filename = '/home/jason/文档/multiprocess_spider/images/' + filename)
        print(filename + '       下载成功！')
    # for img in imgs:
    #     img_url = img.get('data-original')
    #     alt = img.get('alt')
    #     alt = re.sub(r'[\?？\.,。！!]', '', alt)
    #     suffix = os.path.splitext(img_url)[1]
    #     filename = alt + suffix
    #     request.urlretrieve(img_url, '/home/jason/文档/multiprocess_spider/images' + filename)

# """
# opener=urllib.request.build_opener()
# opener.addheaders=[(‘User-Agent’,‘Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36’)]
# urllib.request.install_opener(opener)
# urllib.request.urlretrieve(url, Path)
# """

def main():
    for i in range(1, 11):
        url = "http://www.doutula.com/photo/list/?page=%d" % i
        parse_page(url)



if __name__ == '__main__':
    main()