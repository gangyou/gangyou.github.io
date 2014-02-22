---
layout: post
title: "Ant自动化部署F**k WebSphere"
description: "WebSphere Ant无限槽点，中文资料少网上示例不够完整，搞了好久才摸到一点眉目。略作记录，希望能够后来的Coder们一些帮助。"
category: Coding
tags: [Java, WebSphere, Ant]
---

一. 吐槽部分
----------------------

---

"this is the most utter garbage that ibm has ever written, and never bothered to fix."

--这部分(WebSphere Ant Tasks)是IBM写过的最垃圾的东西，并且他们从来没想过修复它！

这是一段从描述的资料中找到的内容，简直说出了我的心声。我不是WAS专家，一直是把WAS当Tomcat使～折腾ANT远程部署WebSphere V6.1花了我整整2天，在此先吐槽一段时间！

- 第一阶段，用 `${WAS_HOME}/bin/ws_ant.sh` 来处理，可是一执行就 `NoClassDefFoundError` ,话说我这个WAS不是才刚刚干净的装好吗？WTF*500!

- 第二阶段，开始用 `apache-ant-1.8.1` 来处理，确实在这里傻逼了一会，V6.1自带的JDK是1.4的，1.8.1版本似乎太新了,结果是一直卡在了 `NoClassDefFoundError: com/ibm/websphere/bootstrap/PreLauncher`。网上资料有很少（我想任何WAS问题都挺少的)，郁闷啊

- 第三阶段，开窍了！那就全部用WAS自带的东西来吧！终于最后看到了期望中的"BUILD SUCCESSFUL"

吐槽完毕，让我们进入正题！

二. WSADMIN
------------------

---

##wsadmin简介

WAS的远程部署有好几种方式，相同点是都要用wsadmin这个东东，WSAdmin是websphere6.1的管理控制台命令行工具，可以使用它与Websphere application server进行交互，或通过Jacl脚本运行管理命令。工具位于$WAS_HOME/bin目录下。

可用2种最简单的方式去连接wsadmin

1. SOAP
2. Jython API

没仔细研究过Jython，我们的目标就先落到第一种吧

让我们小小的连接下wsadmin，了解下wsadmin能够帮我们做些什么：

1. 连接WsAdmin
定位集群的Deployment Manager地址和端口号，地址即为WAS的地址，端口默认为8879，具体可参看

`${WAS_HOME}/profiles/${NodeName}/properties/wsadmin.properties`

{% highlight python %}
com.ibm.ws.scripting.connectionType=SOAP
com.ibm.ws.scripting.port=8879
com.ibm.ws.scripting.host=localhost
...
{% endhighlight %}



###日常维护

可以使用以下语句连接：

{% highlight bash %}
wsadmin -conntype SOAP -host localhost -port 8879 -user admin -password ******
{% endhighlight %}

如要要管理远程的WS的话，在本地安装一个完整版本的WebSphere吧 = = WTF!

{% highlight bash %}
wsadmin -conntype SOAP -host <remote_address> -port 8879 -user admin -password ******
{% endhighlight %}

连接成功之后就进入了wsadmin的命令行模式，有`wsadmin>`作为命令行前缀

{% highlight bash %}
	# 列出集群节点
	wsadmin> $AdminConfig list Node

	# 列出集群应用服务器
	wsadmin> $AdminConfig list Server

	# 列出应用服务
	wsadmin> $AdminApp list

	# 启动单个服务器
	wsadmin> $AdminControl invoke [$AdminControl queryNames type=NodeAgent,node=test-95Node01,*] launchProcess server35

	# 停止单个服务器
	wsadmin> $AdminControl invoke [$AdminControl queryNames type=Server,node=test-95Node01,name=server35,*] stop

	# 安装服务到集群
	wsadmin> $AdminApp install e:/hello.war {-cluster b2bpool -contextroot hello -appname hello -usedefaultbindings}
	wsadmin> $AdminControl save

	# 开启服务
	wsadmin> $AdminControl invoke [$AdminControl queryNames type=ApplicationManager,node=test-38Node01,*] startApplication hello

	# 停止服务
	wsadmin> $AdminControl invoke [$AdminControl queryNames type=ApplicationManager,process=server1,*] stopApplication hello

	# 更新服务(war包)到集群
	wsadmin> $AdminApp update hello app {-operation update -cluster b2bpool -contextroot hello -contents e:/hello.war}
	wsadmin> $AdminControl save

	# 更新服务(单个文件)到集群
	wsadmin> $AdminApp update hello file {-operation update  -cluster b2bpool -contextroot hello -contents e:/hello.jar -contenturi hello.war/WEB-INF/lib/hello.jar}
	wsadmin> $AdminControl save

	# 更新服务到节点
	wsadmin> $AdminApp update hello app {-operation update -node test-95Node01 -contextroot hello -contents e:/hello.war}
	wsadmin> $AdminControl save

{% endhighlight %}

###使用ant自动部署websphere

---

websphere 6.1中IBM通过wsadmin实现了很多 `ant tasks`, 都打包在了
`${WAS_HOME}/plugins/com.ibm.ws.runtime_6.1.0.jar` 

###三 Ant Tasks

在WebSphere V6中，IBM已经为我们扩展出了很多用起来不是很方便的Tasks，放在`<WAS_HOME>/plugins/com.ibm.ws.runtime_6.1.0.jar`中。

