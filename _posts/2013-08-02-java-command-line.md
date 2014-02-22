---
layout: post
title: "Java Command Line"
description: "Java命令行学习"
category: 
tags: [Java]
---
一直以来都是用IDE，认为工欲善其事，必先厉其器。直到最近才发现，基础才是王道，依赖IDE让我漏掉了很多东西，一有空现在就看基础

Java Standard Options
-----------------------

- `-client`
	
使用Java Hotspot Client VM，在64位jdk下无效，默认使用Java Hotspot Server VM

- `-server`

不解释

- `-agentlib:libname[=options]`

加载Native agent library

- `-agentpath:pathname[=options]`

通过全路径加载Native agent library

- `-classpath classpath` 或 `-cp classpath`

选择一组目录，Jar或者zip，寻找需要的类文件，多个之间用冒号:分割。`-classpath`和`-cp`中的classpath会覆盖系统变量`CLASSPATH`;另外可以通过通配符*制定某文件夹下的所有jar

- `-Dproperty=value`

设置系统变量

- `-d32  -d64`

指定运行环境为32位或者64位，目前仅Hotspot Server VM支持64位运行。使用-d64则-client选项被忽略（在将来版本中可能会发生变化）。对于非64位操作系统，默认运行在32位下（也将更改）

- `-enableassertions[:<package name>"..." | :<class name> ]`
`-ea[:<package name>"..." | :<class name> ]`
`-disabledasserations[:<package name>"..." | :<class name> ]`
`-da[:<package name>"..." | :<class name> ]`

启用或者禁用断言，默认禁用。如果带一个参数并以"..."结束，则会在特定的包和子包下启用或禁用断言;如果以"..."作为参数，则在当前工作目录未命名包下启用或禁用断言;如果不带"...",则对特定的类启用或禁用断言

- `-help or -?`

显示帮助信息并退出

- `-jar`

运行一个jar文件

- `-javaagent:jarpath[=options]`

加载一个Java Programing Language Agent, 参见java.lang.instrument

- `-jre-restrict-search`
`-no-jre-restrict-search`

包含/不包含用户私有的JRE版本搜索

- `-showversion or -version`

查看版本

- `-splash:imagepath`

显示启动画面

- `-verbose -verbose:class`

显示加载的类的信息

- `-verbose:gc`

报告每一次GC

- `-verbose:jni`

报告native method或其他Java Native Interface的活动

- `-version:release`

指定特定的运行版本。不过能够指定一个版本，可以通过version string指定一些列版本，可以通过version id; version id后面跟*表示版本前缀; version id 跟+表示不小于这个版本; 2个用&连接的version id 表示逻辑与。
例如`-version:"1.6.0_13 1.6*&1.6.0_10+"`
表示版本1.6.0_13，或者1.6为前缀版本号的版本并且版本号大于1.6.0_10

Non-Standard Options
---------------------------


