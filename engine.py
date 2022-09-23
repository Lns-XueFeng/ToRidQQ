import logging
from smtplib import SMTP_SSL
from email import encoders, utils
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

import uiautomation

from config import *
from compare import CompareImage
from key import MY_USER, MY_SENDER, MY_PASSWORD


def _new_to_old():
    with open(OLD_IMAGE_PATH, WB_MODE) as fp1:
        with open(NEW_IMAGE_PATH, RB_MODE) as fp2:
            b_data = fp2.read()
            fp1.write(b_data)


def _send_qq_email(name):
    main_msg = _generate_email(name)
    try:
        server = SMTP_SSL(SMTP_QQ_COM, 465)
        server.login(MY_SENDER, MY_PASSWORD)
        server.sendmail(MY_SENDER, [MY_USER, ], main_msg.as_string())
        server.quit()
    except Exception as result:
        logging.error(f"{SEND_EMAIL_ERROR}{result}")
        return False

    return True


def _generate_email(name):
    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()
    html_msg = MIMEText('<p style="font-size:20px; color:pink;"> 新消息的截图 </p>'
                        '<p><img src="cid:new_pic.png" /></p>', 'html', 'utf-8')
    main_msg.attach(html_msg)

    main_msg[FORM] = MY_NAME
    main_msg[TO] = MY_USER
    main_msg[SUBJECT] = str(name) + EMAIL_SUBJECT
    main_msg[DATE] = utils.formatdate()

    # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
    with open(NEW_IMAGE_PATH, RB_MODE) as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase(MIME_NAME, MIME_FORMAT, filename=NEW_IMAGE_PATH)
        # 加上必要的头信息:
        mime.add_header(CONTENT_DISPOSITION, ATTACHMENT, filename=NEW_IMAGE_PATH)
        mime.add_header(CONTENT_ID, NEW_PIC_CLUE)
        mime.add_header(X_ATTACHMENT_ID, NEW_PIC_PNG)
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        main_msg.attach(mime)

    return main_msg


def _compare_two_images():
    """
    比较图片是否相同：
    :return True -> 图片相同   False -> 图片不同

    可能还缺判断图片相似度极低的情况下判断是不是捕获到的不是聊天窗口
    """
    compare = CompareImage(NEW_IMAGE_PATH, OLD_IMAGE_PATH)
    same_rate = compare.compare_two_images()

    if not compare.compare_images_size():  # 如果两张图片大小就不一样可认定图片不同
        # 造成大小不一样可能原因之一：换了获取信息的窗口, 所以需要覆盖一次图片
        logging.warning(LOG_WARN_ONE)
        # 将新图片替换老图片
        _new_to_old()
        return False

    if same_rate > 0.99:  # 相似度大于99%认为图片相似
        return True
    else:
        return False


def run(name):
    qq_box_win = uiautomation.WindowControl(
        searchDepth=1,
        ClassName=WINDOW_CLASS_NAME,
        Name=name,
    )
    qq_box_sms = qq_box_win.ListControl(Name=WINDOW_NAME)
    if qq_box_win.Exists(5):
        qq_box_sms.CaptureToImage(NEW_IMAGE_PATH)

    match_result = _compare_two_images()
    if not match_result:
        logging.info(LOG_INFO_ONE)
        ret = _send_qq_email(name)
        if ret:
            logging.info(LOG_INFO_TWO)
            logging.info(LOG_INFO_TREE)
        else:
            logging.warning(LOG_WARN_TWO)
            logging.info(LOG_INFO_TREE)
        # 将新图片替换老图片, 以便于下次的比较
        _new_to_old()
    else:
        logging.info(LOG_INFO_FOUR)
        logging.info(LOG_INFO_TREE)
