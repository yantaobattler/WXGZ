# -*- coding: UTF-8 -*-
from django.shortcuts import HttpResponse
from WX_FUNC.publictools import *
from WX_FUNC.text import *
from WX_FUNC.robot import robotmain
from WX_FUNC.models import UserList
import logging


logger = logging.getLogger("django")


def switch(req_dict):
    # 先对带状态的输入进行处理

    # 如果记录过状态则取现有状态
    if UserList.objects.filter(FromUserName=req_dict.get('FromUserName')).count() > 0:
        userstatusflag = UserList.objects.filter(FromUserName=req_dict.get('FromUserName'))[0].UserStatus

    else:  # 如果没记录过状态则新建00
        UserList.objects.create(FromUserName=req_dict.get('FromUserName'), UserStatus='00')
        userstatusflag = '00'

    # 状态退出处理
    if req_dict.get('Content') == '退出':  # 需要登记status的公共退出
        if userstatusflag == '00':
            rsp_content = '您没有正在进行的项目！'
        else:
            rsp_content = '您已退出' + userstatus.status.get(userstatusflag, '!')
            UserList.objects.filter(FromUserName=req_dict.get('FromUserName')).update(UserStatus='00')

        return rsp_content

    # 状态操作执行
    if userstatusflag == '01':  # 股票查询
        rsp_content = stock.excute(req_dict.get('Content'))
    # views直接跳转AI， text不处理
    # elif userstatusflag == '02':  # AI聊天
    #     rsp_content = ''
    elif userstatusflag == '03':  # 彩票查询
        rsp_content = lottery.excute(req_dict.get('Content'))
    elif userstatusflag == '04':  # 建议
        rsp_content = suggest.excute(req_dict)

    else:
        # 再对无状态文字或者状态进入开关进行处理
        if req_dict.get('Content').startswith('空气'):  # 查空气质量处理
            rsp_content = airquality.airquality(req_dict.get('Content'))  # 中文

        elif req_dict.get('Content') == '电影':  # 查电影处理
            rsp_content = movie.getmovie5(req_dict.get('Content'))  # 中文

        elif req_dict.get('Content') == '股票':  # 查股票处理start
            rsp_content = stock.start(req_dict.get('FromUserName'))  # 中文

        elif req_dict.get('Content').upper() == 'AI':  # AI处理start
            rsp_content = robotmain.start(req_dict.get('FromUserName'))  # 中文

        elif req_dict.get('Content').startswith('限号'):  # 查限号
            rsp_content = carnumber.carnumberlimit(req_dict.get('Content'))  # 中文

        elif req_dict.get('Content') == '建议':  # 建议处理start
            rsp_content = suggest.start(req_dict.get('FromUserName'))

        elif req_dict.get('Content') == '彩票':  # 彩票start
            rsp_content = lottery.start(req_dict.get('FromUserName'))

        else:
            rsp_content = '收到！'

    return rsp_content


if __name__ == '__main__':
    req_dict = {'FromUserName': 'FromUserName', 'Content': '限号天津'}
    print(switch(req_dict))

