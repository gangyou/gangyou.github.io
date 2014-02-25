---
layout: post
title: WebSphere 核心概念解释
categories: WebSphere
tags: WebSphere, J2EE, Coding, Java, Middleware
---

来了企业里我才知道，以前学的Tomcat，Jetty， 尼玛都是扯淡啊！！！企业里面没人用啊！！！他们说没维保啊！！！他们都说让用WebSphere`(a.k.a WAS)`啊！！！控制台复杂的要死啊！！！软件又大又重啊！！！控制台复杂的要死啊！！！出了问题我就不知道怎么调试啊！！！代码不开源啊！！！要买IBM的培训啊！！！资料都是英文的啊！！！企业市场率为啥这么高啊！！！

学习WebSphere何其痛苦，曾经和同事开玩笑的问：

> 我们用WAS除了发布应用，更新应用，删除应用还用来干啥？

他们的回答是：

> 还有就是发布应用，更新应用，删除应用....

哼哼哼，端正下态度，仔细看看文档！其实WAS还是很强大的！

工作4年了，基本都是在开发应用，运维这块接触的比较少。WAS也只是启停用途。不过始终没弄清楚，

- startNode.sh
- startServer.sh
- startManager.sh
- startXXX.sh

这几个脚本之间到底是什么关系啊！尼玛~~ 哼哼哼，端正端正

直到我发现了红皮宝书，才慢慢弄清楚。我画了几张图，给和我一样弄不清楚这些事情童鞋。

![Websphere Applicatoin Server](/assets/img/20140225/2014-02-25-was-1.png)

接下来逐一解释上图中出现了几个概念

- Application Server: 应用服务器，J2EE的容器，你的应用就是运行在上面
- Node: 节点，就是一个或多个应用服务器的组，WAS通过节点来管理应用服务器们
- Node Group: 节点组，多个节点之间可以组成组，也是管理用的
- Cell：这个中文不知道怎么翻译，暂且就成为Cell吧。一个Cell是具有一个独立的管理域的节点和节点组的集合。
- Deployment Manager: 发布管理器，在WAS里面经常缩写为`Dmgr`。是Cell的核心管理器

这样就可以理解之前所说的那些脚本之间的关系了。首先要Cell运行，然后Cell上面运行着Node(s)和Node Group(s)，在Node里面运行着 Application Server(s)。然后只有启动了Dmgr才能管理里面的内容。

WAS还有一种分布式的部署方法，分布式管理中有一点点新的东西。

![Websphere Applicatoin Server - Distributed Configuration](/assets/img/20140225/2014-02-25-was-2.png)

又出现了几个概念是不

- Host: 主机，单个WAS实例，可以运行在同一个物理机器上也可以运行在不同的物理机器上
- Node Agent:  节点代理，在分布式环境下每个节点都带了一个节点代理，用来与发布管理器通信，协同处理管理工作。

如果想通过WAS Console 远程管理应用服务器，启动Node Agent就是必须的了。

上面这些是我个人对文档的理解，如果有哪里不对的地方，欢迎留言评论，先行谢过~
