import requests
from lxml import etree


def getRemoteHost(_url):
    url = 'https://' + _url + '.ipaddress.com/'
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59'
    }
    try:
        page_text = requests.get(url=url, headers=headers).text
        # print(page_text)
        tree = etree.HTML(page_text)
        li_list = tree.xpath('/html/body/div/main/section[1]/table/tr[6]/td/ul/li/text()')

        print(li_list[0])
        print('over')
        return li_list[0]
    except:
        return "该网站无法解析"

# s = getRemoteHost('google.com')
# print(s)
