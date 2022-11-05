from .toridqq import ToRidQQ
from .toridkj import ToRidKJ


class ToRid:
    def __init__(self, name_list, time, auto_register):
        self.name_list = name_list
        self.time = time
        self.auto_register = auto_register

    def run_toridqq(self):
        return ToRidQQ(
            self.name_list, self.time, self.auto_register)

    def run_toridkj(self):
        return ToRidKJ()

    def thread_run_torid(self):
        to_rid_qq = self.run_toridqq()
        to_rid_kj = self.run_toridkj()
        to_rid_qq.start()
        to_rid_kj.start()
        to_rid_qq.join()
        to_rid_kj.join()
