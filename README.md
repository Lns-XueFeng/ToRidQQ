# ToRidQQ
<h3>Help me to get message and to rid of qq（ To rid of QQ ）</h3>

<h3>目的：</h3>
<p>实现程序自动监控指定QQ消息窗口并将新消息发送至邮箱, 或通过微信进行通知, 从而实现我的手机无QQ化</p>

<h3>原因：</h3>
<ol>
    <li>我不喜欢越来越臃肿QQ以及杂乱的界面</li>
    <li>因为越来越多的群聊以及联系人, 但需查看的寥寥无几</li>
    <li>我喜欢手机上软件就几个, 因此QQ便成了我需要卸载的对象</li>
    <li>我比较喜欢使用邮箱, 因此便萌生了使用程序监控窗口并将新消息发送至我的邮箱</li>
    <li>后面又发现微信可开启QQ邮箱提醒的服务, 完美契合我的目的</li>
</ol>

<h3>需求：</h3>
我想要达到的效果：
<ol>
    <li>监控需要随时知道通知的重要的群聊</li>
    <li>避免错过重要通知且卸载手机上臃肿的QQ</li>
    <li>进一步减少我手机上app的数量</li>
    <li>通过开启微信邮箱通知服务，让微信可以通知我的QQ重要消息</li>
</ol>

<h3>使用程序：</h3>
<ol>
    <li>克隆项目：git clone https://github.com/Lns-XueFeng/ToRidQQ.git</li>
    <li>进入项目目录，安装项目依赖：pip install -r requirements.txt</li>
    <li>务必确定QQ邮箱已开启SMTP服务：找到config文件设置账号以及授权码</li>
    <li>登录QQ以及打开需监控的QQ窗口，复制QQ窗口昵称以待后续传入参数</li>
    <li>启动程序：python -m toridqq your_qq_window_name1 your_qq_window_name2</li>
</ol>

<h3>接收消息</h3>
<ol>
    <li>手机上安装QQ邮箱并开启SMTP服务</li>
    <li>也可以不安装QQ邮箱软件，更方便的方法是依靠微信</li>
    <li>可通过微信中的设置-->通用-->辅助功能-->启用QQ邮箱提醒</li>
    <li>即可达到只使用微信便可同时了解微信以及QQ的通知消息</li>
</ol>

<h3>注意：</h3>
<ol>
    <li>目前支持监控多个窗口, 但别使用QQ自动将窗口合在一起的模式</li>
    <li>需单独分开每个聊天窗口，单独放置后即可（重叠覆盖放置）</li>
    <li>最后，将各个QQ窗口最小化，需要时程序会自动激活窗口</li>
    <li>键盘左上角esc按键即为退出程序按键，按下即可退出程序</li>
</ol>

<h3>简单运行：</h3>
<p>克隆到本地后, 可通过easy_to_rid.py脚本运行, 只需要修改name参数</p>
<p>注意：name参数是一个列表，填写需要监控的窗口名称</p>

<h3>命令行运行：</h3>
<ul>
    <li>如果你只需要监控一个窗口：</li>
    <p>python -m toridqq your_qq_window_name</p>
    <li>如果你需要监控多个窗口(空格分隔window_names)：</li>
    <p>监控n个：python -m toridqq your_qq_window_name1 your_qq_window_name2</p>
</ul>

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
<p>在程序开始运行之前检查计算机网络情况（默认便会检查）</p>
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

<h3>吐槽：</h3>
<p>其实摆脱QQ的方法有很多, 比如：</p>
<ul>
    <li>购买AppleWatch体验近乎手机般的体验（Apple Watch被我卖给我姐了！）</li>
    <li>购买小米手环接收QQ消息并禁用手机QQ通知(但是我的手机就需要下载QQ了！)</li>
</ul>

<h3>成果：</h3>
<ul>
    <li>成功的让我戒掉了每天一打开手机就是看QQ, 搞不好还刷里面的短视频</li>
    <li>让我不再对于别人是否立马回复我的消息那么在意(也和微信禁用通知消息有关)</li>
    <li>QQ从我手机的消失也意味着我手机正式进入只看书听音乐偶尔微信聊天的状态</li>
</ul>
