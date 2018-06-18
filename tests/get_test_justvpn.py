#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from justvpn import JustVpnSession
from getpass import getpass


def main(argv=None):
    idcode = input("请输入你的学号:")
    password = getpass("请输入你的VPN密码:")
    myaccount = JustVpnSession(idcode, password)
    while not myaccount.login():
        print("认证失败，请重新输入")
        idcode = input("请输入你的学号:")
        password = input("请输入你的VPN密码:")
        myaccount = JustVpnSession(idcode, password)
    print("登录成功！")
    res = myaccount.get('cnki.net', isUrlEncode=True)#获取网页
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    html_file = open("cnki.html","w")
    html_file.write(soup.prettify())
    print("已经将知网首页html保存到同目录下的cnki.html文件")

if __name__ == '__main__':
    main()
