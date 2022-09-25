import unittest
from email import encoders, utils
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from engine import _send_qq_email
from engine import _generate_email
from engine import _compare_two_images


class TestEngine(unittest.TestCase):

    def test_compare_two_images(self):
        result = _compare_two_images(
            "test_images/test_new_pic.png",
            "test_images/test_old_pic.png",
        )
        self.assertTrue(result, True)

    def test_generate_email(self):
        result = _generate_email(
            "test",
            "test_images/test_new_pic.png",
        )
        self.assertTrue(result, True)

    def test_send_qq_email(self):
        pass
