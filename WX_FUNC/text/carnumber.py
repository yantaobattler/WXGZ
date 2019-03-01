# -*- coding: UTF-8 -*-
from WX_FUNC.publictools import *


def carnumberlimit(content):

    if content == '限号':
        return '请输入您要查询的城市'

    rsp_content = '您查询的地区没有限号信息'

    city = content[2:]
    rsp_dict = xianhao.excute()

    for k in rsp_dict:
        if k.endswith(city):
            rsp_content = k + '\n' + rsp_dict[k]

    return rsp_content
