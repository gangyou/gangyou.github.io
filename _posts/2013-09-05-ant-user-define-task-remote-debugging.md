---
layout: post
title: "Ant用户自定义任务调试"
description: ""
category: Coding
tags: [Ant,Java]
---

部分内容转载至 [ANT创建并调试自定义的任务](http://blog.csdn.net/caesarzou/article/details/5672415)

1. 前言
--------------

Ant自身提供了一系列的Core Task，可以轻松的实现目录管理，编译，运行等功能。当然除了Core Task提供的功能之外，我们也有一些功能上的扩展的需求。很简单的方式是把自定义的功能封成jar包，调用Task-java来执行主类，这样做的问题是输入的属性将会以参数串的形式出现，很不直观。所以ant提供了另一种方式：自定义Task。自定义Task和Core-Task一样，有自己的Task名和属性。下面来讲一下如何自定义ant Task，以及自定义Task的的创建。

2. 如何创建一个Task
--------------------------

这部分在ant的手册里面写的很清楚，简单翻译一下：

	首先要把%ANT_HOME%/lib下的ant.jar引入classpath,创建一个org.apache.tools.ant.Task 的子类。

	如果要支持一个属性，只需要简单的实现一个public的函数，函数名为set+属性的小写。如果用户填写了该属性，ant会自动调用该函数。

	如果要支持级联的属性，则应该实现org.apache.tools.ant.TaskContainer的接口。

	重载父类的public void execute函数，并在里面实现主逻辑，如果出错，请抛出一个BuildException的异常，因为函数没返回值。

###自定义任务的例子

####MyVeryOwnTask.java

{% highlight java linenos %}
package com.example.ant;

import org.apache.tools.ant.BuildException;
import org.apache.tools.ant.Task;

public class MyVeryOwnTask extends Task {
    private String msg;

    // The method executing the task
    public void execute() throws BuildException {
        System.out.println(msg);
    }

    // The setter for the "message" attribute
    public void setMessage(String msg) {
        this.msg = msg;
    }
}
{% endhighlight %}

`build.xml`示例，注意任务之间的依赖

####build.xml

{% highlight xml linenos %}
<?xml version="1.0"?>

<project name="OwnTaskExample2" default="main" basedir=".">

  <target name="build" >
    <mkdir dir="build"/>
    <javac srcdir="source" destdir="build"/>
  </target>

  <target name="declare" depends="build">
    <taskdef name="mytask"
        classname="com.example.ant.MyVeryOwnTask"
        classpath="build"/>
  </target>

  <target name="main" depends="declare">
    <mytask message="Hello World! MyVeryOwnTask works!"/>
  </target>
</project>
{% endhighlight %}

运行之后会看到类似这样的输出:

	Buildfile: ./build.xml
	build:
	declare:
	main:
	   [mytask] Hello World! MyVeryOwnTask works!
	BUILD SUCCESSFUL
	Total time: 693 milliseconds

3. 如何调试自定义的Task
-----------------------

ant本身是个批处理，逻辑也是用java实现的，结合上面的了解，可以看出自定义的类Task是以refect的方式由java虚拟机加载执行的。即主类存在用户的工程里面。一种方式是将ant的相应jar引入当前工程的classpath，创建一个application的debug配置，将主类设置为ant的主类：org.apache.tools.ant.launch.Launcher。但存在的问题很多，首先ant执行的环境变量，当前目录等都和真正的运行环境有所区别。要配置很多的环境信息和参数，不利于多次调试。

我推荐的方式是利用java的远程调试来达到调试的目的。

3.1 创建远程调试Server
=========================

###3.1.1 Java远程调试

	-Xdebug -Xnoagent -Djava.compiler=NONE -Xrunjdwp:transport=dt_socket,server=y,address=5050,suspend=n
	-XDebug               启用调试。
	-Xnoagent             禁用默认sun.tools.debug调试器。
	-Djava.compiler=NONE  禁止 JIT 编译器的加载。
	-Xrunjdwp             加载JDWP的JPDA参考执行实例。
	transport             用于在调试程序和 VM 使用的进程之间通讯。
	dt_socket             套接字传输。
	dt_shmem              共享内存传输，仅限于 Windows。
	server=y/n            VM 是否需要作为调试服务器执行。
	address=3999          调试服务器的端口号，客户端用来连接服务器的端口号。
	suspend=y/n           是否在调试客户端建立连接之后启动 VM 。

Java的远程调试JDPA是基于JDWP协议的一种交互式调试方式，最大的特点是VM的运行环境和调试环境相互独立。这样就可以很好的解决运行和调试的环境问题。

要实现远程调试，需要在server端的虚拟机参数中加入：

	-Xdebug -Xrunjdwp:transport=dt_socket,address=5050,server=y,suspend=y

即：使用端口的方式进行[JDWP](http://www.ibm.com/developerworks/cn/java/j-lo-jpda3/)通讯，端口为5050，采用挂起的方式，只有客户端连上才启动虚拟机。

###3.1.2 Windows下方式

分析ant.bat文件的代码可以看到：

	"%_JAVACMD%" %ANT_OPTS% -classpath "%ANT_HOME%/lib/ant-launcher.jar" "-Dant.home=%ANT_HOME%" org.apache.tools.ant.launch.Launcher %ANT_ARGS% %ANT_CMD_LINE_ARGS%

而`%ANN_OPTS%`这个环境变量在批处理之前并没有得到设置，看来这就是ANT留给我们的操作参数变量，创建一个debug_ant.bat

	set ANT_OPTS=-Xdebug -Xrunjdwp:transport=dt_socket,address=5050,server=y,suspend=y
	call ant %*

用bebug_ant.bat来替换ant.bat就可以在不影响任何其它环境变量的情况下，启动远程调试server。

### 3.1.3 Linux

聪明的你一定想到了，在linux下面修改ant.sh就好了！没错！可惜我机器上偷懒装的是dpkg安装版本，在bin下面只有执行文件。如果你和我一样，那么也难不倒我们！不就是环境变量嘛

	export ANT_OPTS="-Xdebug -Xrunjdwp:transport=dt_socket,address=5050,server=y,suspend=y"
	cd ant-example
	ant targetname

### 3.1.4 跨平台简单解决方案

其实我们已经有Eclipse了，对不对！不要这么麻烦的啦～

#####3.1.4.1 创建外部工具配置

首先配置外部执行`Run-> External Tools -> External Tools Configuration`，你如果之前执行过Ant脚本，大概会长这个样子！如果没有，那么创建一个并执行吧～

![Eclipse External Tools][external-tools-1]

然后新建一个Ant Build配置

![Eclipse External Tools Config Step 1][external-tools-new-1]

注意红圈的地方，其中第二个红圈`BuildFile`这里要写上对应的文件。比如你的项目叫`your-project`那么

	${workspace_loc:/your-project/build.xml}

第三个红圈可加可不加，是让Ant Build过程显示更多的信息而已，已经在调试了，我们总希望能够尽量多的获取调试信息不是？

然后是在配置JRE启动参数，参数可从上面的描述中获取

![Eclipse External Tools Config Step 2][external-tools-new-2]


#####3.1.4.2 创建Debug项

以3.1.4.1中的配置运行Ant脚本，VM就会挂起并监听相应的接口！接下去就是Debug了！

通过`Run -> Debug Configurations...` 打开Debug配置，在`Remote Java Application`下新建一个选项，具体配置如图：

![Eclipse Debug Configuratin][eclipse-debug-config]

注意： 
2- 项目配置
3- 连接类型选Standard Socket Attach
4- 端口和JRE配置中的参数保持一致

启动External Tools, 加好断点，Debug开始！

3.2 调试
=====================

###3.2.1 开启调试服务

不管你是用ant.bat，还是设置ANT_OPTS后执行脚本，此时ant都会挂起并监听着端口。接下来进入最后一步

###3.2.2 创建远程调试Client

用eclipse打开你的自定义Task所在的工程，打开Debug configuration，新增Remote Java Application

选择:

	Project: your project	
	connection Type： Standard（SocketAttach）
	connection Properties：
		Host： local host
		Port： 5050

###3.2.3 开始调试

在eclipse的代码相应位置设置好断点，采用刚刚创建的configuration进行调试。

此时ant的虚拟机将开始执行，并会在断点相应的位置上做出响应。

OK，现在享受你自定义的task带来的方便吧。

4. 常见问题
=========================

### 4.1 Unable to install breakpoint due to missing line number attribute

这个问题通过以下方法解决

	1. 访问eclipse 菜单 "Window --> Preferences --> Java --> Compiler --> Classfile Generation", 勾选"Add line number attributes"
	2. 在build.xml <javac> 任务中加入 `debug="true"`
	3. Clean项目，删除已经编译的class文件
	4. Enjoy!


[external-tools-1]: /assets/images/2013-09-05-eclipse-external-tools-1.png "Eclipse External Tools Configuration image 1"
[external-tools-new-1]: /assets/images/2013-09-05-external-tools-config-new-1.png "Eclipse Externla Tools Configuration New Step 1"
[external-tools-new-2]: /assets/images/2013-09-05-external-tools-config-new-2.png "Eclipse Externla Tools Configuration New Step 2"
[eclipse-debug-config]: /assets/images/2013-09-05-eclipse-debug-config-1.png "Eclipse Debug Configurations"
