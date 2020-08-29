from unittest import TestCase
from justvpn import JustVpnSession
from configparser import ConfigParser
from bs4 import BeautifulSoup


class TestJustVpnSession(TestCase):
    def __init__(self, method_name: str = ...):
        super().__init__(method_name)
        self.config = ConfigParser()
        self.config.read('config.ini')
        login_cfg = self.config['login']
        username = login_cfg['USERNAME']
        password = login_cfg['PASSWORD']
        self.session = JustVpnSession(username, password)

    def test_login(self):
        self.assertTrue(self.session.login())
        self.session.close()

    def test_get(self):
        self.assertTrue(self.session.login())
        res = self.session.get('https://www.cnki.net')
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        self.assertEqual(soup.title.text, '中国知网')
        self.session.close()

    def test_post(self):
        # TODO: post 测试
        # self.assertTrue(self.session.login())
        # self.session.close()
        pass

    def test_encode_url(self):
        source_urls = ['http://jwgl.just.edu.cn:8080/',
                       'jwgl.just.edu.cn:8080',
                       'http://jwgl.just.edu.cn:8080/a/b/',
                       'https://www.cnki.net/a/b',
                       'https://ids.v.just.edu.cn:4443/cas/login?service=http%3A%2F%2Fmy.just.edu.cn%2F'
                       ]
        target_urls = ['https://54a22a8aad6e5ffd02eb5278924100b5my.v.just.edu.cn:4443/',
                       'https://54a22a8aad6e5ffd02eb5278924100b5my.v.just.edu.cn:4443/',
                       'https://54a22a8aad6e5ffd02eb5278924100b5my.v.just.edu.cn:4443/a/b/',
                       'https://elkssl0d53ff2b217dbf7bcdae2fa7a747bda5my.v.just.edu.cn:4443/a/b/',
                       'https://ids.v.just.edu.cn:4443/cas/login?service=http%3A%2F%2Fmy.just.edu.cn%2F'
                       ]
        for source, target in zip(source_urls, target_urls):
            self.assertEqual(target, JustVpnSession.encode_url(source))
