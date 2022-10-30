from .toridqq import ToRidQQ
from .toridkj import ToRidKJ


class ToRid:
    def __init__(self, name_list):
        self.name_list = name_list

    def run_toridqq(self, time, auto_register):
        to_rid_qq = ToRidQQ(self.name_list)
        to_rid_qq.run_to_rid(time, auto_register)

    def run_toridkj(self):
        pass
