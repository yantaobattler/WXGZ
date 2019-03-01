# -*- coding: UTF-8 -*-
from WX_FUNC.publictools import *


def getmovie5(content):
    df = tushareutil.movie()
    rsp_content = '今日全国票房前列的电影是：' + '\n'
    rsp_content = rsp_content + df['MovieName'][0] + '，' + df['BoxOffice'][0] + '万\n'
    rsp_content = rsp_content + df['MovieName'][1] + '，' + df['BoxOffice'][1] + '万\n'
    rsp_content = rsp_content + df['MovieName'][2] + '，' + df['BoxOffice'][2] + '万\n'
    rsp_content = rsp_content + df['MovieName'][3] + '，' + df['BoxOffice'][3] + '万\n'
    rsp_content = rsp_content + df['MovieName'][4] + '，' + df['BoxOffice'][4] + '万\n'
    rsp_content = rsp_content + df['MovieName'][5] + '，' + df['BoxOffice'][5] + '万\n'
    rsp_content = rsp_content + df['MovieName'][6] + '，' + df['BoxOffice'][6] + '万\n'
    rsp_content = rsp_content + df['MovieName'][7] + '，' + df['BoxOffice'][7] + '万\n'
    rsp_content = rsp_content + df['MovieName'][8] + '，' + df['BoxOffice'][8] + '万\n'
    rsp_content = rsp_content + df['MovieName'][9] + '，' + df['BoxOffice'][9] + '万\n'

    # print(rsp_content)
    return rsp_content


if __name__=='__main__':
    getmovie5('1')