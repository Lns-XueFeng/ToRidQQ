import os
import sys
import logging
from time import sleep

import requests
from requests import HTTPError

from key import SCHOOL_ACCOUNT, SCHOOL_PASSWORD
from config import *


sys.setrecursionlimit(100)   # 设置最大递归层数为100


class Internet:
    """
    程序因需要长时间运行, 且我的设备需要链接校园网
    因，校园网在一定时间后会失效，需重新连接
    故，需要另外加一个功能判断是否有网，如果无，则自动连接
    """
    _url = "http://10.255.0.19/drcom/login?"

    _header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42",
    }
    _params = {
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

    @classmethod
    def link_school_internet(cls):
        res = None
        try:
            res = requests.get(
                url=Internet._url,
                headers=Internet._header,
                params=Internet._params,
            ).status_code
        except HTTPError as error:
            logging.error(f"{LOG_ERROR_ONE}{error}")

        if res != 200:
            sleep(1)
            cls.link_school_internet()
            logging.warning(LOG_WARN_FOUR)

        logging.info(LOG_INGO_FIVE)
        return res

    @classmethod
    def check_computer_internet(cls):
        res = os.system(PING_BAIDU)
        if res == 0:
            return True
        return False


if __name__ == "__main__":
    # r = Internet.link_school_internet()
    # print(r)
    r = Internet.check_computer_internet()
    print(r)
