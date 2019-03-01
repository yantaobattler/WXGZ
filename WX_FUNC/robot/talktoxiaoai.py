# -*- coding: UTF-8 -*-
import requests
import json
import datetime
import hashlib
import logging

logger = logging.getLogger("django")

app_key = 'ofVrzWyEhmwX'  # 自己注册的ashdestiny
app_sec = 'lbLCjMfD22r25mUck3KT'  # 自己注册的
uri = '/ask.do'
http_method = 'POST'
realm = 'xiaoi.com'


def get_signature():
    time_str = str(datetime.datetime.now())
    nonce = hashlib.sha1(time_str.encode()).hexdigest()

    HA1 = "{0}:{1}:{2}".format(app_key, realm, app_sec)
    HA1 = hashlib.sha1(HA1.encode()).hexdigest()

    HA2 = "{0}:{1}".format(http_method, uri)
    HA2 = hashlib.sha1(HA2.encode()).hexdigest()

    signature = "{0}:{1}:{2}".format(HA1, nonce, HA2)
    signature = hashlib.sha1(signature.encode()).hexdigest()

    # print("signature:" + signature)
    # print("nonce:" + nonce)
    ret = {}

    ret['signature'] = signature
    ret['nonce'] = nonce

    return ret


def get_http_header_xauth():
    ret_vals = get_signature()

    ret = "app_key=\"{0}\",nonce=\"{1}\",signature=\"{2}\"".format(app_key,
                                                                   ret_vals['nonce'],
                                                                   ret_vals['signature'])

    return ret


def toxiaoai(req_dict):  # xiaoai
    rsp_dict = {}
    content = '我不知道你在说什么~请说文字~'

    if req_dict.get('MsgType') == 'text':  # 小I也让他暂时只支持文字请求

        try:
            xauth = get_http_header_xauth()  # 获得签名信息
            head = {'Connection': 'keep-alive',
                    'X-Auth': xauth,  # 请求头要带着签名
                    "Content-type": "application/x-www-form-urlencoded",  # 官方文档上贴过来的
                    "Accept": "text/plain",  # 官方文档上贴过来的
                    }
            url = 'http://nlp.xiaoi.com/ask.do'

            data = {'userId': req_dict.get('FromUserName'),
                    'question': req_dict.get('Content'),
                    'type': '0',
                    'platform': 'custom'}  # 官方文档上贴过来的，没有会报错

            response = requests.post(url, headers=head, data=data)
            content = response.text
            # print(response.text)
        except Exception as e:
            logger.exception(e)
            content = '啧啧，崩溃了，重说一遍~'

    rsp_dict['Content'] = '[I]' + content
    rsp_dict['MsgType'] = 'text'
    return rsp_dict


if __name__=='__main__':
    req_dict = {'FromUserName': 'FromUserName',
                'ToUserName': 'ToUserName',
                'Content': '牛哥',
                'MsgType': 'text'}
    print(toxiaoai(req_dict))