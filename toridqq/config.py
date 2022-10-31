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
LOG_FORMAT = "\n"
LOG_RESULT_PATH = "./result/results.log"
LOG_RECORD_TIME = "<{}：{}>"
LOG_CURRENT_WINDOW = "<{}：当前监控{}>"
LOG_FAIL_LINK = "<{}：尝试连接校园网失败{}次>"
LOG_NOT_FIND_WINDOW = "<{}：未找到应监控窗口>"
LOG_SEND_SUCCESS = "<{}：新消息邮件发送成功>"
LOG_MABEY_TOOGLE = "<{}：可能切换窗口, 进行覆盖>"
LOG_NOT_SEND = "<{}：判定为无新消息(not send)>"
LOG_SEND = "<{}：判定为新消息(send)>"
LOG_EMAIL_ERROR = "<{}：邮件发送失败, {}>"


# -----------------------------toridqq.py-----------------------------
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
PRINT_START = "程序开始监控QQ窗口"
PRINT_END = "程序结束监控正常退出"
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
SEND_EMAIL_ERROR = "邮件发送失败"


# -----------------------------compare.py-----------------------------
SAME_RATE = "图片相似度："
NO_SAME_RATE = "图片不相似度："
PERCENT_SIGN = "%"


# -----------------------------internet.py-----------------------------
PING_BAIDU = "ping baidu.com -n 1"


# -----------------------------toridkj.py-----------------------------
URL = "https://user.qzone.qq.com/proxy/domain/ic2.qzone.qq.com/cgi-bin/feeds/feeds3_html_more?" \
    "uin=1477792904&scope=0&view=1&daylist=&uinlist=&gid=&flag=1&filter=all&applist=all" \
    "&refresh=0&aisortEndTime=0&aisortOffset=0&getAisort=0&aisortBeginTime=0" \
    "&pagenum=1&externparam=&firstGetGroup=0&icServerTime=0&mixnocache=0&scene=0&begintime=0" \
    "&count=10&dayspac=0&sidomain=qzonestyle.gtimg.cn&useutf8=1&outputhtmlfeed=1&rd={}" \
    "&usertime={}&windowId={}&getob=1&g_tk={}&g_tk={}"

HEADER = {
    "accept-encoding": "gzip, deflate, br",
    # 此cookie时效一天左右, 也就是解决了自动化获取cookie即可实现一直获取信息,
    # 第一种方法是使用selenium进行模拟登录(过于麻烦, 还需要choromedriver)
    # 第二种用协议：但逆向难度估计不小
    "cookie": "iip=0; pgv_pvid=6430652910; LW_uid=s1z6E5B8J6s4K4Y1c6M5Y418S8; eas_sid=q1a6451866l4x4C1d6a5K6q6A2; RK=h/FYX5lwSr; ptcz=d295ed152e18c4b960133810a016725162fff82e6bfc425131e4c9cd6c4a4dcc; ied_qq=o1477792904; uin_cookie=o1477792904; tvfe_boss_uuid=960620ff139b1538; o_cookie=1477792904; pac_uid=1_1477792904; LW_sid=S1r6a6F3i3J3n7k2Y1k1U0j1C6; logTrackKey=dd2f9804e349413ab75fbca26ba3913b; _clck=3898611844|1|f5x|0; qz_screen=1920x1080; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0; ptui_loginuin=1477792904; __Q_w_s__QZN_TodoMsgCnt=1; pgv_info=ssid=s8933187755; vversion_name=8.2.95; video_omgid=2f8042dba619443f; _qpsvr_localtk=0.07045077453807802; uin=o1477792904; skey=@0UsgjmP8k; p_uin=o1477792904; pt4_token=jvOZJxoGa8jtV4Ikf1lUfmw9yJBB2UNK*6kSuKpFWdA_; p_skey=QujlBX1KRg7IFVyhR0hRFZgaZA4urJyF4qB5sy4TMmU_; Loading=Yes; 1477792904_todaycount=0; 1477792904_totalcount=5659",
    "referer": "https://user.qzone.qq.com/1477792904",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.24"
}
