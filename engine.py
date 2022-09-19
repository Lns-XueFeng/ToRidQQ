import logging
from time import sleep
from email import encoders, utils
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

import uiautomation as auto
from compare import CompareImage


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
    with open('images/new_pic.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename='images/old_pic.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='images/old_pic.png')
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


def compare_images():
    """
    比较图片是否相同：
    :return True -> 图片相同   False -> 图片不同

    可能还缺判断图片相似度极低的情况下判断是不是捕获到的不是聊天窗口
    """
    compare = CompareImage()
    same_rate = compare.compare_image()

    if not compare.compare_size():  # 如果两张图片大小就不一样可认定图片不同
        # 造成大小不一样可能原因之一：换了获取信息的窗口, 所以需要覆盖一次图片
        logging.warning("可能切换了QQ窗口, 进行一次覆盖")
        with open("images/old_pic.png", 'wb') as fp1:
            with open("images/new_pic.png", 'rb') as fp2:
                b_data = fp2.read()
                fp1.write(b_data)
        return False

    if same_rate > 0.99:  # 相似度大于99%认为图片相似
        return True
    else:
        return False


def main(name):
    qq_box_win = auto.WindowControl(searchDepth=1, ClassName='TXGuiFoundation',
                                    Name=name)
    qq_box_mess = qq_box_win.ListControl(Name="消息")
    if qq_box_win.Exists(5):
        qq_box_mess.CaptureToImage("images/new_pic.png")

    sleep(0.5)
    match_result = compare_images()
    if not match_result:
        logging.info("发现新消息：发送邮件")
        ret = send_qq(name)
        if ret:
            logging.info("邮件发送成功")
            logging.info("\n")
        else:
            logging.warning("邮件发送失败")
            logging.info("\n")
        # 将新图片替换老图片, 以便于下次的比较
        with open("images/old_pic.png", 'wb') as fp1:
            with open("images/new_pic.png", 'rb') as fp2:
                b_data = fp2.read()
                fp1.write(b_data)
    else:
        logging.info("图片相同 ->判断为信息重复：本次不发送邮件提醒")
        logging.info("\n")
