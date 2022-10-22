import subprocess

from .torid import ToRid

from .config import QQ_EXE_PATH


class ToRidQQ(ToRid):
    def __init__(self, name_list: list):
        super(ToRidQQ, self).__init__(name_list)

    def open_qq(self):
        subprocess.Popen([QQ_EXE_PATH])

    def register(self):
        pass

    def open_window(self):
        pass

    def monitor_window(self):
        pass
