# -*- coding: utf-8 -*-
import regex as re


# preset
clean_list = ['<.+>']


def clean_text_display():
    for n in range(13872, 13876):
        if n in [209, 4873, 4874, 10020, 10505]:
            continue

        text = open('D:/Google 雲端硬碟/Meeting/Meeting data/ChatBot/ChatBot/JinYong_Article/A%s.txt' % str(n), 'r', encoding='utf-8').read()

        title = re.findall('<title>.+ - 看板 JinYong - 批', text)[0]
        title = re.sub('<title>', '', title)
        title = re.sub(' - 看板 JinYong - 批', '', title)
        print(title)
        print('===============================================')

        text = re.sub('\n', '\b', text)
        content = re.findall('<div id="main-container">.+※ 發信站: 批踢踢實業坊', text)[0]
        content = re.sub('\b', '\n', content)

        for _ in clean_list:
            content = re.sub(_, '', content)

        print(content)
        print('===============================================')

        text = re.sub('\b', '\n', text)
        push = re.findall('<div class="push">.+class="push-ipdatetime">', text)

        for p in push:
            p = re.sub('<div class="push"><span class="f1 hl push-tag">', '', p)
            p = re.sub('<div class="push"><span class="hl push-tag">', '', p)
            p = re.sub('</span><span class="f3 hl push-userid">', '', p)
            p = re.sub('</span><span class="f3 push-content">', '', p)
            p = re.sub('</span><span class="push-ipdatetime">', '', p)
            print(p)

        break


def clean_text_save():
    s = 0
    f = 0
    error_text = []

    for n in range(1, 13876):
        try:
            if n in [209, 4873, 4874, 10020, 10505]:
                continue

            save_content = ''
            text = open('D:/Google 雲端硬碟/Meeting/Meeting data/ChatBot/ChatBot/JinYong_Article/A%s.txt' % str(n), 'r', encoding='utf-8').read()

            title = re.findall('<title>.+ - 看板 JinYong - 批', text)[0]
            title = re.sub('<title>', '', title)
            title = re.sub(' - 看板 JinYong - 批', '', title)
            save_content += title
            save_content += '\n'
            save_content += '==============================================='
            save_content += '\n'

            text = re.sub('\n', '\b', text)
            content = re.findall('<div id="main-container">.+※ 發信站: 批踢踢實業坊', text)[0]
            content = re.sub('\b', '\n', content)

            for _ in clean_list:
                content = re.sub(_, '', content)

            save_content += content
            save_content +='\n'
            save_content += '==============================================='
            save_content += '\n'

            text = re.sub('\b', '\n', text)
            push = re.findall('<div class="push">.+class="push-ipdatetime">', text)

            for p in push:
                p = re.sub('<div class="push"><span class="f1 hl push-tag">', '', p)
                p = re.sub('<div class="push"><span class="hl push-tag">', '', p)
                p = re.sub('</span><span class="f3 hl push-userid">', '', p)
                p = re.sub('</span><span class="f3 push-content">', '', p)
                p = re.sub('</span><span class="push-ipdatetime">', '', p)
                save_content += p
                save_content += '\n'

            open('JinYong/a%s.txt' % str(n), 'w', encoding='utf-8').write(save_content)
            s += 1
            print('第%d篇文章處理成功' % n)
        except:
            f += 1
            error_text.append(n)
            print('第%d篇文章處理失敗！！！' % n)

    print('成功：', s)
    print('失敗：', f)
    print('失敗文章: ', error_text)


def speed_test():
    import os

    text_list = set(os.listdir('JinYong/'))

    for text in text_list:
        content = open('JinYong/%s' % text, 'r', encoding='utf-8').read()
        if '張無忌' in content:
            print(text)


if __name__ == '__main__':
    speed_test()
