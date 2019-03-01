# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
import hashlib
import logging

'''
# 接受微信服务器配置验证时需要调用此函数
'''

logger = logging.getLogger("django")


def checksignature(request):
    try:
        signature = request.GET['signature']
        timestamp = request.GET['timestamp']
        nonce = request.GET['nonce']
        echostr = request.GET['echostr']
        list = [timestamp,
                nonce,
                'thisisthewxtoken']
        list.sort()
        logger.info(list)
        liststr = list[0] + list[1] + list[2]
        logger.info(liststr)
        logger.info('*' * 20)
        logger.info(hashlib.sha1(liststr.encode()).hexdigest())
    except Exception as e:
        logger.exception(e)

    if signature == hashlib.sha1(liststr.encode()).hexdigest():
        return echostr