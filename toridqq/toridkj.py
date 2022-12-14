import re
import random
import time
from urllib import parse
from multiprocessing import Process

import requests
from requests import HTTPError

from .config import *
from .utils import NoRequestResponse, NoKeyValueError


class ToRidKJ(Process):
    """
    ToRidKJ即为：摆脱QQ空间
    将QQ空间中新出的动态（仅自己想了解的好友, 推送至手机）
    """
    def __init__(self):
        super(ToRidKJ, self).__init__(daemon=True)
        self.cookie = HEADER["cookie"]
        self.g_tk = self.decrypt_g_tk()
        self.rid = random.random()
        self.time_stamp = time.time()
        self.window_ld = random.random()
        self.url = URL.format(
            self.rid, self.time_stamp, self.window_ld, self.g_tk, self.g_tk)
        self.header = HEADER
        self.data_text = None
        self.parsed_text = None
        self.key = None

    def decrypt_g_tk(self) -> int:
        """
        rid = random.random()
        time_stamp = time.time()
        window_ld = random.random()
        g_tk是最后一个加密参数, 与cookie相关
        :return:
        """
        key_list = re.findall("p_skey=(.*?);", self.cookie) or re.findall("skey=(.*?);", self.cookie) \
            or re.findall("rv2=(.*?);", self.cookie)
        self.key = key_list

        hash_value = 5381
        if not self.key:
            raise NoKeyValueError
        for i in self.key[0]:
            hash_value += (hash_value << 5) + ord(i)

        return hash_value & 2147483647

    def to_dict(self) -> str:
        """
        将cookie字符串转为字典形式
        :return:
        """
        new_cookie = "{" + self.cookie.replace("=", ":").replace(";", ",") + "}"
        return new_cookie

    def get_decode_data(self) -> str:
        """
        请求返回的数据里面有很多乱码的数据
        待再拿出来的时候进行解码得到正常的数据
        :return:
        """
        encode_result = self.data_text.encode("unicode_escape")
        decode_result = encode_result.decode("utf-8")
        rpl_result = decode_result.replace("\\x", "%").replace("\\n", "").replace("\\t", "").replace("\\", "")
        decoded_data = parse.unquote(rpl_result)
        return decoded_data

    def request(self) -> str:
        """
        请求拿到qq空间动态信息
        但是其中包含乱码数据
        :return:
        """
        res = requests.get(url=self.url, headers=HEADER)
        status_code = res.status_code
        if status_code == 200:
            text_result = res.text.replace("_Callback(", "")[0:-3]
            self.data_text = text_result   # 英文和数字均乱码
        if status_code != 200:
            raise HTTPError
        return self.data_text

    def parse_text(self):
        """
        对拿到的qq空间动态信息
        及其乱码信息进行解析整理
        :return:
        """
        if self.data_text:
            pass
        if not self.data_text:
            raise NoRequestResponse

    def run_to_rid(self):
        pass

    def run(self):
        """多线程调用ToRidKJ"""
        self.run_to_rid()


"""
getACSRFToken: function(url) {
    url = QZFL.util.URI(url);   ->检查url规范的, 可去除

    var skey;
    if (url) {
        if (url.host && url.host.indexOf("qzone.qq.com") > 0) {
            try {
                skey = QZONE.FP._t.QZFL.cookie.get("p_skey");
            } catch (err) {
                skey = QZFL.cookie.get("p_skey");
            }
        } else {
            if (url.host && url.host.indexOf("qq.com") > 0) {
                skey = QZFL.cookie.get("skey");
            }
        }
    }
    if (!skey) {
        skey = QZFL.cookie.get("p_skey") || (QZFL.cookie.get("skey") || (QZFL.cookie.get("rv2") || ""));
    }
        -> 上面一大段代码其实就是在cookie里: 如果p_skey有就用这个, 否则skey, 再否则就rv2

    var hash = 5381;
    for (var i = 0, len = skey.length; i < len; ++i) {
        hash += (hash << 5) + skey.charCodeAt(i);
    }
    return hash & 2147483647;
    }

    最后就是用python来实现一下这个函数即可, 因此也可以解释了为什么g_tk是一天变一次, 因为可能qq空间的cookie失效时间是一天.
"""
