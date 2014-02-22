---
layout: post
title: "Ant用户编写任务"
description: ""
category: Coding
tags: [Java, Ant]
---
任务生命周期
-------------------

###解析阶段
1. 对任务类进行实例化
2. 创建对project和父目标对象的引用
3. 增加id引用
4. 调用init()
5. 嵌套元素得到解析，并利用addXXX(), addCOnfiguredXXX() 和 createXXX()等方法得到处理

如果你的任务需要实例化元素本身，或者如果对象没有默认的构造函数，则使用create “你的任务创建了嵌套对象”
如果你的任务需要一个已实例化对象的引用，则使用add “Ant为你的对象增加了一个对象引用”
如果你需要Ant在传递引用前完全地处理元素，则使用addConfigured “Ant为你的任务对象增加了已配置的对象引用”

###运行时阶段
1. 任务的所有属性都得到设置

setXXX()得到调用，XXX为属性的首字母大写
2. 处理来自XML文件的CDATA文本

当Ant读取CDATA段时，它会对任务调用addText(String cdata)

3. 所有嵌套元素的属性都得到设置
4. execute() 得到调用

