# -*- coding: UTF-8 -*-
from WX_FUNC.models import UserList
from WX_FUNC.models import RobotLog
from WX_FUNC.robot import *

import logging
import time
import random


logger = logging.getLogger("django")


def start(FromUserName):

    rsp_content = '您已成功进入AI模式，接下来会有多名机器人随机为您服务，您可以开始了！\n回复“退出”可退出AI模式'

    UserList.objects.filter(FromUserName=FromUserName).update(UserStatus='02')  # 02 AI

    return rsp_content


def end(req_dict):
    rsp_dict = {}  # 返回报文

    UserList.objects.filter(FromUserName=req_dict.get('FromUserName')).update(UserStatus='00')

    rsp_dict['MsgType'] = 'text'
    rsp_dict['ToUserName'] = req_dict.get('FromUserName')
    rsp_dict['FromUserName'] = req_dict.get('ToUserName')
    rsp_dict['CreateTime'] = int(time.time())
    rsp_dict['Content'] = '您已退出AI模式'

    return rsp_dict


def switch(req_dict):

    rsp_dict = {}  # 返回报文

    # 直接退出AI模式
    if req_dict.get('MsgType') == 'text' and req_dict.get('Content') == '退出':
        rsp_dict = end(req_dict)
        return rsp_dict

    # 随机机器人提供服务
    # i = random.randint(1, 3)
    i = 1
    if i == 1:
        rsp_dict = talktotuling.totuling(req_dict)
    # elif i == 2:
    #     rsp_dict = talktoqingyunke.toqingyunke(req_dict)
    # elif i == 3:
    #     rsp_dict = talktoxiaoai.toxiaoai(req_dict)

    # 20181224 改为本地机器人识别
    # rsp_dict = talktolocalrobot.localrobot(req_dict)

    rsp_dict['ToUserName'] = req_dict.get('FromUserName')
    rsp_dict['FromUserName'] = req_dict.get('ToUserName')
    rsp_dict['CreateTime'] = int(time.time())
    # rsp_dict['Content'] = '这是AI模式'
    # rsp_dict['MsgType'] = 'text'

    # 写日志
    RobotLog.objects.create(FromUserName=req_dict.get('FromUserName', ''),
                            # RobotType=str(i),
                            RobotType='L',
                            MsgType=req_dict.get('MsgType', ''),
                            MsgId=req_dict.get('MsgId', ''),
                            ReqDict=str(req_dict),
                            RspDict=str(rsp_dict))

    return rsp_dict

if __name__ == '__main__':
    req_dict = {'FromUserName': 'FromUserName',
                'ToUserName': 'ToUserName',
                'Content': 'AI',
                'MsgType': 'text'}
    print(switch(req_dict))