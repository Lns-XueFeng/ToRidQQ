# -----------------------------用户设置-----------------------------
QQ_EXE_PATH = "F:\\QQ\\Bin\\QQScLauncher.exe"
# 设置你的QQ邮箱账号以及授权码
MY_USER = None
MY_PASSWORD = None   # 这个是需要在QQ邮箱设置界面开启SMTP服务拿到授权码
MY_SENDER = None   # 填QQ邮箱账号即可


# -----------------------------all the py-----------------------------
# 文件相关
RB_MODE = "rb"
WB_MODE = "wb"
IMAGES_PATH = "./images"
MODEL_IMAGE_PATH = "./images/model/new_pic.png"
SET_USER_IMAGES = "./images/{}"
USER_NEW_IMAGES = "./images/{}/new_pic.png"
USER_OLD_IMAGES = "./images/{}/old_pic.png"

# logging 日志需记录的常量
LOG_LEVEL = "INFO"
LOG_RESULT_PATH = "./result/results.log"
LOG_ERROR_ONE = "连接校园网Error："
LOG_WARN_ONE = "可能切换了QQ窗口：进行一次覆盖"
LOG_WARN_TWO = "邮件发送：Fail"
LOG_WARN_TREE = "尝试连接校园网失败..."
LOG_WARN_FOUR = "Try again"
LOG_INFO_ONE = "发现新消息：Send"
LOG_INFO_TWO = "邮件发送：Success"
LOG_INFO_TREE = "\n"
LOG_INFO_FOUR = "图片相似度大于99%->判定为信息重复：本次不发送邮件提醒"
LOG_INGO_FIVE = "成功连接校园网"


# -----------------------------torid.py-----------------------------
# __init__
RELATIVE_IMAGES = "./images"
RELATIVE_RESULT = "./result"

# _capture_qq_window
WINDOW_CLASS_NAME = "TXGuiFoundation"
WINDOW_NAME = "消息"
SEND_SUCCESS = "send success"
SEND_FAILED = "send failed"
IMAGES_NOT_EQUAL = "images not equal"

# run_to_rid
A_MODE = "a"
UTF_8 = "utf-8"
PRINT_START = "程序开始监控QQ聊天窗口"
PRINT_END = "程序结束监控QQ意外退出"
TIME_FORMAT = "%Y-%m-%d %H:%M"
QQ_WINDOW_NAME = "团结的火药桶"
TEST = "test"
TEST_BEGIN = "test begin"
TEST_FINISHED = "test finished"


# -----------------------------email.py-----------------------------
# _generate_email 函数
MY_NAME = "Lns-XueFeng"
EMAIL_SUBJECT = "来消息啦"
FORM, TO, SUBJECT, DATE = "From", "To", "Subject", "Date"
MIME_NAME, MIME_FORMAT = "image", "png"
CONTENT_DISPOSITION, ATTACHMENT = "Content-Disposition", "attachment"
CONTENT_ID, NEW_PIC_CLUE = "Content-ID", "<new_pic.png>"
X_ATTACHMENT_ID, NEW_PIC_PNG = "X-Attachment-Id", "new_pic.png"

# send_qq_email 函数
SMTP_QQ_COM = "smtp.qq.com"
SEND_EMAIL_ERROR = "发送QQ邮件Error："


# -----------------------------compare.py-----------------------------
SAME_RATE = "图片相似度："
NO_SAME_RATE = "图片不相似度："
PERCENT_SIGN = "%"


# -----------------------------internet.py-----------------------------
PING_BAIDU = "ping baidu.com -n 1"
