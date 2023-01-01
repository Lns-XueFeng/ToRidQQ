from toridqq import ToRidQQ


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
    支持监控多个窗口   已完成
    
    本程序核心为ToRidQQ, 为了摆脱QQ, 那么程序的功能便可围绕着这个主题进行扩展开发
        下一个可考虑的点是 “QQ空间”  开始扩展的话代码结构即可再次改变,
        ToRid 修改为 ToRidQQ, 现在的ToRidQQ可变为ToRid, 在这个类里面去调用不同的ToRid... 
        
    可能的尝试：
        1.增加生成本地网页展示历史的截图记录
        2.因为假如监控的窗口很多, 利用一个个文件夹来管理对应窗口的截图不免太过浪费，
        因此，增加数据库来分别存放各个窗口的图片，这样管理也方便，存取也方便
"""


if __name__ == "__main__":
    to_rid_qq = ToRidQQ(["团结的火药桶", "弹药20级6班"])
    to_rid_qq.run_to_rid()
