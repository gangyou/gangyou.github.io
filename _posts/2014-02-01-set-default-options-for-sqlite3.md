---
layout: post
title: "设置Sqlite3的默认选项"
description: "set default options for sqlite3"
category: Coding
tags: [Database, Coding, Python, Sqlite3]
---
Sqlite3是 Python默认支持的一个简单数据库，可以作为文件数据库或者`In-Memory`的数据库。在开发`Data-Driver Applicaton`的时候，调试的时候，都十分好用。

关于Sqlite3的说明请参考 [w3cschool.cc](http://http://www.w3cschool.cc/) 的相关教程，能在W3C上面有教程也说明这个数据库的广泛程度了吧。

默认安装的sqlite3还是有很多使用上的不便的，特别是默认使用`list`的显示模式和关闭的`headers`，具体含义可以参看上面的网址，本文仅仅介绍如何设置这些默认的选项，所有选项可以在命令行使用`.show`查看。

sqlite3启动的时候会读取`~/.sqliterc`的配置信息，那么可以直接把你想执行的启动命令写入到这个文件中，在这里我们仅仅设置下显示的模式

{% highlight bash linenos %}

vi ~/.sqliterc
.mode column
.headers on

{% endhighlight %}

这样就看着顺眼多了是不是？