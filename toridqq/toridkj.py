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
        self._cookie = HEADER["cookie"]
        self._g_tk = self._decrypt_g_tk()
        self._rid = random.random()
        self._time_stamp = time.time()
        self._window_ld = random.random()

        self._url = URL.format(
            self._rid, self._time_stamp, self._window_ld, self._g_tk, self._g_tk)
        self._header = HEADER
        self._data_text = None
        self._parsed_text = None
        self._key = None

    def _decrypt_g_tk(self) -> int:
        """
        rid = random.random()
        time_stamp = time.time()
        window_ld = random.random()
        g_tk是最后一个加密参数, 与cookie相关
        :return:
        """
        key_list = re.findall("p_skey=(.*?);", self._cookie) or re.findall("skey=(.*?);", self._cookie) \
            or re.findall("rv2=(.*?);", self._cookie)
        self.key = key_list

        hash_value = 5381
        if not self.key:
            raise NoKeyValueError
        for i in self.key[0]:
            hash_value += (hash_value << 5) + ord(i)

        return hash_value & 2147483647

    def _to_dict(self) -> str:
        """
        将cookie字符串转为字典形式
        :return:
        """
        new_cookie = "{" + self._cookie.replace("=", ":").replace(";", ",") + "}"
        return new_cookie

    def _get_decode_data(self) -> str:
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

    def _request(self) -> str:
        """
        请求拿到qq空间动态信息
        但是其中包含乱码数据
        :return:
        """
        res = requests.get(url=self._url, headers=HEADER)
        status_code = res.status_code
        if status_code == 200:
            text_result = res.text.replace("_Callback(", "")[0:-3]
            self.data_text = text_result   # 英文和数字均乱码
        if status_code != 200:
            raise HTTPError
        return self.data_text

    def _parse_text(self):
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
