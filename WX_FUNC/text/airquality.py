# -*- coding: UTF-8 -*-
from WX_FUNC.publictools import *


def airquality(Content):
    city = Content[2:]
    if len(city) == 0:
        rsp_content = '请输入城市！'
        return rsp_content
    city_airquality = kongqi.excute(city)
    # print(city_airquality)
    if len(city_airquality) == 0:
        rsp_content = '对不起，未找到您要查询的城市！'
    else:
        rsp_content = city + '的空气质量为：'+ city_airquality.get('level')+'\n'
        rsp_content = rsp_content + '空气质量指数为：' + city_airquality.get('AQI')+'\n'
        rsp_content = rsp_content + '其中PM2.5浓度为：' + city_airquality.get('PM2.5') + 'μg/m3\n'
        rsp_content = rsp_content + 'PM10浓度为：' + city_airquality.get('PM10') + 'μg/m3\n'
        rsp_content = rsp_content + '二氧化氮浓度为：' + city_airquality.get('NO2') + 'μg/m3\n'
        rsp_content = rsp_content + '臭氧一小时浓度为：' + city_airquality.get('O3') + 'μg/m3\n'
        rsp_content = rsp_content + '臭氧八小时浓度为：' + city_airquality.get('O3/8h') + 'μg/m3\n'
        rsp_content = rsp_content + '二氧化硫浓度为：' + city_airquality.get('S02') + 'μg/m3\n'
        rsp_content = rsp_content + '一氧化碳浓度为：' + city_airquality.get('CO') + 'mg/m3\n'
        rsp_content = rsp_content + city_airquality.get('time')

    return rsp_content