# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import logging


logger = logging.getLogger("django")
# head 信息
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Connection': 'keep-alive'}


def ssqbydateno(dateno):
    url = 'http://kaijiang.500.com/shtml/ssq/'+dateno+'.shtml'
    result_dict = {}
    try:
        response1 = requests.get(url, headers=head)
        soup1 = BeautifulSoup(response1.text, 'xml')

        datestr = soup1.find("span", class_="span_right").text.split(" ")[0][10:]
        result_dict['year'] = datestr[:4]  # 开奖年
        result_dict['month'] = datestr.split('Äê')[1].split('ÔÂ')[0]  # 开奖月
        result_dict['date'] = datestr.split('Äê')[1].split('ÔÂ')[1].split('ÈÕ')[0]  # 开奖日

        ball = soup1.find("table", width="100%", border="0", cellspacing="0", cellpadding="1")

        # 排序球
        result_dict['r1'] = ball.find_all("li", class_="ball_red")[0].text
        result_dict['r2'] = ball.find_all("li", class_="ball_red")[1].text
        result_dict['r3'] = ball.find_all("li", class_="ball_red")[2].text
        result_dict['r4'] = ball.find_all("li", class_="ball_red")[3].text
        result_dict['r5'] = ball.find_all("li", class_="ball_red")[4].text
        result_dict['r6'] = ball.find_all("li", class_="ball_red")[5].text
        result_dict['b1'] = ball.find_all("li", class_="ball_blue")[0].text

        # 开奖顺序
        result_dict['open'] = ball.find_all("td")[3].text.strip()

    except Exception as e:
        logger.exception(e)

    return result_dict


def ssqtotxt():
    # get url
    response = requests.get('http://kaijiang.500.com/ssq.shtml', headers=head)
    soup = BeautifulSoup(response.text, 'lxml')

    # 写标题
    txtName = "E:/shuangseqiu" + time.strftime("%Y%m%d", time.localtime()) + ".txt"
    headline = 'dateno,year,month,date,r1,r2,r3,r4,r5,r6,b1,open_r1,open_r2,open_r3,open_r4,open_r5,open_r6,open_b1\n'

    f = open(txtName, "w+")
    f.write(headline)
    f.close()

    urls = soup.find("div", class_="iSelectList").find_all("a")
    for i in urls:
        try:
            url = i.get('href')
            dateno = i.text  # 期数

            # 分期
            response1 = requests.get(url, headers=head)
            soup1 = BeautifulSoup(response1.text, 'xml')

            datestr = soup1.find("span", class_="span_right").text.split(" ")[0][10:]
            year = datestr[:4]  # 开奖年
            month = datestr.split('Äê')[1].split('ÔÂ')[0]   # 开奖月
            date = datestr.split('Äê')[1].split('ÔÂ')[1].split('ÈÕ')[0]  # 开奖日

            if len(month) == 1:
                month = '0' + month
            if len(date) == 1:
                date = '0' + date

            ball = soup1.find("table", width="100%", border="0", cellspacing="0", cellpadding="1")

            # 排序球
            r1 = ball.find_all("li", class_="ball_red")[0].text
            r2 = ball.find_all("li", class_="ball_red")[1].text
            r3 = ball.find_all("li", class_="ball_red")[2].text
            r4 = ball.find_all("li", class_="ball_red")[3].text
            r5 = ball.find_all("li", class_="ball_red")[4].text
            r6 = ball.find_all("li", class_="ball_red")[5].text
            b1 = ball.find_all("li", class_="ball_blue")[0].text

            # 开奖顺序
            open_r1 = ball.find_all("td")[3].text.strip().split()[0]
            open_r2 = ball.find_all("td")[3].text.strip().split()[1]
            open_r3 = ball.find_all("td")[3].text.strip().split()[2]
            open_r4 = ball.find_all("td")[3].text.strip().split()[3]
            open_r5 = ball.find_all("td")[3].text.strip().split()[4]
            open_r6 = ball.find_all("td")[3].text.strip().split()[5]
            open_b1 = b1

            line = dateno + ','
            line = line + year + ','
            line = line + month + ','
            line = line + date + ','
            line = line + r1 + ','
            line = line + r2 + ','
            line = line + r3 + ','
            line = line + r4 + ','
            line = line + r5 + ','
            line = line + r6 + ','
            line = line + b1 + ','
            line = line + open_r1 + ','
            line = line + open_r2 + ','
            line = line + open_r3 + ','
            line = line + open_r4 + ','
            line = line + open_r5 + ','
            line = line + open_r6 + ','
            line = line + open_b1 + '\n'

            f = open(txtName, "a+")
            f.write(line)
            f.close()

            print(dateno)
        except:
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ')
            continue

if __name__ == '__main__':
    # ssqtotxt()
    # print(type(time.strftime("%Y%m%d", time.localtime()) ))
    ssqbydateno('18002')