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
    def __init__(self, name):
        if not os.path.exists("./images"):
            os.mkdir("./images")
        if not os.path.exists("./result"):
            os.mkdir("./result")

        self.qq_window_name = name

    def _compare_two_images(self):
        self.compare = CompareImage(
            NEW_IMAGE_PATH,
            OLD_IMAGE_PATH
        )
        return self.compare.compare_two_images()

    def _new_to_old(self):
        return self.compare.new_to_old()

    def _send_qq_email(self):
        self.email = Email(self.qq_window_name)
        return self.email.send_qq_email()

    def _check_computer_internet(self):
        self.internet = Internet()
        return self.internet.check_computer_internet()

    def _link_school_internet(self):
        return self.internet.link_school_internet()

    def _capture_qq_window(self, new_image_path: str):
        qq_box_win = uiautomation.WindowControl(
            searchDepth=1,
            ClassName=WINDOW_CLASS_NAME,
            Name=self.qq_window_name,
        )
        qq_box_sms = qq_box_win.ListControl(Name=WINDOW_NAME)
        if qq_box_win.Exists(5):
            qq_box_sms.CaptureToImage(new_image_path)

    def _capture_and_match(self):
        self._capture_qq_window(NEW_IMAGE_PATH)
        match_result = self._compare_two_images()
        if not match_result:
            logging.info(LOG_INFO_ONE)
            ret = self._send_qq_email()
            self._new_to_old()  # new_image -> old_image
            if ret:
                logging.info(LOG_INFO_TWO)
                logging.info(LOG_INFO_TREE)
                return 'send success'
            logging.warning(LOG_WARN_TWO)
            logging.info(LOG_INFO_TREE)
            return 'send failed'
        logging.info(LOG_INFO_FOUR)
        logging.info(LOG_INFO_TREE)
        return 'image not equal'

    def run_to_rid(self, time=300, name=""):
        logging.basicConfig(
            level=LOG_LEVEL,
            filemode=A_MODE,
            encoding=UTF_8,
            filename=LOG_RESULT_PATH,
        )
        print(PRINT_START if name != "test" else "测试开始")
        while True:
            logging.info(datetime.now().strftime(TIME_FORMAT))
            computer_internet = self._check_computer_internet()
            if not computer_internet:
                school_link_status = self._link_school_internet()
                if school_link_status != 200:
                    logging.warning(LOG_WARN_TREE)
                    sleep(time)  # 五分钟后重试
                    continue
            self._capture_and_match()
            if name == "test":
                break
            sleep(60)  # 一分钟查看一次
        print(PRINT_END if name != "test" else "测试完成")
