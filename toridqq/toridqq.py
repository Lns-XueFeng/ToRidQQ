import subprocess

from .torid import ToRid


class ToRidQQ(ToRid):
    def __init__(self, name):
        super(ToRidQQ, self).__init__(name)

    def open_qq(self):
        # subprocess.Popen(["F:\QQ\Bin\QQScLauncher.exe"])
        pass

    def register(self):
        pass

    def open_window(self):
        pass
