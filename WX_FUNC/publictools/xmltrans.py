# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup

#  实现dict与utf8的xml之间转换
#
# reqbody = request.body
# e.g.:
# reqbody = b'<xml><URL><![CDATA[http://39.107.236.31/WX_FUNC/mainfunc/]]></URL>' \
#           b'<ToUserName><![CDATA[ToUserName]]></ToUserName>' \
#           b'<FromUserName><![CDATA[FromUserName]]></FromUserName>' \
#           b'<CreateTime>123456</CreateTime>' \
#           b'<MsgType><![CDATA[text]]></MsgType>' \
#           b'<Content><![CDATA[\xe9\x98\xbf\xe6\x96\xaf\xe8\x92\x82\xe8\x8a\xac]]></Content>' \
#           b'<MsgId>9877</MsgId></xml>'
#
# 可以直接把微信传过来的request.body转成dict
# dict1 = xmltrans.trans_xml_to_dict(reqbody)
# print(dict1)
# 可以直接把dict转成微信用的HttpResponse
# xml2 = xmltrans.trans_dict_to_xml(dict1)
# return HttpResponse(xml2)


def trans_xml_to_dict(xml):
    """
    将微信交互返回的 XML 格式数据转化为 Python Dict 对象，已转码
    :param xml: 原始 XML 格式数据
    :return: dict 对象
    """

    soup = BeautifulSoup(xml.decode('utf-8'), features='xml')
    xml = soup.find('xml')
    if not xml:
        return {}

    # 将 XML 数据转化为 Dict
    data = dict([(item.name, item.text) for item in xml.find_all()])
    return data




def trans_dict_to_xml(data):
    """
    将 dict 对象转换成微信交互所需的 XML 格式数据,已转码
    :param data: dict 对象
    :return: xml 格式数据
    """
    xml = []
    for k in sorted(data.keys()):
        v = data.get(k,   '')
        if k == 'detail' and not v.startswith('<![CDATA['):
            v = '<![CDATA[{}]]>'.format(v)
        xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
    return '<xml>{}</xml>'.format(''.join(xml)).encode()