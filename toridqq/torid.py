from flask import Flask

from .toridqq import ToRidQQ
from .toridkj import ToRidKJ


class ToRid:
    """
    等能正确处理从空间得到的动态信息后
    便可以将ToRidQQ以及ToRidKJ继承Thread对象
    这样两个需要长时间监控的程序便可以一起工作
    但是对于如何正确的结束还有待商榷
    """
    def __init__(self, name_list, time, auto_register):
        self.name_list = name_list
        self.time = time
        self.auto_register = auto_register
        self.app = Flask(__name__)

    def show_qq_window(self):
        @self.app.route("/")
        def index():
            self.run_toridqq()   # 改为用户触发查寻最新消息
            return "toridqq已启动"
        return index

    def run_flask(self):
        self.app.run(host='0.0.0.0')

    def run_toridqq(self):
        to_rid_qq = ToRidQQ(self.name_list, self.time, self.auto_register)
        to_rid_qq.start()
        to_rid_qq.join()

    def run_toridkj(self):
        to_rid_kj = ToRidKJ()
        to_rid_kj.start()
        to_rid_kj.join()
