# -*- coding: UTF-8 -*-
import requests
import json

import logging

logger = logging.getLogger("django")


def toqingyunke(req_dict):  # 青云客智能聊天机器人
    rsp_dict = {}
    content = '你到底在说神马呀~'

    if req_dict.get('MsgType') == 'text':  # 青云客只支持文字请求
        try:
            apiUrl = 'http://api.qingyunke.com/api.php'
            para = {'key': 'free', 'appid': '0', 'msg': req_dict.get('Content')}

            rsp = requests.get(apiUrl, params=para)

            # json to dict
            rsp_dict = json.loads(s=rsp.text)

            if rsp_dict['result'] == 0:
                content = rsp_dict.get('content', '你到底在说神马呀~')
        except Exception as e:
            logger.exception(e)
            content = '啧啧，崩溃了，重说一遍~'

    rsp_dict['Content'] = '[Q]'+content
    rsp_dict['MsgType'] = 'text'
    return rsp_dict


if __name__=='__main__':
    req_dict = {'FromUserName': 'FromUserName',
                'ToUserName': 'ToUserName',
                'Content': '牛哥',
                'MsgType': 'text'}
    print(toqingyunke(req_dict))