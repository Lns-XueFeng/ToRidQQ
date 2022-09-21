import logging
from smtplib import SMTP_SSL
from email import encoders, utils
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import uiautomation

from compare import CompareImage
from config import MY_USER, MY_SENDER, MY_PASSWORD


def send_qq(name):
    main_msg = make_email(name)
    try:
        server = SMTP_SSL("smtp.qq.com", 465)
        server.login(MY_SENDER, MY_PASSWORD)
        server.sendmail(MY_SENDER, [MY_USER, ], main_msg.as_string())
        server.quit()
    except Exception as result:
        logging.error(f"发送QQ邮件Error：{result}")
        return False

    return True


def make_email(name):
    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()

    html_msg = MIMEText(
        '<p style="font-size:20px; color:pink;"> 新消息的截图 </p>\
        <p><img src="cid:new_pic.png" /></p>', 'html', 'utf-8'
    )
    main_msg.attach(html_msg)

    main_msg['From'] = 'Lns-XueFeng'
    main_msg['To'] = MY_USER
    main_msg['Subject'] = str(name) + "来消息啦"
    main_msg['Date'] = utils.formatdate()

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open('images/new_pic.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename='images/new_pic.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='images/new_pic.png')
        mime.add_header('Content-ID', '<new_pic.png>')
        mime.add_header('X-Attachment-Id', 'new_pic.png')
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        main_msg.attach(mime)

    return main_msg


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
        logging.warning("可能切换了QQ窗口：进行一次覆盖")
        with open("images/old_pic.png", 'wb') as fp1:
            with open("images/new_pic.png", 'rb') as fp2:
                b_data = fp2.read()
                fp1.write(b_data)
        return False

    if same_rate > 0.99:  # 相似度大于99%认为图片相似
        return True
    else:
        return False


def run(name):
    qq_box_win = uiautomation.WindowControl(
        searchDepth=1,
        ClassName='TXGuiFoundation',
        Name=name,
    )
    qq_box_sms = qq_box_win.ListControl(Name="消息")
    if qq_box_win.Exists(5):
        qq_box_sms.CaptureToImage("images/new_pic.png")

    match_result = compare_images()
    if not match_result:
        logging.info("发现新消息：Send")
        ret = send_qq(name)
        if ret:
            logging.info("邮件发送：Success")
            logging.info("\n")
        else:
            logging.warning("邮件发送：Fail")
            logging.info("\n")
        # 将新图片替换老图片, 以便于下次的比较
        with open("images/old_pic.png", 'wb') as fp1:
            with open("images/new_pic.png", 'rb') as fp2:
                b_data = fp2.read()
                fp1.write(b_data)
    else:
        logging.info("图片相似度大于99%->判定为信息重复：本次不发送邮件提醒")
        logging.info("\n")
