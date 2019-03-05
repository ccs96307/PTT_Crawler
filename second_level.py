# -*- coding: utf-8 -*-

import requests
import time
import regex as re

# preset
Board_list = ['JinYong']
headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


def get_all_HTML_second_level(board):
    total_num = 0
    url_list = []

    for board in Board_list:
        for n in range(1, 695):
            content = open(board + '_HTML/index' + str(n) + '.txt', 'r', encoding='utf-8').read()
            url_temp = re.findall('<a href=".+html', content)

            for url in url_temp:
                url = re.sub('<a href="', '', url)
                url = 'https://www.ptt.cc' + url
                url_list.append(url)

        s = 0
        f = 0
        fail_record = []
        get_times = 0

        for url in url_list:
            get_times += 1
            time.sleep(3)

            r = requests.get(url, headers=headers)

            if r.status_code == requests.codes.ok:
                print('第 %d 篇文章原始碼提取成功' % get_times)
                s += 1
                open(board + '_Article/A' + str(get_times) + '.txt', 'w', encoding='utf-8').write(r.text)
            else:
                print('第 %d 頁文章原始碼提取失敗' % get_times)
                f += 1
                fail_record.append(get_times)
                content

        print('成功提取數： ', s)
        print('失敗提取數： ', f)
        print('失敗頁面： ', fail_record)


if __name__ == '__main__':
    for board in Board_list:
        get_all_HTML_second_level(board)

