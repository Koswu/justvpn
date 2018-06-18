#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from JustVpn import JustVpnSession


def main(argv=None):
    idcode = input("请输入你的学号:")
    password = input("请输入你的VPN密码:")
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
    print (soup.prettify())

if __name__ == '__main__':
    main()
