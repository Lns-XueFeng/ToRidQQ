import os.path
import logging
from time import sleep
from datetime import datetime

import uiautomation

from .config import *
from .email import Email
from .internet import Internet
from .compare import CompareImage


class ToRid:
    def __init__(self, name_list):
        if not os.path.exists(RELATIVE_RESULT):
            os.mkdir(RELATIVE_RESULT)

        self.qq_window_name_list = name_list
        self.qq_window_name = None
        # 为每一个需监控的窗口创建其图片文件夹并初始化其new和old的图片
        self.init_new_and_old()

    def init_new_and_old(self):
        for qq_window_name in self.qq_window_name_list:
            if not os.path.exists("./{}".format(qq_window_name)):
                os.mkdir(f"./{qq_window_name}")
                with open("./images/new_pic.png", "rb") as fp:
                    data = fp.read()
                    with open(f"./{qq_window_name}/new_pic.png", "wb") as fp1:
                        fp1.write(data)
                    with open(f"./{qq_window_name}/old_pic.png", "wb") as fp2:
                        fp2.write(data)

    def _compare_two_images(self) -> bool:
        self.compare = CompareImage(
            f"./{self.qq_window_name}/new_pic.png",
            f"./{self.qq_window_name}/old_pic.png",
            self.qq_window_name,
        )
        return self.compare.compare_two_images()

    def _new_to_old(self) -> None:
        return self.compare.new_to_old()

    def _send_qq_email(self) -> bool:
        self.email = Email(self.qq_window_name)
        return self.email.send_qq_email()

    def _check_computer_internet(self) -> bool:
        self.internet = Internet()
        return self.internet.check_computer_internet()

    def _link_school_internet(self) -> int or None:
        return self.internet.link_school_internet()

    def _capture_qq_window(self) -> None:
        """
        调用uiautomation对指定qq窗口进行捕捉截图
        :return:
        """
        qq_box_win = uiautomation.WindowControl(
            searchDepth=1,
            ClassName=WINDOW_CLASS_NAME,
            Name=self.qq_window_name,
        )
        qq_box_sms = qq_box_win.ListControl(Name=WINDOW_NAME)
        if qq_box_win.Exists(5):
            qq_box_win.SetActive()
            qq_box_win.MoveToCenter()
            qq_box_sms.CaptureToImage(f"./{self.qq_window_name}/new_pic.png")

    def _capture_and_match(self) -> str:
        """
        捕捉图片以及对其和前一张捕捉的图片进行相似性比较
        如果图片不同，则判断为新消息，发送邮件
        :return:
        """
        self._capture_qq_window()
        match_result = self._compare_two_images()
        if not match_result:
            logging.info(LOG_INFO_ONE)
            ret = self._send_qq_email()
            self._new_to_old()  # new_image -> old_image
            if ret:
                logging.info(LOG_INFO_TWO)
                logging.info(LOG_INFO_TREE)
                return SEND_SUCCESS
            logging.warning(LOG_WARN_TWO)
            logging.info(LOG_INFO_TREE)
            return SEND_FAILED
        logging.info(LOG_INFO_FOUR)
        logging.info(LOG_INFO_TREE)
        return IMAGES_NOT_EQUAL

    def run_to_rid(self, time=300, name="") -> None:
        """
        主要逻辑函数，对指定窗口进行轮询监控并进行一些意外操作
        :param time: 监控时间
        :param name: QQ窗口名字
        :return:
        """
        logging.basicConfig(
            level=LOG_LEVEL,
            filemode=A_MODE,
            encoding=UTF_8,
            filename=LOG_RESULT_PATH,
        )
        print(PRINT_START if name != TEST else TEST_BEGIN)
        while True:
            logging.info(datetime.now().strftime(TIME_FORMAT))
            computer_internet = self._check_computer_internet()
            if not computer_internet:
                school_link_status = self._link_school_internet()
                if school_link_status != 200:
                    logging.warning(LOG_WARN_TREE)
                    sleep(time)  # 五分钟后重试
                    continue
            for qq_window_name in self.qq_window_name_list:
                self.qq_window_name = qq_window_name   # 更新self.qq_window_name为当前指向window_name
                self._capture_and_match()

            if name == TEST:
                break
            sleep(time)  # 一分钟查看一次
        print(PRINT_END if name != TEST else TEST_FINISHED)
