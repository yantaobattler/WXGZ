# -*- coding: UTF-8 -*-
from django.shortcuts import HttpResponse
import logging


logger = logging.getLogger("django")


def switch(req_dict):
    if req_dict['Event'] == 'subscribe':  # 关注
        rsp_content = '欢迎关注本实验室！下面的各种功能可以随便尝试，' \
                      '如果发现有问题或者有好的建议，请到“提建议”菜单进行登记\n' \
                      'enjoy yourself!'

    else:
        rsp_content = '收到按钮！'
    return rsp_content
