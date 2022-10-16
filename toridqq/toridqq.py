import subprocess

from .torid import ToRid

from .config import QQ_EXE_PATH


class ToRidQQ(ToRid):
    def __init__(self, name):
        super(ToRidQQ, self).__init__(name)

    def open_qq(self):
        subprocess.Popen([QQ_EXE_PATH])

    def register(self):
        pass

    def open_window(self):
        pass

    def monitor_window(self):
        pass
