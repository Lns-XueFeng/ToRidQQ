import os
from unittest import TestCase

from toridqq import GenerateHtml


class TestGenHtml(TestCase):

    def test_genhtml_is_true(self):
        """测试是否生成了html字符串"""
        gen_html = GenerateHtml()
        html_string = gen_html._get_html()
        self.assertEqual(html_string, str)

    def test_verify_html_file(self):
        """测试是否生成了html文件"""
        gen_html = GenerateHtml()
        gen_html.gen_html_file()
        exist = False
        if os.path.exists("./template_html.html"):
            exist = True
        self.assertTrue(exist)
