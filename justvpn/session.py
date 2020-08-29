#!/usr/bin/python3
# coding:utf-8
import requests
from urllib.parse import urlparse
import hashlib
import re
from bs4 import BeautifulSoup

from requests.packages.urllib3.exceptions import InsecureRequestWarning


class JustVpnSession(requests.Session):
    _LOGIN_URL = 'https://ids.v.just.edu.cn:4443/cas/login?service=http://my.just.edu.cn/'
    _VPN_URL = 'https://vpn2.just.edu.cn/'
    _HEADER = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"}
    _WHITE_LIST = [
        'ids.v.just.edu.cn',
        'my.v.just.edu.cn',
        'my.just.edu.cn',
    ]

    def __init__(self, username, password):
        super().__init__()
        for key in self._HEADER:
            self.headers[key] = self._HEADER[key]
        self._username = str(username)
        self._password = str(password)
        self._is_login = False
        self.verify = False

    def is_login(self):
        return self._is_login

    def login(self) -> bool:
        """
        登录vpn
        :return:
        """
        if self._is_login:
            return True
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        res = super().get(self._VPN_URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        hidden_item = soup.find('input', {'name': 'execution'})
        if hidden_item is None:
            raise Exception('find login token failed.')
        execution_val = hidden_item['value']
        login_payload = {
            "username": self._username,
            "password": self._password,
            "_eventId": 'submit',
            "loginType": '1',
            'submit': '登 录',
            'execution': execution_val,
        }
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        res = super().post(self._LOGIN_URL, login_payload)
        self._is_login = True
        soup = BeautifulSoup(res.text, 'html.parser')
        if soup.title.text == "江苏科技大学":
            return True
        return False

    def get(self, url, **kwargs):
        if 'is_encode' not in kwargs or kwargs['is_encode']:
            res = super().get(self.encode_url(url), verify=False, **kwargs)
        else:
            res = super().get(url, verify=False, **kwargs)
        return res

    def post(self, url, data=None, json=None, **kwargs):
        if 'is_encode' not in kwargs or kwargs['is_encode']:
            return super().post(self.encode_url(url), data, json, verify=False, **kwargs)
        else:
            return super().post(url, data, json, verify=False, **kwargs)

    @staticmethod
    def encode_url(url: str) -> str:
        if re.match(r"https?://.+", url) is None:
            url = "http://" + url
        parsed = urlparse(url)
        if parsed.netloc.split(':')[0] in JustVpnSession._WHITE_LIST:
            return url
        prefix = hashlib.md5(parsed.netloc.encode('utf-8')).hexdigest()
        if parsed.scheme == 'https':
            prefix = 'elkssl' + prefix
        path = parsed.path
        if path == '':
            path = '/'
        if path[-1] != '/':
            path += '/'
        return 'https://%smy.v.just.edu.cn:4443%s' % (prefix, path)
