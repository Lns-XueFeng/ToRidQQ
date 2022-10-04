from toridqq import ToRid


"""
1.打开QQ -> 2.打开群聊 -> 3.运行脚本 -> 4.确保窗口无遮挡

下一个问题是： 
    如何让此程序更易于使用
        其重要优化步骤在于 1与2
    
解决方案：
    1.最开始, 我是丢到副屏, 且我平时也不关机
    2.接着, 可以将其丢尽虚拟机, 配置一次环境, 只要不关机即可
    3.着眼于将第一步与第二步用程序进行自动化
        subprocess打开qq并登录 -> uiautomation打开监控窗口 -> 运行脚本进行监控 -> 确保窗口始终是激活的(Top window)
    
未来可能的扩展：
    命令行方面的支持
        必选参数  QQ窗口名称 默认团结的火药桶
        可选参数  参数设置监控间隔时常 默认间隔300s
        可选参数  是否自动打开QQ、登录QQ、监控QQ相应窗口
        可选参数  是否先检测机器网络环境
        可选参数  是否自动登录学校校园网(协议)
        可选参数  是否需要监控多个QQ消息窗口
    多进程支持多个窗口进行监控
"""


if __name__ == "__main__":
    to_rid_qq = ToRid("团结的火药桶")
    to_rid_qq.run_to_rid()