import unittest

import requests

from toridqq import Internet


class TestInternet(unittest.TestCase):

    def test_link_https_internet(self):
        """测试对https://www.baidu.com发起一个http请求且返回状态码为200"""
        result = requests.get("https://www.baidu.com").status_code
        self.assertEqual(result, 200)

    def test_check_computer_internet(self):
        """测试此计算机是否联网, 联网则result为True"""
        internet = Internet()
        result = internet.check_computer_internet()
        self.assertTrue(result, True)
