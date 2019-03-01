# -*- coding: UTF-8 -*-
from WX_FUNC.publictools import *
from WX_FUNC.models import UserList
import logging

logger = logging.getLogger("django")


def start(FromUserName):

    rsp_content = '目前仅支持福彩双色球查询\n' \
                  '请输入“ssq” + 开奖期数\n' \
                  '如：ssq18001'

    UserList.objects.filter(FromUserName=FromUserName).update(UserStatus='03')  # 03彩票

    return rsp_content


def excute(content):

    try:
        if content.startswith('ssq'):
            dateno = content[3:]
            result_dict = caipiao.ssqbydateno(dateno)

            if len(result_dict) == 0:
                rsp_content = '没有查询到您输入的期次！'
            else:
                rsp_content = '双色球第'+dateno+'期\n'
                rsp_content = rsp_content + '开奖日期：'
                rsp_content = rsp_content + result_dict['year'] + '年'
                rsp_content = rsp_content + result_dict['month'] + '月'
                rsp_content = rsp_content + result_dict['date'] + '日\n'
                rsp_content = rsp_content + '红球:'
                rsp_content = rsp_content + result_dict['r1'] + ','
                rsp_content = rsp_content + result_dict['r2'] + ','
                rsp_content = rsp_content + result_dict['r3'] + ','
                rsp_content = rsp_content + result_dict['r4'] + ','
                rsp_content = rsp_content + result_dict['r5'] + ','
                rsp_content = rsp_content + result_dict['r6'] + '\n'
                rsp_content = rsp_content + '蓝球:' + result_dict['b1'] + '\n'
                rsp_content = rsp_content + '出球顺序:' + result_dict['open'].replace(' ', ',')

        else:
            rsp_content = '暂不支持其他彩票查询'

    except Exception as e:
        logger.exception(e)
        rsp_content = '请再试一次'

    return rsp_content
