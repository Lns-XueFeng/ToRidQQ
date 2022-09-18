from PIL import Image


class CompareImage:
    def __init__(self):
        self.image_one = Image.open("new_pic.png")
        self.image_two = Image.open("old_pic.png")

    def pixel_equal(self, x, y):
        """
        判断两个像素是否相同
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片像素点
        piex1 = self.image_one.load()[x, y]
        piex2 = self.image_two.load()[x, y]
        threshold = 10
        # 比较每个像素点的RGB值是否在阈值范围内，若两张图片的RGB值都在某一阈值内，则我们认为它的像素点是一样的
        if abs(piex1[0] - piex2[0]) < threshold and \
                abs(piex1[1] - piex2[1]) < threshold and \
                abs(piex1[2] - piex2[2]) < threshold:
            return True
        else:
            return False

    def compare_size(self):
        size_one = self.image_one.size
        size_two = self.image_two.size
        if size_one == size_two:
            return True

    def compare_image(self):
        """
        进行比较
        :param image1:图片1
        :param image2: 图片2
        :return:
        """
        left = 80   # 坐标起始位置
        right_num = 0   # 记录相同像素点个数
        false_num = 0   # 记录不同像素点个数
        all_num = 0   # 记录所有像素点个数
        for i in range(left, self.image_one.size[0]):
            for j in range(self.image_one.size[1]):
                if self.pixel_equal(i, j):
                    right_num += 1
                else:
                    false_num += 1
                all_num += 1
        same_rate = round(right_num / all_num, 3)		# 相同像素点比例
        nosame_rate = round(false_num / all_num, 3)	 # 不同像素点比例
        print("图片相似度: ", str(round(same_rate * 100, 1)) + "%")
        print("图片不相似度: ", str(round(nosame_rate * 100, 1)) + "%")

        return same_rate


if __name__ == "__main__":
    compare = CompareImage()
    if compare.compare_size():
        same_rate = compare.compare_image()
        print(same_rate)
