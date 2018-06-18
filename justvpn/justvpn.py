#coding:utf-8
import requests
import os
from bs4 import BeautifulSoup
#禁用https安全警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class JustVpnSession(requests.Session):
    _LOGIN_URL = 'https://vpn.just.edu.cn/dana-na/auth/url_default/login.cgi'
    _URL_PREFIX = r'https://vpn.just.edu.cn/,DanaInfo='
    _header = {
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
    #LOGIN_URL = 'http://127.0.0.1:3378'
    def __init__(self, username, password):
        super().__init__()
        self._username = str(username)
        self._password = str(password)
    def login(self):
        postVals = {'btnSubmit':'登录',
                'password':self._password,
                'realm':'LDAP-REALM',
                'tz_offset': '480',
                'username': self._username }
        res = self.post(self._LOGIN_URL, postdata=postVals)
       # print(res)
        soup = BeautifulSoup(res.text, 'lxml')
        #检查是否认证成功
        if soup.find("input", id="btnSubmit_6") != None:
            return False
        #检查是否已经登录,如登录，尝试继续会话
        if soup.find("input", id="btnContinue") != None: 
            #print("已经登录，尝试继续会话")
            formDataStr = soup.find("input", id="DSIDFormDataStr").get("value")
            postdata = { 'btnContinue':'继续会话',
                    'FormDataStr':formDataStr }
            res = self.post(self._LOGIN_URL, postdata=postdata)
            #soup = BeautifulSoup(res.text, 'lxml')
        return True
        #print("登录成功")
        #print(soup.prettify())
    def get(self, url, isUrlEncode=False):
        if isUrlEncode:
            return super().get(self._encodeUrl(url), headers=self._header)
        else:
            return super().get(url, headers=self._header)
    def post(self, url, postdata, isUrlEncode=False):
        if isUrlEncode:
            return super().post(self._encodeUrl(url), data=postdata, verify=False, headers=self._header)
        else:
            return super().post(url, data=postdata,  verify=False, headers=self._header)
    def _encodeUrl(self, url):#给url加上访问前缀
        return self._URL_PREFIX + url

            
