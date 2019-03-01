# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from WX_FUNC.publictools import *
from WX_FUNC.event import *
from WX_FUNC.text import textmain
from WX_FUNC.robot import robotmain
from WX_FUNC.models import MainTransLog
from WX_FUNC.models import UserList


import logging
import time


logger = logging.getLogger("django")


def mainfunc(request):

    # 接受微信服务器配置验证时需要调用此函数
    # echostr = checksignature.checksignature(request)
    # return HttpResponse(echostr)
    logger.info(request.body)

    req_dict = xmltrans.trans_xml_to_dict(request.body)
    rsp_dict = {}

    try:

        # 查询流水是否有重复
        if req_dict.get('MsgType', '') == 'text':  # 文本信息处理
            # 文本用msgid判重
            if MainTransLog.objects.filter(MsgId=req_dict.get('MsgId')).count() > 0:
                # 未处理信息返回空
                return HttpResponse('')

        elif req_dict.get('MsgType', '') == 'event':  # 按钮信息处理
            # 事件用FromUserName+CreateTime判重
            if MainTransLog.objects.filter(FromUserName=req_dict.get('FromUserName'),
                                           CreateTime=req_dict.get('CreateTime')).count() > 0:
                # 未处理信息返回空
                return HttpResponse('')

        # 处理非重复消息
        # 记录请求主流水表
        MainTransLog.objects.create(FromUserName=req_dict.get('FromUserName', ''),
                                    CreateTime=req_dict.get('CreateTime', ''),
                                    MsgType=req_dict.get('MsgType', ''),
                                    MsgId=req_dict.get('MsgId', ''))

        # 开始处理
        if request.method == 'POST':

            # AI对话模式直接跳转
            if UserList.objects.filter(FromUserName=req_dict.get('FromUserName')).count() > 0:
                userstatusflag = UserList.objects.filter(FromUserName=req_dict.get('FromUserName'))[0].UserStatus
                if userstatusflag == '02':  # AI聊天
                    rsp_dict = robotmain.switch(req_dict)
                    rsp_xml = xmltrans.trans_dict_to_xml(rsp_dict)
                    return HttpResponse(rsp_xml)

            # 非AI模式再判断
            if req_dict.get('MsgType') == 'text':  # 文本信息处理
                rsp_content = textmain.switch(req_dict)
                rsp_dict['MsgType'] = 'text'
                rsp_dict['ToUserName'] = req_dict.get('FromUserName')
                rsp_dict['FromUserName'] = req_dict.get('ToUserName')
                rsp_dict['CreateTime'] = int(time.time())
                rsp_dict['Content'] = rsp_content
                rsp_xml = xmltrans.trans_dict_to_xml(rsp_dict)
                return HttpResponse(rsp_xml)

            elif req_dict.get('MsgType') == 'event':  # 按钮信息处理
                rsp_content = eventmain.switch(req_dict)
                rsp_dict['MsgType'] = 'text'
                rsp_dict['ToUserName'] = req_dict.get('FromUserName')
                rsp_dict['FromUserName'] = req_dict.get('ToUserName')
                rsp_dict['CreateTime'] = int(time.time())
                rsp_dict['Content'] = rsp_content
                rsp_xml = xmltrans.trans_dict_to_xml(rsp_dict)
                return HttpResponse(rsp_xml)

        elif request.method == 'GET':
            logger.info(request)
    except Exception as e:
        logger.exception(e)
    # 未处理信息返回空
    return HttpResponse('')


if __name__ == '__main__':
    reqbody_text = b'<xml><URL><![CDATA[http://39.107.236.31/WX_FUNC/mainfunc/]]></URL>' \
              b'<ToUserName><![CDATA[ToUserName]]></ToUserName>' \
              b'<FromUserName><![CDATA[FromUserName]]></FromUserName>' \
              b'<CreateTime>123456</CreateTime>' \
              b'<MsgType><![CDATA[text]]></MsgType>' \
              b'<Content><![CDATA[\xe9\x98\xbf\xe6\x96\xaf\xe8\x92\x82\xe8\x8a\xac]]></Content>' \
              b'<MsgId>9877</MsgId></xml>'
    # 生活玩
    reqbody_event = b'<xml><ToUserName><![CDATA[gh_fbe56efbaba6]]></ToUserName>' \
                    b'<FromUserName><![CDATA[owVW40mpS0nmRsMCIVl_tl75-Oh8]]></FromUserName>' \
                    b'<CreateTime>1519954302</CreateTime>' \
                    b'<MsgType><![CDATA[event]]></MsgType>' \
                    b'<Event><![CDATA[VIEW]]></Event>' \
                    b'<EventKey><![CDATA[http://mp.weixin.qq.com/s?__biz=MzUzNTI5NTkzNw==&mid=2247483652&idx=1&sn=bac982f0def58c50fa156acf2fa80f2e&chksm=fa86e3aacdf16abc30c812f5a9a73eb3d8ffe040893d1d1a9fa06e84c27e78faaefb44c2e59c&scene=18#wechat_redirect]]></EventKey>' \
                    b'<MenuId>412954514</MenuId></xml>'
    # aa = xmltrans.trans_xml_to_dict(reqbody_text)
    # print(MainTransLog.objects.filter(MsgId='6529381623650200355'))
    # request.body=reqbody_text
    # mainfunc(request)