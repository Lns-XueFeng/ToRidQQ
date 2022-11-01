import os
import sys

import requests
from requests import HTTPError

from .config import *
from .key import SCHOOL_ACCOUNT, SCHOOL_PASSWORD


sys.setrecursionlimit(100)   # 设置最大递归层数为100


class Internet:
    """
    程序因需要长时间运行, 且我的设备需要链接校园网
    因，校园网在一定时间后会失效，需重新连接
    故，需要另外加一个功能判断是否有网，如果无，则自动连接
    """
    def __init__(self):
        self.default_try_count = 5
        self._url = "http://10.255.0.19/drcom/login?"

        self._header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42",
        }
        self._params = {
            "callback": "dr1003",
            "DDDDD": SCHOOL_ACCOUNT,
            "upass": SCHOOL_PASSWORD,
            "0MKKey": "123456",
            "R1": "0",
            "R3": "0",
            "R6": "0",
            "para": "00",
            "v6ip": "",
            "v": "581",
        }

    def link_school_internet(self, try_link_count) -> int or None:
        """
        尝试协议登录校园网
        :return: 状态码 or None
        """
        res = None
        try:
            res = requests.get(
                url=self._url,
                headers=self._header,
                params=self._params,
            ).status_code
        except HTTPError as error:
            if try_link_count == self.default_try_count:
                raise error

        # if res != 200:
        #     sleep(1)
        #     cls.link_school_internet()

        return res

    @staticmethod
    def check_computer_internet() -> bool:
        """
        检查计算机是否有网络
        :return: True or False
        """
        res = os.system(PING_BAIDU)
        if res == 0:
            return True   # 有网络
        return False
