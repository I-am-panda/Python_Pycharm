# coding = utf-8
import time

import requests
from bs4 import BeautifulSoup

# 请求头
header = {
    ':scheme': 'https',
    'cache-control': 'max-age=0',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': 'Hm_lvt_522b01156bb16b471a7e2e6422d272ba=1602816510; UM_distinctid=1752f4f095b8de-080c3f80720469-c781f38-144000-1752f4f095c89e; oauthBackUrl=https%3A%2F%2Fucenter.jin10.com%2F; onSound=1; onNotification=2; jinSize=normal; kind_g=%5B%223%22%2C%227%22%5D; trend=1; x-token=cd916c86-ae61-4093-b395-ce40d434a40f; admin_token=290ebdc7-7f06-4cd8-a98a-c7a2e1206035',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}
# 查找a标签链接
def search_url(url):
    urls = [
        "https://cdn.jin10.com/app_pages/vip_profile/index.html",
        "https://www.jin10.com/vip/payment/index.html"
    ]
    try:
        # 请求url
        r = requests.get(url,header,timeout=3)
    except:
        print("输入的链接有误，不能请求访问")
    for i in urls:
        if i == url:
            tyle =False
        else:
            tyle = True
    if  tyle ==False:
        urls.append(url)
    # 设置编码为utf-8
    r.encoding = 'utf - 8'
    # 转为字符串文本格式
    html = r.text
    print(html)
    # 解析成文档对象
    soup = BeautifulSoup(html, 'html.parser')
    # 查找文档中所有a标签
    a_label = soup.find_all('a')
    if not a_label:
        print("在该页面上没有找到任何超链接")
        return
    for k in a_label:
        # 查找href标签
        link = k.get('href')
        # link为空
        if link:
            # 检查链接能否访问
            check_url(link)

# 检查链接能否访问
def check_url(url):
    try:
        r = requests.get(url,timeout = 3)
        if r.status_code == 200:
            print("%s可以访问" %url)
    except:
        print("%s不能访问" %url)
        send_msg()

# 发送通知
def send_msg():
    pass


def main():

    url = input('请输入要检查的url：')
    if url == '':
        url = 'https://www.jin10.com/vip/payment/index.html'
    while True:
        print('退出脚本直接关闭运行窗口')
        # 查找页面上的所有a标签链接
        search_url(url)
        time.sleep(10)

if __name__ == '__main__':
    main()