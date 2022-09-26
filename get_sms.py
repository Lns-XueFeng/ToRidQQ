import logging
from time import sleep
from datetime import datetime

from engine import run
from internet import Internet

from config import *

"""
1.打开QQ -> 2.打开群聊 -> 3.运行脚本 -> 4.确保窗口无遮挡

下一个问题是： 
    如何让此程序更易于使用
        其重要优化步骤在于 1与2
    
解决方案：
    1.最开始, 我是丢到副屏, 且我平时也不关机
    2.接着, 可以将其丢尽虚拟机, 配置一次环境, 只要不关机即可
    3.着眼于将第一步与第二步用程序进行自动化
    
未来可能的扩展：
    命令行方面的支持
    多进程支持多个窗口进行监控
"""


if __name__ == '__main__':
    logging.basicConfig(
        level=LOG_LEVEL,
        filemode=A_MODE,
        encoding=UTF_8,
        filename=LOG_RESULT_PATH,
    )
    print(PRINT_START)
    while True:
        logging.info(datetime.now().strftime(TIME_FORMAT))
        computer_internet = Internet.check_computer_internet()
        if not computer_internet:
            school_link_status = Internet.link_school_internet()
            if school_link_status != 200:
                logging.warning(LOG_WARN_TREE)
                sleep(300)   # 五分钟后重试
                continue
        result = run(name=QQ_WINDOW_NAME)
        if result == 'send success':
            logging.info(LOG_INFO_TWO)
            logging.info(LOG_INFO_TREE)
        if result == 'send failed':
            logging.warning(LOG_WARN_TWO)
            logging.info(LOG_INFO_TREE)
        if result == 'image not equal':
            logging.info(LOG_INFO_FOUR)
            logging.info(LOG_INFO_TREE)
        sleep(60)   # 一分钟查看一次
    print(PRINT_END)
