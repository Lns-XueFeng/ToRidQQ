import sys
import argparse

from requests import HTTPError

from .toridqq import ToRidQQ
from .internet import Internet


parser = argparse.ArgumentParser()
parser.add_argument("name", nargs="?", default="团结的火药桶", help="设置将要监控聊天窗口名称")
parser.add_argument("-t", "--time", nargs="?", default=300, help="设置程序监控窗口间隔时间")
parser.add_argument("-o", "--open", action="store_true", help="是否自动打开并登录QQ")
# 默认在程序开始前进行一次网络检查, 注：运行时每次轮询亦会检测网络情况
parser.add_argument("-c", "--check", action="store_true", default=True, help="是否检测计算机网络环境")
parser.add_argument("-r", "--register", action="store_true", help="是否校园网自动协议登录(校园网才可用,修改源代码进行自定义)")
args = parser.parse_args(sys.argv[1:])

# 从参数获取
to_rid_qq = ToRidQQ(args.name)

if args.open:
    to_rid_qq.open_qq()
    to_rid_qq.register()
    to_rid_qq.open_window()

if args.check:
    computer = Internet()
    result = computer.check_computer_internet()
    if not result:
        args.register = True

if args.register:
    computer = Internet()
    http_status = computer.link_school_internet()
    if http_status != 200:
        raise HTTPError

to_rid_qq.run_to_rid(args.time)
