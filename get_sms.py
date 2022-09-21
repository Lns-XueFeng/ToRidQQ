import logging
from time import sleep
from datetime import datetime

from engine import run
from internet import Internet


if __name__ == '__main__':
    logging.basicConfig(
        level="INFO",
        filemode="a",
        encoding="utf-8",
        filename="result/results.log",
    )
    print("程序开始监控QQ聊天窗口")
    while True:
        logging.info(datetime.now().strftime("%Y-%m-%d %H:%M"))
        res = Internet.check_internet()
        if not res:
            if Internet.try_link() != 200:
                logging.warning("尝试连接校园网失败...")
                break
            logging.info("计算机网络连接：{}".format(res))
        run(name='团结的火药桶')
        sleep(60)   # 一分钟查看一次
    print("程序结束监控QQ意外退出")
