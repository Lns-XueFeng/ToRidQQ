import os.path
import logging
from time import sleep
from datetime import datetime

import uiautomation

from .config import *
from .internet import Internet
from .compare import CompareImage
from .email import Email


class ToRid:
    def __init__(self):
        if not os.path.exists("./images"):
            os.mkdir("./images")
        if not os.path.exists("./result"):
            os.mkdir("./result")

        self.name = QQ_WINDOW_NAME
        self.internet = Internet()
        self.email = Email(self.name)
        self.compare = CompareImage(NEW_IMAGE_PATH, OLD_IMAGE_PATH)

    def _capture_qq_window(self, new_image_path: str):
        qq_box_win = uiautomation.WindowControl(
            searchDepth=1,
            ClassName=WINDOW_CLASS_NAME,
            Name=self.name,
        )
        qq_box_sms = qq_box_win.ListControl(Name=WINDOW_NAME)
        if qq_box_win.Exists(5):
            qq_box_sms.CaptureToImage(new_image_path)

    @classmethod
    def new_to_old(cls) -> None:
        with open(OLD_IMAGE_PATH, WB_MODE) as old:
            with open(NEW_IMAGE_PATH, RB_MODE) as new:
                new_image_bytes = new.read()
                old.write(new_image_bytes)

    def run(self):
        self._capture_qq_window(NEW_IMAGE_PATH)
        match_result = self.compare.compare_two_images()
        if not match_result:
            logging.info(LOG_INFO_ONE)
            ret = self.email.send_qq_email()
            ToRid.new_to_old()  # new_image -> old_image
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

    def main(self):
        logging.basicConfig(
            level=LOG_LEVEL,
            filemode=A_MODE,
            encoding=UTF_8,
            filename=LOG_RESULT_PATH,
        )
        print(PRINT_START)
        while True:
            logging.info(datetime.now().strftime(TIME_FORMAT))
            computer_internet = self.internet.check_computer_internet()
            if not computer_internet:
                school_link_status = self.internet.link_school_internet()
                if school_link_status != 200:
                    logging.warning(LOG_WARN_TREE)
                    sleep(300)  # 五分钟后重试
                    continue
            self.run()
            sleep(60)  # 一分钟查看一次
        print(PRINT_END)
