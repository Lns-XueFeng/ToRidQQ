import random
import time

import requests
from requests import HTTPError

from toridqq.config import *
from utils import NoRequestResponse


class ToRidKJ:
    """
    ToRidKJ即为：摆脱QQ空间
    将QQ空间中新出的动态（仅自己想了解的好友, 推送至手机）
    """
    def __init__(self):
        self.rid = random.random()
        self.time_stamp = time.time()
        self.window_ld = random.random()
        self.url = URL.format(self.rid, self.time_stamp, self.window_ld)
        self.header = HEADER
        self.data_text = None
        self.parsed_text = None

    def request(self):
        res = requests.get(url=self.url, headers=HEADER)
        if res.status_code == 200:
            self.data_text = res.text.replace("_Callback", "")
        raise HTTPError

    def parse_text(self):
        if self.data_text:
            pass
        raise NoRequestResponse
