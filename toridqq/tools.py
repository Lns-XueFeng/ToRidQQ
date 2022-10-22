from config import *


def create_images(qq_window_name: str) -> None:
    """
    创建用户生成截图文件夹
    :param qq_window_name: 监控窗口名称
    :return:
    """
    with open(MODEL_IMAGE_PATH, RB_MODE) as fp:
        data = fp.read()
        with open(USER_NEW_IMAGES.format(qq_window_name), WB_MODE) as fp1:
            fp1.write(data)
        with open(USER_OLD_IMAGES.format(qq_window_name), WB_MODE) as fp2:
            fp2.write(data)


def new_to_old(qq_window_name: str) -> None:
    with open(USER_OLD_IMAGES.format(qq_window_name), WB_MODE) as old:
        with open(USER_NEW_IMAGES.format(qq_window_name), RB_MODE) as new:
            new_image_bytes = new.read()
            old.write(new_image_bytes)


def torid_logging(func):
    """
    装饰函数为其增加日志记录功能
    :return:
    """
    pass
