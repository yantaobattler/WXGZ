import requests
from bs4 import BeautifulSoup

from django.conf import settings
import sys
import os
import django


# head 信息
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Connection': 'keep-alive'}
tag = ['AQI',
       'PM2.5',
       'PM10',
       'CO',
       'NO2',
       'O3',
       'O3/8h',
       'S02']

# 外部引用django配置时需要这么写
pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '../..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WXGZ.settings")
django.setup()
from WX_FUNC.models import CityList


def excute(city):
    status = {}

    # 不需要用代理
    if CityList.objects.filter(CityName=city).count() > 0:
        c = CityList.objects.filter(CityName=city)
        # print(c[0])
    else:
        return {}

    url = 'http://www.pm25.in/' + c[0].CityURL.strip() + '/'

    response = requests.get(url, headers=head)
    soup = BeautifulSoup(response.text, 'lxml')
    citystatus = soup.find_all("div", class_="span12 data")  # 这是个list
    # print(citystatus)

    status_list = citystatus[0].find_all("div", class_="span1")  # list的第一个才能继续find
    # print(len(status_list))
    for i in range(8):
        status[tag[i]] = status_list[i].find("div", class_="value").text.strip()
    # print(status)

    # 污染等级
    status['level'] = soup.h4.text.strip()  # 直接soup.h4可以取到soup里的第一个h4标签
    # 更新时间
    status['time'] = soup.p.text.strip()

    return status


def getcitylist():
    # 不需要用代理
    response = requests.get('http://www.pm25.in/', headers=head)
    soup = BeautifulSoup(response.text, 'lxml')

    # file = open('d:/1.TXT', 'r')
    # page = file.read()
    # soup = BeautifulSoup(page, 'lxml')

    citys = soup.find_all("div", class_="all")  # 这是list of全部城市那个div
    city_li = citys[0].find_all("li")  # list的第一个才能继续find
    for eachcity in city_li:
        cityname = eachcity.a.text.strip()
        cityurl = eachcity.a.get('href')
        CityList.objects.update_or_create(CityName=cityname, CityURL=cityurl)


if __name__ == '__main__':

    getcitylist()
