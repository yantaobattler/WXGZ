# -*- coding: UTF-8 -*-
import requests
import json

import logging

logger = logging.getLogger("django")


def localrobot(req_dict):  # 本地机器人
    rsp_dict = {}
    content = '你到底在说神马呀~'

    if req_dict.get('MsgType') == 'text':  # 本地机器人 暂时只支持文字请求
        try:
            rsp = req_dict.get('Content')

            rsp = rsp.replace('?', '!')
            rsp = rsp.replace('？', '!')
            rsp = rsp.replace('你', '我')
            rsp = rsp.replace('啥', '什么')
            rsp = rsp.replace('知不知道', '不知道')
            rsp = rsp.replace('为什么', '不知道为什么')
            rsp = rsp.replace('吗', '')
            rsp = rsp.replace('怎么样', '不知道怎么样')
            rsp = rsp.replace('谁', '一个厉害的人')

            if '闫涛' in rsp:
                rsp = '你找他干什么呀!'
            if '圣诞' in rsp:
                rsp = '死而复生？吃我铁拳圣裁啦！'
            if '勇者' in rsp:
                rsp = '一个鲁拉就回家啦！'
            if '法老' in rsp:
                rsp = '哈哈哈哈哈哈哈哈哈！'
            if '贞德' in rsp:
                rsp = '我是合格的圣诞老人！'
            if 'saber' in rsp.lower():
                rsp = '懂人心还是不懂人心？'
            if 'archer' in rsp.lower():
                rsp = '红茶绿茶黑茶闪茶你要哪个？'
            if 'lancer' in rsp.lower():
                rsp = '真英雄用眼神杀人！'
            if 'caster' in rsp.lower():
                rsp = '让我们来聊聊王的故事吧！'
            if 'assassin' in rsp.lower():
                rsp = '冠位之名非吾所需！'
            if 'rider' in rsp.lower():
                rsp = '这就是那片大海吧！'
            if 'berserker' in rsp.lower():
                rsp = '安珍大人！'
            if 'ego' in rsp.lower():
                rsp = '人造？哼哼哼！'
            if 'shelder' in rsp.lower():
                rsp = 'Lord Camelot！'
            if 'foreigner' in rsp.lower():
                rsp = '这啥？还没有呢 ！'
            if 'ruler' in rsp.lower():
                rsp = '吾主在此！'
            if 'avenger' in rsp.lower():
                rsp = '小安在哪里？'
            if 'cancer' in rsp.lower():
                rsp = '仅此一人！'
            if '学妹' in rsp.lower():
                rsp = '前辈！'

            content = rsp
        except Exception as e:
            logger.exception(e)
            content = '啧啧，崩溃了，重说一遍~'
    else:
        content = '目前只支持文字对话哦亲'

    rsp_dict['Content'] = content
    rsp_dict['MsgType'] = 'text'
    return rsp_dict


if __name__=='__main__':
    req_dict = {'FromUserName': 'FromUserName',
                'ToUserName': 'ToUserName',
                'Content': '你吃饭了吗？',
                'MsgType': 'text'}
    print(localrobot(req_dict))