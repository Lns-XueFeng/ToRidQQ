from .toridqq import ToRidQQ
from .toridkj import ToRidKJ


class ToRid:
    def __init__(self, name_list, time, auto_register):
        self._name_list = name_list
        self._time = time
        self._auto_register = auto_register

    def run(self):
        toridqq = ToRidQQ(
            self._name_list, self._time, self._auto_register
        )
        toridqq.run_to_rid()
