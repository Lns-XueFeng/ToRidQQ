import unittest

from compare import CompareImage


class TestCompare(unittest.TestCase):

    def test_compare_same_images_size(self):
        """测试验证两张图片的尺寸相等"""
        compare = CompareImage(
            "test_same_images/test_new_pic.png",
            "test_same_images/test_old_pic.png"
        )
        result = compare.compare_images_size()
        self.assertTrue(result, True)

    def test_compare_no_same_image_size(self):
        """测试验证两张图片的尺寸不相等"""
        compare = CompareImage(
            "test_size_images/test_new_pic.png",
            "test_size_images/test_old_pic.png"
        )
        result = compare.compare_images_size()
        self.assertFalse(result, False)

    def test_compare_two_same_images(self):
        """测试验证两张图片相似"""
        compare = CompareImage(
            "test_same_images/test_new_pic.png",
            "test_same_images/test_old_pic.png"
        )
        result = compare.compare_two_images()
        self.assertEqual(result, 1.0)

    def test_compare_two_no_same_images(self):
        """测试验证两张图片不相似"""
        compare = CompareImage(
            "test_nosame_images/test_new_pic.png",
            "test_nosame_images/test_old_pic.png"
        )
        result = compare.compare_two_images()
        self.assertNotEqual(result, 1.0)
