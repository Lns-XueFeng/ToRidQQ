import logging
from smtplib import SMTP_SSL
from email import encoders, utils
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from .config import *
from .key import MY_USER, MY_PASSWORD, MY_SENDER


class Email:
    def __init__(self, name: str):
        self.name = name

    def _generate_email(self, new_image_path: str) -> MIMEMultipart:
        # 构造MIMEMultipart对象做为根容器
        main_msg = MIMEMultipart()
        html_msg = MIMEText('<p style="font-size:20px; color:pink;"> 新消息的截图 </p>'
                            '<p><img src="cid:new_pic.png" /></p>', 'html', 'utf-8')
        main_msg.attach(html_msg)

        main_msg[FORM] = MY_NAME
        main_msg[TO] = MY_USER
        main_msg[SUBJECT] = self.name + EMAIL_SUBJECT
        main_msg[DATE] = utils.formatdate()

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open(new_image_path, RB_MODE) as f:
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

    def send_qq_email(self) -> bool:
        main_msg = self._generate_email(NEW_IMAGE_PATH)
        try:
            server = SMTP_SSL(SMTP_QQ_COM, 465)
            server.login(MY_SENDER, MY_PASSWORD)
            server.sendmail(MY_SENDER, [MY_USER, ], main_msg.as_string())
            server.quit()
        except Exception as result:
            logging.error(f"{SEND_EMAIL_ERROR}{result}")
            return False
        return True
