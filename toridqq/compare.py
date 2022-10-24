import logging

from PIL import Image

from .config import *
from .utils import new_to_old


class CompareImage:
    def __init__(self, new_image_path: str, old_image_path: str, qq_window_name):
        self._image_one = Image.open(new_image_path)
        self._image_two = Image.open(old_image_path)
        self.qq_window_name = qq_window_name

        self.class_name = self.__class__.__name__

    def _compare_two_pixel(self, x: int, y: int) -> bool:
        """
        判断两个像素是否相同
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片像素点
        piex1 = self._image_one.load()[x, y]
        piex2 = self._image_two.load()[x, y]

        # 比较每个像素点的RGB值是否在阈值范围内，
        # 若两张图片的RGB值都在规定范围内，则我们认为它的像素点是一样的
        threshold = 10
        compare1 = abs(piex1[0] - piex2[0]) < threshold
        compare2 = abs(piex1[1] - piex2[1]) < threshold
        compare3 = abs(piex1[2] - piex2[2]) < threshold
        if compare1 and compare2 and compare3:
            return True
        return False

    def _compare_images_size(self) -> bool:
        """
        比较两个图片的尺寸是否相等
        :if 相等 return True
        :else return False
        """
        size_one = self._image_one.size
        size_two = self._image_two.size
        if size_one == size_two:
            return True
        return False

    def _count_two_images_rate(self) -> float:
        """
        将俩图片进行比较
        :return: same_rate 图片相似度
        """
        left = 80   # 坐标起始位置
        right_num = 0   # 记录相同像素点个数
        false_num = 0   # 记录不同像素点个数
        all_num = 0   # 记录所有像素点个数
        for i in range(left, self._image_one.size[0]):
            for j in range(self._image_one.size[1]):
                if self._compare_two_pixel(i, j):
                    right_num += 1
                else:
                    false_num += 1
                all_num += 1
        same_rate = round(right_num / all_num, 3)
        no_same_rate = round(false_num / all_num, 3)
        logging.info(f"<{self.class_name}：{SAME_RATE}{str(round(same_rate * 100, 1))}{PERCENT_SIGN}>")
        logging.info(f"<{self.class_name}：{NO_SAME_RATE}{str(round(no_same_rate * 100, 1))}{PERCENT_SIGN}>")

        return same_rate

    def compare_two_images(self) -> bool:
        """
        比较图片是否相同：
        :return True -> 图片相同   False -> 图片不同

        可能还缺判断图片相似度极低的情况下判断是不是捕获到的不是聊天窗口
        """
        if not self._compare_images_size():   # 如果两张图片大小就不一样可认定图片不同
            # 造成大小不一样可能原因之一：换了获取信息的窗口, 所以需要覆盖一次图片
            logging.warning(LOG_MABEY_TOOGLE.format(self.class_name))
            new_to_old(self.qq_window_name)   # new_image -> old_image
            return False

        same_rate = self._count_two_images_rate()
        if same_rate > 0.99:  # 相似度大于99%认为图片相似
            logging.info(LOG_NOT_SEND.format(self.class_name))
            return True
        else:
            logging.info(LOG_SEND.format(self.class_name))
            return False
