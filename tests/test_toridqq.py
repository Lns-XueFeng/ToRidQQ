import unittest
from unittest.mock import MagicMock

from toridqq import ToRidQQ


class TestToRidQQ(unittest.TestCase):
    @unittest.skip
    def test_capture_qq_window(self):
        to_rid = ToRidQQ(["团结的火药桶"])
        to_rid._capture_qq_window()

    def test_run_image_not_equal(self):
        """测试当图片相似时程序不发送邮件"""
        to_rid = ToRidQQ(["团结的火药桶"])
        to_rid._compare_two_images = MagicMock(return_value=True)
        to_rid._capture_qq_window = MagicMock(return_value=None)
        result = to_rid._capture_and_match()
        self.assertEqual(result, 'images not equal')

    def test_run_send_success(self):
        """测试当图片不相似, 成功发送邮件"""
        to_rid = ToRidQQ(["团结的火药桶"])
        to_rid._compare_two_images = MagicMock(return_value=False)
        to_rid._capture_qq_window = MagicMock(return_value=None)
        to_rid._send_qq_email = MagicMock(return_value=True)
        to_rid._new_to_old = MagicMock(return_value=None)
        result = to_rid._capture_and_match()
        self.assertEqual(result, 'send success')

    def test_run_send_failed(self):
        """测试当图片不相似, 但发送邮件失败"""
        to_rid = ToRidQQ(["团结的火药桶"])
        to_rid._compare_two_images = MagicMock(return_value=False)
        to_rid._capture_qq_window = MagicMock(return_value=None)
        to_rid._send_qq_email = MagicMock(return_value=False)
        to_rid._new_to_old = MagicMock(return_value=None)
        result = to_rid._capture_and_match()
        self.assertEqual(result, 'send failed')
