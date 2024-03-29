import unittest

from toridqq import Email


class TestEmail(unittest.TestCase):

    def test_generate_email(self):
        """测试生成了MIMEMultipart邮件"""
        email = Email("test")
        result = email._generate()
        self.assertEqual(type(result).__name__, "MIMEMultipart")
