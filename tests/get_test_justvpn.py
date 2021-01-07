#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from justvpn import JustVpnSession
import configparser


def main(argv=None):
    config = configparser.ConfigParser()
    config.read('account.ini')
    idcode = config.get('account', 'username')
    password = config.get('account', 'password')
    myaccount = JustVpnSession(idcode, password)
    if not myaccount.login():
        print("认证失败")
        exit(1)
    print("登录成功！")
    res = myaccount.get('cnki.net')#获取网页
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    html_file = open("cnki.html","w")
    html_file.write(soup.prettify())
    print("已经将知网首页html保存到同目录下的cnki.html文件")

if __name__ == '__main__':
    main()
