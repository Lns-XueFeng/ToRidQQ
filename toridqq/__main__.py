import sys
import argparse

from requests import HTTPError

from .torid import ToRid
from .internet import Internet


parser = argparse.ArgumentParser()
parser.add_argument("name_list", nargs="*", default="团结的火药桶", help="设置将要监控聊天窗口名称")
parser.add_argument("-t", "--time", nargs="?", default=300, help="设置程序监控窗口间隔时间")
parser.add_argument("-o", "--open", action="store_true", help="是否自动打开并登录QQ(为避免读取用户账号密码请设置为自动登录)")
# 默认在程序开始前进行一次计算机网络检查
parser.add_argument("-c", "--check", action="store_true", default=True, help="是否检测计算机网络环境")
# 如果你也是通过校园网联网, 那么可开启, 则每次轮询便会检查一次
parser.add_argument("-r", "--register", action="store_true", help="是否校园网自动协议登录(校园网才可用,修改源代码进行自定义)")
args = parser.parse_args(sys.argv[1:])

to_rid = ToRid(args.name_list)
auto_register = False

# if args.open:
#     to_rid_qq.open_qq()
#     to_rid_qq.register()
#     to_rid_qq.open_window()

if args.check:
    computer = Internet()
    result = computer.check_computer_internet()
    if not result and args.register:
        auto_register = True

if auto_register:
    computer = Internet()
    http_status = computer.link_school_internet(1)
    if http_status != 200:
        raise HTTPError

to_rid.run_toridqq(args.time, auto_register)
