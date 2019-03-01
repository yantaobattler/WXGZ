import requests
from bs4 import BeautifulSoup


# head 信息
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Connection': 'keep-alive'}


def main():
    # 代理IP地址
    # http的代理ip列表
    http_list = proxy_ip_http()
    # https的代理ip列表
    https_list = proxy_ip_https()
    proxy = {
        'http': http_list[0],
        'https': https_list[0],
    }
    p = requests.get('http://www.trcbank.com.cn/', headers=head, proxies=proxy)


# 搞代理ip
def proxy_ip_http():
    response = requests.get('http://www.xicidaili.com/wt/', headers=head)
    soup = BeautifulSoup(response.text, 'lxml')
    http_ip_list = []
    # print(soup)
    tr_list = soup.find_all("tr", class_=["odd", ""])
    '''
    tr_list里每个tr长这样
    <tr class="odd">
    <td class="country"><img alt="Cn" src="http://fs.xicidaili.com/images/flag/cn.png"/></td>
    <td>222.76.187.198</td>
    <td>8118</td>
    <td>
    <a href="/2018-01-19/fujian">福建厦门</a>
    </td>
    <td class="country">高匿</td>
    <td>HTTP</td>
    <td class="country">
    <div class="bar" title="0.344秒">
    <div class="bar_inner fast" style="width:91%">
    </div>
    </div>
    </td>
    <td class="country">
    <div class="bar" title="0.068秒">
    <div class="bar_inner fast" style="width:98%">
    </div>
    </div>
    </td>
    <td>3分钟</td>
    <td>18-01-19 22:33</td>
    </tr>
    '''

    for tr in tr_list:
        tdlist = tr.find_all('td')  # 在每个tr标签下,查找所有的td标签
        # print(tdlist[1].string)  # 这里提取IP值
        # print(tdlist[2].string)  # 这里提取端口值
        http_proxy_ip = 'http://'+tdlist[1].string+':'+tdlist[2].string
        http_ip_list.append(http_proxy_ip)
    return http_ip_list


def proxy_ip_https():
    response = requests.get('http://www.xicidaili.com/wn/', headers=head)
    soup = BeautifulSoup(response.text, 'lxml')
    https_ip_list = []
    # print(soup)
    tr_list = soup.find_all("tr", class_=["odd", ""])

    for tr in tr_list:
        tdlist = tr.find_all('td')  # 在每个tr标签下,查找所有的td标签
        # print(tdlist[1].string)  # 这里提取IP值
        # print(tdlist[2].string)  # 这里提取端口值
        https_proxy_ip = 'https://'+tdlist[1].string+':'+tdlist[2].string
        https_ip_list.append(https_proxy_ip)
    print(https_ip_list)
    return https_ip_list


if __name__ == "__main__":
    # execute only if run as a script
    main()