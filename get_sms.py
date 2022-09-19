import logging
from time import sleep
from datetime import datetime

from engine import main


"""
原因：
    此脚本是为了满足我不想在手机上下载qq所写一直以来我都觉得QQ的界面越来越臃肿, 
    且随着QQ使用时间的增加各种群各种联系人越来越多, 可是我需要查看的群只有那么一个两个, 
    因此我便萌生了做一个程序帮助我自动检测QQ对应的群是否有新消息了, 
    如果有, 通过QQ邮箱发送给我(我比较喜欢用邮箱), 这样我便不用每天不知不觉的耗费大量时间与精力在QQ上, 
    事实证明我是对的, 在卸载了QQ之后我的手机无比安静, 使得我每天多出非常多的精力与时间来做别的事情
    (注：我手机本身的APP就非常少)
    
使用：
    打开需要获取信息的聊天窗口, 放在桌面上(不要被挡住)
    将此聊天窗口的名字(群昵称或你的好友昵称)填入到main函数的name参数内
    
实现：
    利用uiautomation获取窗口截图
    判断前后图片的相似度
    如果不相似则说明是新消息
    发送邮件到我手机

注意：不可打开多个聊天窗口, 目前一次仅支持一个
可能还需要一个是否链接上校园网的判断, 没有的话就用协议自动链接校园网
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
        main(name='团结的火药桶')
        sleep(60)   # 一分钟查看一次
