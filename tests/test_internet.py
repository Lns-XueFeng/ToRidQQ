import unittest

import requests

from ToRidQQ.internet import Internet


class TestInternet(unittest.TestCase):

    def test_link_https_internet(self):
        """测试对https://www.baidu.com发起一个http请求且返回状态码为200"""
        result = requests.get("https://www.baidu.com").status_code
        self.assertEqual(result, 200)

    def test_check_computer_internet(self):
        """测试此计算机是否联网, 联网则result为True"""
        result = Internet.check_computer_internet()
        self.assertTrue(result, True)