在使用这些自定义任务之前呢，请注意以下要点：

1. 使用IBM V9 JDK。（如果非要使用Oracle(Sun) JDK的话呢，先运行`<WAS_HOME>/profiles/<your profile>/bin/setupCmdLine.sh|bat` 设置环境变量)
2. 设置Ant的执行变量`ANT_OPTS="-Duser.install.root=<WAS_HOME>/profiles/<your profile>"`。如果你是打算远程部署另外一台机器上的WAS，你要装个完整版本的WAS在本地(WTF)，这里指定本地的profile位置
3. 准备Ant的执行库，一般只要包含上面提到的wasruntime.jar就可以，不放心的话就吧`<WAS_HOME>/lib, <WAS_HOME>/plugins, <WAS_HOME>/optionalLibraries`下的jar都加入classpath吧，至少我是这样的哈哈

*关于远程部署还有一点需要补充：不管你怎么指定IP，很遗憾的告诉你在Ant tasks内部，是不认ip只认主机名的！WTF有没有？ 比如你要部署的WAS地址是192.168.0.1,主机名myserver1,wsadmin会去找myserver1，而不管什么IP地址*

*这就需要在`/etc/hosts`里面为主机名增加地址解析，不明白请google之*
	
一个简单的例子，如果有什么问题请留言，请注意V6中貌似是没有UpdateApplication的，很多网上的例子都有V6用户就不要用了

{% highlight xml %}
<?xml version="1.0"?>
<project name="wasant" basedir="." default="wsInstallApp">
  <property environment="env" />
  <property name="ws.root" value="${env.WAS_HOME}"/>
  <property name="wsanttasks.jar" value="${ws.root}/plugins/com.ibm.ws.runtime.jar"/>
  <property name="ws.appname" value="myapp"/>
  <property name="ws.ear" value="/var/tmp/myapp.war"/>
  <property name="ws.contextroot" value="/myapp"/>
  <!--Login information-->
  <property name="ws.username" value="admin"/>
  <property name="ws.password" value="admin"/>
  <property name="ws.host" value="192.168.0.1"/>
  <property name="ws.port" value="8879"/>
  <property name="ws.conntype" value="SOAP"/>

  <!-- wsadmin command defined -->
  <property name="stopApp.Test166"
     value="$AdminControl invoke [$AdminControl queryNames type=ApplicationManager,process=Test166,*] stopApplication ${ws.appname}"/>

  <!-- task list  -->
  <taskdef name="wsStartServer" classname="com.ibm.websphere.ant.tasks.StartServer" classpath="${wsanttasks.jar}" />
  <taskdef name="wsStopServer" classname="com.ibm.websphere.ant.tasks.StopServer" classpath="${wsanttasks.jar}" />
  <taskdef name="wsInstallApp" classname="com.ibm.websphere.ant.tasks.InstallApplication" classpath="${wsanttasks.jar}" />
  <taskdef name="wsUninstallApp" classname="com.ibm.websphere.ant.tasks.UninstallApplication" classpath="${wsanttasks.jar}" />
  <taskdef name="wsStartApp" classname="com.ibm.websphere.ant.tasks.StartApplication" classpath="${wsanttasks.jar}" />
  <taskdef name="wsStopApp" classname="com.ibm.websphere.ant.tasks.StopApplication" classpath="${wsanttasks.jar}" />
  <taskdef name="wsListApps" classname="com.ibm.websphere.ant.tasks.ListApplications" classpath="${wsanttasks.jar}" />
  <taskdef name="wsAdmin" classname="com.ibm.websphere.ant.tasks.WsAdmin" classpath="${wsanttasks.jar}" />

  <!-- List APP-->
  <target name="wsListApps" description="List All Applications">
    <wsListApps conntype="${ws.conntype}" host="${ws.host}" port="${ws.port}" user="${ws.username}" password="${ws.password}" washome="${ws.root}" />
  </target>

  <!-- Uninstall App -->
  <target name="wsUninstallApp" description="Uninstall an Enterprise Application">
    <wsUninstallApp washome="${ws.root}" application="${ws.appname}" conntype="${ws.conntype}" options="-cell ${ws.cell} -node ${ws.node} -server ${ws.server} -appname ${ws.appname} -usedefaultbindings" host="${ws.host}" port="${ws.port}" user="${ws.username}" password="${ws.password}" failonerror="true"/>
  </target>

  <!-- install application -->
  <target name="wsInstallApp" description="Install Application ${ws.appname}">
    <wsInstallApp user="${ws.username}" password="${ws.password}" host="${ws.host}" ear="${ws.ear}" port="${ws.port}" conntype="${ws.conntype}" washome="${ws.root}" options="-cell ${ws.cell} -node ${ws.node} -server ${ws.server} -appname ${ws.appname} -usedefaultbindings -contextroot ${ws.contextroot}" />  
  </target>
</project>

{% endhighlight %}

接下去执行Ant

### 参考资料

---

- [使用WSAdmin和ANT自动部署websphere6.1](http://blog.csdn.net/andyxm/article/details/5971894)
- [WAS 6.0 ant tasks: Install an app with an external Ant](http://www.jroller.com/holy/entry/was_6_0_ant_tasks)


