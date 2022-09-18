from time import sleep
from email import encoders, utils
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

import uiautomation as auto
from compare import CompareImage


"""
原因：
    此脚本是为了满足我不想在手机上下载qq所写一直以来我都觉得QQ的界面越来越臃肿, 且随着QQ使用时间的增加各种群各种联系人越来越多, 
    可是我需要查看的群只有那么一个两个, 因此我便萌生了做一个程序帮助我自动检测QQ对应的群是否有新消息了, 
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

可能还需要一个是否链接上校园网的判断, 没有的话就用协议自动链接校园网
"""


def send_qq(name):
    my_sender = '1477792904@qq.com'
    my_pass = 'ctohgjxfvcrufjef'
    my_user = '1477792904@qq.com'
    ret = True

    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()

    html_msg = MIMEText(
        '<p style="font-size:20px; color:pink;"> 新消息的截图 </p>\
        <p><img src="cid:0" /></p>', 'html', 'utf-8'
    )
    main_msg.attach(html_msg)

    main_msg['From'] = 'Lns-XueFeng'
    main_msg['To'] = my_user
    main_msg['Subject'] = str(name) + "来消息啦"
    main_msg['Date'] = utils.formatdate()

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('old_pic.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename='old_pic.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='old_pic.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        main_msg.attach(mime)

    try:
        server = SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user, ], main_msg.as_string())
        server.quit()

    except Exception:
        ret = False

    return ret


def compare_images(path_one, path_two):
    """
    比较图片是否相同：
    :return True -> 图片相同   False -> 图片不同

    可能还缺判断图片相似度极低的情况下判断是不是捕获到的不是聊天窗口
    """
    compare = CompareImage()
    same_rate = compare.compare_image()

    if not compare.compare_size():   # 如果两张图片大小就不一样可认定图片不同
        # 造成大小不一样可能原因之一：换了获取信息的窗口, 所以需要覆盖一次图片
        print("可能切换了QQ窗口, 进行一次覆盖")
        with open("old_pic.png", 'wb') as fp1:
            with open("new_pic.png", 'rb') as fp2:
                b_data = fp2.read()
                fp1.write(b_data)
        return False

    if same_rate > 0.99:   # 相似度大于99%认为图片相似
        return True
    else:
        return False


def main(name):
    qq_box_win = auto.WindowControl(searchDepth=1, ClassName='TXGuiFoundation',
                                    Name=name)
    qq_box_mess = qq_box_win.ListControl(Name="消息")
    if qq_box_win.Exists(5):
        qq_box_mess.CaptureToImage("new_pic.png")

    match_result = compare_images("new_pic.png", "old_pic.png")
    if not match_result:
        print("发现新消息：发送邮件")
        ret = send_qq(name)
        if ret:
            print("邮件发送成功")
        else:
            print("邮件发送失败")
        # 将新图片替换老图片, 以便于下次的比较
        with open("old_pic.png", 'wb') as fp1:
            with open("old_pic.png", 'rb') as fp2:
                b_data = fp2.read()
                fp1.write(b_data)
    else:
        print("图片相同 ->判断为信息重复：本次不发送邮件提醒")


if __name__ == '__main__':
    while True:
        main(name='弹药20级6班')
        sleep(60)   # 1分钟查看一次
