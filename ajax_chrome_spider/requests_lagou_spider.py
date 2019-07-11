# coding=utf-8

import requests
from lxml import etree
import time
import re


headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '25',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'user_trace_token=20190706113016-50754af6-c677-4cce-9807-4c4da378afaa; _ga=GA1.2.83245996.1562383818; LGSID=20190706113017-6014238e-9f9e-11e9-bd39-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0QW9b0FNkUsjZ7iKI00000cTH27C00000TyeGaC.THL0oUhY1x60UWdBmy-bIfK15yDYPvNBrHPWnj0snyf1myD0IHdAfHRsP1K7nYwKnjTvrjuArRRLPDuDP1uArH0swHNKfsK95gTqFhdWpyfqn1cYn1DkPj04rausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4_myIEIi4WUvYEUA78uA-8uzdsmyI-QLKWQLP-mgFWpa4CIAd_5LNYUNq1ULNzmvRqUNqWu-qWTZwxmh7GuZNxTAPBI0KWThnqn1cLPWf%26tpl%3Dtpl_11534_19968_16032%26l%3D1512575879%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3243114098_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D120%26ie%3Dutf-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26oq%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rqlang%3Dcn; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; LGUID=20190706113017-601425d2-9f9e-11e9-bd39-525400f775ce; JSESSIONID=ABAAABAABEEAAJAD25AFD4773FA15FFFDB3D4EC0E630528; _gid=GA1.2.2759990.1562383820; index_location_city=%E6%B7%B1%E5%9C%B3; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1562383819,1562384746; X_HTTP_TOKEN=0a2e979caf493ad63574832651c5caeb8f6d7fcde7; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1562384754; LGRID=20190706114553-8e125e95-9fa0-11e9-bd39-525400f775ce; TG-TRACK-CODE=index_search; SEARCH_ID=7978bbdba9e64a7993087bd1c9256f0a',
        'DNT': '1',
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    }


def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'

    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
    # response = requests.post(url, headers=headers, data=data)
    # print(response.json())

    for x in range(1, 2):
        data['pn'] = x
        response = requests.post(url, headers=headers, data=data)
        print(response.json())
        positions = response.json()["content"]["positionResult"]["result"]
        for position in positions:
            position_url = "https://www.lagou.com/jobs/%s.html" % position['positionId']
            print(position_url)
            # break
            position_resp = requests.get(position_url, headers=headers)
            parse_position(position_resp.text)
            time.sleep(1)


def parse_position(source):
    html = etree.HTML(source)
    try:
        title = html.xpath("//span[@class='name']/text()")[0]
        company = html.xpath("//h2[@class='fl']/text()")[0].strip()
        job_request_span = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_span[0].xpath(".//text()")[0]
        salary = salary.strip()
        city = job_request_span[1].xpath(".//text()")[0]
        city = re.sub(r"[/\s]", "", city)
        work_years = job_request_span[2].xpath(".//text()")[0]
        work_years = re.sub(r"[/\s]", "", work_years)
        education = job_request_span[3].xpath(".//text()")[0]
        education = re.sub(r"[/\s]", "", education)
        company_website = html.xpath("//ul[@class='c_feature']/li[last()]/a/@href")[0]
        position_desc = "".join(html.xpath("//dd[@class='job_bt']/div//text()"))
        position = {
            'title': title,
            'city': city,
            'salary': salary,
            'company': company,
            'company_website': company_website,
            'education': education,
            'work_years': work_years,
            'desc': position_desc,
        }
        print(position)
    except:
        print(source)

    print('=' * 40)


def main():
    request_list_page()



if __name__ == '__main__':
    main()

