# -*- coding: UTF-8 -*-
from WX_FUNC.publictools import *
from WX_FUNC.models import UserList
import logging


logger = logging.getLogger("django")


def start(FromUserName):

    rsp_content = '请输入6位股票代码查询实时行情'

    UserList.objects.filter(FromUserName=FromUserName).update(UserStatus='01')  # 01股票查询

    return rsp_content


def excute(content):

    try:
        df = tushareutil.realtimestock(content)
        rsp_content = content + '  ' + df['name'][0] + '\n'
        rsp_content = rsp_content + '昨收：' + df['pre_close'][0] + '\n'
        rsp_content = rsp_content + '今开：' + df['open'][0] + '\n'
        rsp_content = rsp_content + '今日最高价：' + df['high'][0] + '\n'
        rsp_content = rsp_content + '今日最低价：' + df['low'][0] + '\n'
        rsp_content = rsp_content + '买一：' + df['bid'][0] + '\n'
        rsp_content = rsp_content + '卖一：' + df['ask'][0] + '\n'

    except Exception as e:
        logger.exception(e)
        rsp_content = '未查询到您输入的股票代码'

    return rsp_content

