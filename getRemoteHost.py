import pdb

import requests
from lxml import etree


def getRemoteHost(_url):
    # 原版的URL
    #url = 'https://' + _url + '.ipaddress.com/'
    # 新版的URL更改了
    url = 'https://ipaddress.com/website/' + _url
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59'
    }
    try:
        page_text = requests.get(url=url, headers=headers).text
        # print(page_text)
        tree = etree.HTML(page_text)
        # 获取XPath路径
        li_list = tree.xpath('/html/body/div[1]/main/section[1]/table/tbody/tr[6]/td/ul/li/text()')
        return li_list[0]
    except:
        return "该网站无法解析"

s = getRemoteHost('github.com')
print(s)
