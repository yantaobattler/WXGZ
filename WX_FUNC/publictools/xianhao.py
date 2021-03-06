# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

# head 信息
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Connection': 'keep-alive'}


def excute():
    rsp_dict = {}
    response = requests.get('https://xianxing.911cha.com', headers=head)
    soup = BeautifulSoup(response.text, 'lxml')

# 开始拆

    # 其他城市
    for i in range(3, 10):
        temp3 = soup.find_all("div", class_="mcon")[i]
        city = temp3.find("h3", class_="f16").text[:-6]  # 城市名

        temp4 = temp3.find_all("td", width="25%")

        txt = ''
        for j in temp4:
            txt = txt + j.text + '\n'

        txt = txt + temp3.find("div", class_="f14").text

        rsp_dict[city] = txt

    # 主城，大概可能是按照ip搞得,服务器是北京，本地跑是天津
    temp1 = soup.find_all("div", class_="mcon")[0]
    city = temp1.find("h2", class_="f16").text[:-6]
    temp2 = temp1.find_all("td", width="25%")

    txt = ''
    for i in temp2:
        txt = txt + i.text + '\n'

    txt = txt + temp1.find("div", class_="f14").text
    rsp_dict[city] = txt

    # 因为这个网站天津的限号规则不更新了，天津的规则=北京，所以改取北京的规则
    beijing_rsp = rsp_dict['北京']
    tianjin_rsp = rsp_dict['天津']
    tail = tianjin_rsp.split('\n')[4]
    tianjin_rsp = '\n'.join(beijing_rsp.split('\n')[0:4]) + '\n' + tail
    rsp_dict['天津'] = tianjin_rsp

    return rsp_dict


if __name__ == '__main__':
    print(excute())