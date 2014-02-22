---
layout: post
title: "Mac 轻松调整窗口大小"
description: "每天一点Mac技巧系列7-Mac Tips Everyday day 7 from mac kongfu"
category: Mac
tags: [Mac]
---

很快读完了《Mac KongFu》，虽然很多内容MacTalk里面也曾经介绍过，不过还是有几个干货的。

把觉得有用的技巧分享出来！

如果想调整窗口大小，只需把鼠标指针悬停在窗口边框上。没有鼠标的DS们，用触摸板很难瞄准有没有？

在terminal里面执行以下命令，可以扩大感应区域

{% highlight bash linenos %}
	defaults write -g AppleEdgeResizseExteriorSize 10
{% endhighlight %}

注销并重新登录系统使更改生效。

如果要恢复设置：

{% highlight bash linenos %}
	defaults delete -g AppleEdgeResizeExteriroSize
{% endhighlight %}

拖动鼠标前如果按住了`Option`键或者`Shift`键（也可同时按住），可以更轻松的调整窗口大小。按住`Option`键拖动某条边框，会使相对的两条边框同时收缩（类似手风琴风箱收缩的效果）；按住`Shift`键拖动会缩小整个窗口的宽高——效果类似于拖动窗口的边角。同时按住`Option`键和`Shift`键拖动，窗口将以其中心为基准点按比例缩放。
