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
        
    支持监控多个窗口
        得到命令行传入的需要监控的窗口们列表
        每轮询一次便遍历一次此列表
        每一个窗口根据其名称新建一个图片文件夹以便于分别判断每一个窗口新旧图片的相似度
        
        通过窗口名称(window_name)进行标识
        1.修改name参数?为*, 得到需监控列表(window_name_list)
        2.在ToRid实例化时遍历window_name_list为每个window_name新建图片文件夹
        3.修改run_to_rid中代码: 遍历len(window_name_list)次self._capture_and_match(window_name)并传入标识(window_name_list)
        4.内部代码根据标识window_name去工作(即, 后面的代码只是改变了其工作的路径)
    
"""


if __name__ == "__main__":
    to_rid_qq = ToRid("团结的火药桶")
    to_rid_qq.run_to_rid()
