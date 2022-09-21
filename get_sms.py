import logging
from time import sleep
from datetime import datetime

from engine import run
from internet import Internet


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
    多进程支持多个窗口进行监控
"""


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
