---
layout: post
title: "Mac 让外接的显示器字体显示效果更平滑"
description: "每天一点Mac技巧系列8-Mac Tips Everyday day 8 from mac kongfu"
category: Mac
tags: [Mac]
---

来自《Mac功夫》

如果你外接了一个非苹果生产的显示器，可能会觉得字体看起来有些失真和颗粒化，这是因为没有设置好字体的抗锯齿属性。修正方法很简单，打开terminal运行以下代码，注销并重新登录系统使更改生效

{% highlight bash linenos %}
	defaults -currentHost write -g AppleFontSmoothing -int 2
{% endhighlight %}

恢复代码：

{% highlight bash linenos %}
	defaults -currentHost delete -g AppleFontSmoothing
{% endhighlight %}
