import unittest

import requests

from internet import Internet


class TestInternet(unittest.TestCase):

    def test_link_https_internet(self):
        result = requests.get("https://www.baidu.com").status_code
        self.assertEqual(result, 200)

    def test_check_computer_internet(self):
        result = Internet.check_computer_internet()
        self.assertTrue(result, True)
