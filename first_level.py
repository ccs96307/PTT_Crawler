# -*- coding: utf-8 -*-
import requests
import time


# preset
Board_list = ['JinYong']
headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}


def get_the_newest_index_web_content(board):
    r_newest = requests.get("https://www.ptt.cc/bbs/" + board + "/index.html", headers=headers)

    while True:
        if r_newest.status_code == requests.codes.ok:
            print('ok')
        else:
            print('something error!')
        open(board + "_HTML/test.txt", 'w', encoding='utf-8').write(r_newest.text)
        break


def get_all_HTML_first_level(board):
    s = 0
    f = 0
    fail_record = []

    for index in range(1, 695):
        time.sleep(3)
        r = requests.get('https://www.ptt.cc/bbs/' + board + '/index' + str(index) + '.html', headers=headers)

        if r.status_code == requests.codes.ok:
            print('第 %d 頁網頁原始碼提取成功' % index)
            s += 1
        else:
            print('第 %d 頁網頁原始碼提取失敗！！！' % index)
            f += 1
            fail_record.append(index)
            continue

    print('成功提取數： ', s)
    print('失敗提取數： ', f)
    print('失敗頁面： ', fail_record)


if __name__ == '__main__':
    for board in Board_list:
        get_all_HTML_first_level(board)
