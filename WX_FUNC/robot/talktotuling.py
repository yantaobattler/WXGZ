# -*- coding: UTF-8 -*-
import requests
import json

import logging

logger = logging.getLogger("django")

apiKey = 'c9b19fa38a61457fba5fc6aa0b0b6c72'  # 自己注册的
apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'


def totuling(req_dict):  # 图灵机器人
    rsp_dict = {}
    content = '图灵不理解。请继续。'

    userInfo = {
        'apiKey': apiKey,
        'userId': req_dict.get('FromUserName').replace('-', '').replace('_', '')
    }

    inputText = {}
    inputImage = {}
    inputMedia = {}
    selfInfo = {}

    perception = {
        'inputText': inputText,
        'inputImage': inputImage,
        'inputMedia': inputMedia,
        'selfInfo': selfInfo
    }

    try:
        if req_dict.get('MsgType') == 'text':  # 文字请求
            inputText['text'] = req_dict.get('Content')

            data = {
                'reqType'    : 0,  # int 输入类型:0-文本(默认)、1-图片、2-音频
                'perception'   : perception,  # 输入信息
                'userInfo': userInfo,  # 用户参数
            }
            # 我们通过如下命令发送一个post请求
            response = requests.post(apiUrl, data=json.dumps(data))
            content = dealwithresponse(response)

        elif req_dict.get('MsgType') == 'image':  # 图片
            inputImage['url'] = req_dict.get('PicUrl')

            data = {
                'reqType': 1,  # int 输入类型:0-文本(默认)、1-图片、2-音频
                'perception': perception,  # 输入信息
                'userInfo': userInfo,  # 用户参数
            }
            # 我们通过如下命令发送一个post请求
            response = requests.post(apiUrl, data=json.dumps(data))
            content = dealwithresponse(response)

        elif req_dict.get('MsgType') == 'voice':  # 文字请求
            inputText['text'] = req_dict.get('Recognition')

            data = {
                'reqType'    : 0,  # int 输入类型:0-文本(默认)、1-图片、2-音频
                'perception'   : perception,  # 输入信息
                'userInfo': userInfo,  # 用户参数
            }
            # 我们通过如下命令发送一个post请求
            response = requests.post(apiUrl, data=json.dumps(data))
            content = dealwithresponse(response)

    except Exception as e:
        logger.exception(e)
        content = '啧啧，崩溃了，重说一遍~'

    rsp_dict['Content'] = '[T]' + content
    rsp_dict['MsgType'] = 'text'
    return rsp_dict


def dealwithresponse(response):

    content = ''
    dict_temp = json.loads(s=response.text)

    try:
        # 先把多个回答组的文字部分挑出来
        for value in dict_temp['results']:
            if value['resultType'] == 'text':
                content = content + value['values']['text']
        # 文字后面拼URL
        for value in dict_temp['results']:
            if value['resultType'] == 'url':
                content = content + '\n' + value['values']['url']
        # 其他类型信息不处理，写日志
        for value in dict_temp['results']:
            if value['resultType'] == 'voice':
                logger.info('*'*20 + 'tuling return a voice:')
                logger.info(dict_temp)
            if value['resultType'] == 'video':
                logger.info('*'*20 + 'tuling return a video:')
                logger.info(dict_temp)
            if value['resultType'] == 'image':
                logger.info('*'*20 + 'tuling return a image:')
                logger.info(dict_temp)
            if value['resultType'] == 'news':
                logger.info('*'*20 + 'tuling return a news:')
                logger.info(dict_temp)
    except Exception as e:
        logger.exception(dict_temp)


    return content


if __name__ == '__main__':
    req_dict = {'FromUserName': 'owVW40mpS0nmRsMCIVl_tl75-Oh8',
                'ToUserName': 'ToUserName',
                'Content': '赫萝',
                'MsgType': 'text'}
    print(totuling(req_dict))


