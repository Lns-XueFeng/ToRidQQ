import unittest

from compare import CompareImage


NEW_IMAGE_PATH = "test_images/test_new_pic.png"
OLD_IMAGE_PATH = "test_images/test_old_pic.png"


class TestCompare(unittest.TestCase):

    compare = CompareImage(NEW_IMAGE_PATH, OLD_IMAGE_PATH)

    def test_compare_images_size(self):
        result = TestCompare.compare.compare_images_size()
        self.assertTrue(result, True)

    def test_compare_two_images(self):
        result = TestCompare.compare.compare_two_images()
        self.assertEqual(result, 1.0)
