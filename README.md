# ToRidQQ
<h3>Help me to get message and to rid of qq</h3>

<h3>目的：</h3>
<p>实现程序自动监控指定QQ消息窗口并将新消息发送至我的邮箱, 从而实现我的手机无QQ化</p>

<h3>使用：</h3>
<ol>
    <li>打开QQ并激活指定QQ窗口</li>
    <li>复制QQ窗口昵称以待后续传入参数</li>
    <li>克隆项目：git clone https://github.com/Lns-XueFeng/ToRidQQ.git</li>
    <li>启动程序：python -m toridqq your_qq_window_name</li>
    <li>注意需将QQ窗口始终处于激活状态</li>
</ol>

<h3>原因：</h3>
<ol>
    <li>我不喜欢越来越臃肿QQ以及杂乱的界面</li>
    <li>因为越来越多的群聊以及联系人, 但需查看的寥寥无几</li>
    <li>我喜欢手机上软件就几个, 因此QQ便成了我需要卸载的对象</li>
    <li>我比较喜欢使用邮箱, 因此便萌生了使用程序监控窗口并将新消息发送至我的邮箱</li>
</ol>

<h3>简单运行：</h3>
<p>克隆到本地后, 可通过easy_to_rid.py脚本运行, 只需要修改name参数</p>

<h3>自定义间隔时间：</h3>
<p>自定义程序监控指定窗口的轮询间隔时间</p>
<ul>
    <li>python -m toridqq -t interval_time your_qq_window_name</li>
    <li>python -m toridqq --time interval_time your_qq_window_name</li>
</ul>

<h3>自动打开并登录QQ：</h3>
<p>目前暂不支持</p>
<ul>
    <li>python -m toridqq -o your_qq_window_name</li>
    <li>python -m toridqq --open your_qq_window_name</li>
</ul>

<h3>检查计算机网络情况：</h3>
<p>在程序开始运行之前检查计算机网络情况</p>
<ul>
    <li>python -m toridqq -c your_qq_window_name</li>
    <li>python -m toridqq --check your_qq_window_name</li>
</ul>

<h3>校园网协议自动登录：</h3>
<p>如果你也是校园网登录的网络, 可通过修改源代码来协议自动登录</p>
<ul>
    <li>python -m toridqq -r your_qq_window_name</li>
    <li>python -m toridqq --register your_qq_window_name</li>
</ul>

<h4>注意：不要打开多个窗口, 目前仅支持一个窗口</h4>