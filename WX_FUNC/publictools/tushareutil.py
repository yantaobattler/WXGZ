# -*- coding: UTF-8 -*-
import tushare as ts


def movie():
    df = ts.realtime_boxoffice()
    return df[['Irank',        # 排名
               'MovieName',    # 片名
               'BoxOffice']]   # 今日票房


def realtimestock(code):
    df = ts.get_realtime_quotes(code)  # Single stock symbol
    return df[['name',   # 股票名称
               'pre_close',  # 昨收
               'open',   # 今开
               'high',   # 今日最高价
               'low',    # 今日最低价
               'bid',    # 买一
               'ask']]   # 卖一


if __name__ == '__main__':
    # print(movie())
    print(realtimestock('300348'))
