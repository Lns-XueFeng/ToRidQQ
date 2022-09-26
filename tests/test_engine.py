import unittest
from unittest.mock import MagicMock
from email import encoders, utils
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import engine


class TestEngine(unittest.TestCase):

    def test_compare_two_same_images(self):
        """测试验证两张图片相似"""
        result = engine._compare_two_images(
            "test_same_images/test_new_pic.png",
            "test_same_images/test_old_pic.png",
        )
        self.assertTrue(result, True)

    def test_compare_two_no_same_images(self):
        """测试验证两张图片不相似"""
        result = engine._compare_two_images(
            "test_nosame_images/test_new_pic.png",
            "test_nosame_images/test_old_pic.png",
        )
        self.assertFalse(result, False)

    def test_compare_two_nosame_size_images(self):
        """测试验证两张图片尺寸不相等"""
        engine._new_to_old = MagicMock(return_value=None)
        result = engine._compare_two_images(
            "test_size_images/test_new_pic.png",
            "test_size_images/test_old_pic.png",
        )
        self.assertFalse(result, False)

    def test_compare_two_same_size_images(self):
        """测试验证两张图片尺寸相等"""
        engine._new_to_old = MagicMock(return_value=None)
        result = engine._compare_two_images(
            "test_same_images/test_new_pic.png",
            "test_same_images/test_old_pic.png",
        )
        self.assertTrue(result, True)

    def test_generate_email(self):
        """测试生成了MIMEMultipart邮件"""
        result = engine._generate_email(
            "test",
            "test_same_images/test_new_pic.png",
        )
        self.assertEqual(type(result).__name__, "MIMEMultipart")

    def test_run_image_not_equal(self):
        """测试当图片相似时程序不发送邮件"""
        engine._compare_two_images = MagicMock(return_value=True)
        engine._capture_qq_window = MagicMock(return_value=None)
        result = engine.run(name="test")
        self.assertEqual(result, 'image not equal')

    def test_run_send_success(self):
        """测试当图片不相似, 成功发送邮件"""
        engine._compare_two_images = MagicMock(return_value=False)
        engine._capture_qq_window = MagicMock(return_value=None)
        engine._send_qq_email = MagicMock(return_value=True)
        engine._new_to_old = MagicMock(return_value=None)
        result = engine.run(name="test")
        self.assertEqual(result, 'send success')

    def test_run_send_failed(self):
        """测试当图片不相似, 但发送邮件失败"""
        engine._compare_two_images = MagicMock(return_value=False)
        engine._capture_qq_window = MagicMock(return_value=None)
        engine._send_qq_email = MagicMock(return_value=False)
        engine._new_to_old = MagicMock(return_value=None)
        result = engine.run(name="test")
        self.assertEqual(result, 'send failed')
