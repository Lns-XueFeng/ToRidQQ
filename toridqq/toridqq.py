import os.path
import logging
from time import sleep
from datetime import datetime

import keyboard
import uiautomation

from .config import *
from .email import Email
from .internet import Internet
from .compare import CompareImage
from .utils import WindowNotFindError
from .utils import create_images, new_to_old, exit_program
from .genhtml import GenerateHtml


class ToRidQQ:
    def __init__(self, name_list: list, time=300, auto_register=False):
        if not os.path.exists(RELATIVE_RESULT):
            os.mkdir(RELATIVE_RESULT)

        self._try_link_count = 0
        self._class_name = self.__class__.__name__
        self._qq_window_name_list = name_list
        self._qq_window_name = None   # 指向当前监控窗口名称
        self._init_new_and_old()
        self._time = time   # 控制监控轮询间隔
        self._auto_register = auto_register   # 是否自动校园网登录

    def _init_new_and_old(self) -> None:
        """在类初始化时循环检查是否创建了对应每一个窗口的图片文件夹以及其图片 """
        for qq_window_name in self._qq_window_name_list:
            user_images = SET_USER_IMAGES.format(qq_window_name)
            if not os.path.exists(user_images):
                os.mkdir(user_images)
                create_images(qq_window_name)

    def _new_to_old(self):
        """ new_image -> old_image """
        return new_to_old(self._qq_window_name)

    def _compare_two_images(self) -> bool:
        self.compare = CompareImage(
            USER_NEW_IMAGES.format(self._qq_window_name),
            USER_OLD_IMAGES.format(self._qq_window_name),
            self._qq_window_name,
        )
        return self.compare.compare_two_images()

    def _send_qq_email(self) -> bool:
        return Email(self._qq_window_name).send()

    @staticmethod
    def _link_school_internet(try_link_count) -> int or None:
        return Internet().link_school_internet(try_link_count)

    def _capture_qq_window(self) -> None:
        """ 调用uiautomation对指定qq窗口进行捕捉截图 """
        with uiautomation.UIAutomationInitializerInThread():
            qq_box_win = uiautomation.WindowControl(
                searchDepth=1,
                ClassName=WINDOW_CLASS_NAME,
                Name=self._qq_window_name,
            )
            qq_box_sms = qq_box_win.ListControl(Name=WINDOW_NAME)
            if qq_box_win.Exists(5):
                qq_box_win.SetActive()
                qq_box_win.MoveToCenter()
                qq_box_sms.CaptureToImage(USER_NEW_IMAGES.format(self._qq_window_name))
            else:
                logging.error(LOG_NOT_FIND_WINDOW.format(self._class_name))
                raise WindowNotFindError

    def _capture_and_match(self) -> str:
        """
        捕捉图片以及对其和前一张捕捉的图片进行相似性比较
        如果图片不同，则判断为新消息，发送邮件
        """
        self._capture_qq_window()
        match_result = self._compare_two_images()
        if not match_result:
            ret = self._send_qq_email()
            self._new_to_old()
            if ret:
                return SEND_SUCCESS
            return SEND_FAILED
        return IMAGES_NOT_EQUAL

    def run_to_rid(self, name="") -> None:
        """
        主要逻辑函数，对指定窗口进行轮询监控并进行一些意外操作
        :param name: QQ窗口名字
        """
        exit_warn = PRINT_END if name != TEST else TEST_FINISHED
        keyboard.add_hotkey("esc", exit_program, args=(exit_warn,))
        logging.basicConfig(
            level=LOG_LEVEL,
            filemode=A_MODE,
            encoding=UTF_8,
            filename=LOG_RESULT_PATH,
        )
        print(PRINT_START if name != TEST else TEST_BEGIN)
        while True:
            logging.info(LOG_FORMAT)
            current_time = datetime.now().strftime(TIME_FORMAT)
            logging.info(LOG_RECORD_TIME.format(self._class_name, current_time))
            school_link_status = self._link_school_internet(self._try_link_count)
            if self._auto_register and school_link_status != 200:
                self._try_link_count = school_link_status + 1
                logging.warning(
                    LOG_FAIL_LINK.format(self._class_name, self._try_link_count))
                sleep(self._time)
                continue
            for qq_window_name in self._qq_window_name_list:
                self._qq_window_name = qq_window_name   # 更新self.qq_window_name
                logging.info(LOG_CURRENT_WINDOW.format(self._class_name, self._qq_window_name))
                self._capture_and_match()

            generate = GenerateHtml()
            generate.gen_html_file()

            if name == TEST:
                break
            sleep(self._time)
