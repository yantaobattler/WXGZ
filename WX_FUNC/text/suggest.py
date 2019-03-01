# -*- coding: UTF-8 -*-
from WX_FUNC.models import UserList
from WEB_FUNC.models import Suggest
import logging


logger = logging.getLogger("django")


def start(FromUserName):

    rsp_content = '您已进入意见建议模式，可以在下面直接输入了！'

    UserList.objects.filter(FromUserName=FromUserName).update(UserStatus='04')  # 04建议

    return rsp_content


def excute(req_dict):

    try:
        Suggest.objects.create(username=req_dict.get('FromUserName'),
                               channel='wx001',   # wx001-围观实验室
                               suggest=req_dict.get('Content'))
        rsp_content = '您的建议已经记录！\n' \
                      '您可以继续输入建议，或者回复“退出”来退出此模式'

    except Exception as e:
        logger.exception(e)
        rsp_content = '刚刚服务器晕了，没听清您的建议...\n' \
                      '请您再重新输入一次~'

    return rsp_content
