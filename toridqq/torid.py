from .toridqq import ToRidQQ
from .toridkj import ToRidKJ


class ToRid:
    """
    等能正确处理从空间得到的动态信息后
    便可以将ToRidQQ以及ToRidKJ继承Thread对象
    这样两个需要长时间监控的程序便可以一起工作
    但是对于如何正确的结束还有待商榷
    """
    def __init__(self, name_list):
        self.name_list = name_list

    def run_toridqq(self, time, auto_register):
        to_rid_qq = ToRidQQ(self.name_list)
        to_rid_qq.run_to_rid(time, auto_register)

    def run_toridkj(self):
        to_rid_kj = ToRidKJ()
        to_rid_kj.run_to_rid()
