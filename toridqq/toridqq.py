import subprocess

import pyautogui

from .torid import ToRid


class ToRidQQ(ToRid):
    def __init__(self, name):
        super(ToRidQQ, self).__init__(name)

    def open_qq(self):
        subprocess.Popen(["F:\QQ\Bin\QQScLauncher.exe"])

    def register(self):
        pass

    def open_window(self):
        pass
