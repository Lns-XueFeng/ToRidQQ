import argparse
import sys

from .torid import ToRid


parser = argparse.ArgumentParser()
parser.add_argument("name", nargs="?", default="团结的火药桶", help="设置将要监控聊天窗口名称")
parser.add_argument("-t", "--time", nargs="?", default=300, help="设置程序监控窗口间隔时间")
args = parser.parse_args(sys.argv[1:])

# 从参数获取
to_rid_qq = ToRid(args.name)
to_rid_qq.run_to_rid(args.time)
