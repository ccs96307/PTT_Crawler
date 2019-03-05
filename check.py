from bs4 import BeautifulSoup
import requests
import re

payload = \
    {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
    }

url_first = 'https://www.ptt.cc/bbs/Gossiping/index.html'
over18 = 'https://www.ptt.cc/ask/over18'
i = 0


def get_web(url):
    rs = requests.session()
    res = rs.post(over18, verify=False, data=payload)  # 過未滿18歲的葉面
    res = rs.get(url, verify=False)  # get 八卦版的內容

    if res.status_code != 200:
        print("invalid url ", url)
    else:
        soup = BeautifulSoup(res.text)
        for entry in soup.select('.r-ent'):
            print(entry.select('.date')[0].text, entry.select('.author')[0].text, entry.select('.title')[0].text)

        #print(res.text)
        #regex = re.compile(r'上頁')

        match = re.findall(r'<a class="btn wide" href="(.*?)">&lsaquo; 上頁</a>', res.text)  # 找上一頁的連結 用相似來找 findall有既定格式來尋找
        print('上一頁連結:', match)  # 上一頁的連結
        return match  # 回傳match
#<a class="btn wide" href="/bbs/Gossiping/index38983.html">&lsaquo; 上頁</a>


for i in range(100):
    print(i)
    if i <= 0:
        #get_web(url_first)
        first = get_web(url_first)#first =  first match
        st = ''.join(first)#list to string
        url_new = 'https://www.ptt.cc' + st  # 新的網址
    else:
        #print(url_new)
        #get_web(url_new)
        tmp = get_web(url_new)
        st2 = ''.join(tmp)
        url_new = 'https://www.ptt.cc' + st2