import unittest
from unittest.mock import MagicMock

from toridqq import ToRid


class TestEngine(unittest.TestCase):
    def test_main(self):
        """
        将整个项目运行一遍 查看result/result.log查看运行情况
        注意：需要将需监控的QQ窗口显示出来, 建议QQ默认窗口尺寸
        """
        to_rid = ToRid()
        # 在测试里面不发送QQ邮件
        to_rid._send_qq_email = MagicMock(return_value=True)
        to_rid.main(name="test")
