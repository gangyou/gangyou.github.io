---
layout: post
title: "Learn to use iTerm"
description: "Learn to use iTerm"
category: Coding
tags: [Mac, iTerm, Shell]
---
Mac君（池建强）在《程序员需要知道的Mac十大工具》里面提到了Mac自带终端的替代品——iTerm工具。抽空学习了下，这个工具能够提升的效率不是一点点啊！

### 关于鼠标

---

一般我们在用Terminal的时候，基本是不会用到鼠标，不过在iTerm中，用好鼠标也是很有好处的。

- 选择文本。iTerm会把鼠标选中的文本自动复制到剪贴板中
- 双击。 双击会选中一个word
- 三击。 选中一整行
- 四击。 被称为**Smart select**，会自动识别一个URL字符串或者EMAIL地址，并选中。
-  按住shift并选择，会逐渐扩展选中的区域
-  按住cmd并单击URL，打开网页
-  按住cmd并单击文件名，打开文件
-  按住cmd能够拖放选中的文本到指定位置
-  按住cmd和option，三指滑动tracepad可以进行区域选择
-  按住control并点击可以打开右键菜单

看到了吧？用鼠标就能在`terminal`中做这么多事情了！再加上键盘不是要逆天了！！

### 关于键盘

---

- cmd + left arrow, cmd + right arrow 切换tabs，使用 cmd + { ， cmd + } 可以完成同样的效果
- cmd + [1~9] 直接导航到某个tab
- cmd + option + arrow keys 可以在 split panes中导航，split pane就是横向或者竖向拆分的窗口
- cmd + [, cmd + ]， 在split pane中顺序导航
- cmd + enter 全屏幕， cmd + u 恢复
- cmd + opt + E 类似mac的Expose 模式，显示所有的tab


### 查找并选择

---

抛开鼠标的文本选择，在窗口中按`cmd + f` 进入查找窗口，输入要查找的内容，然后按`tab`，则查找单词的后续文本会被选择。按`shift + tab`向左边选择

### 拆分窗口 split panes

---

上面提到了split panes，但是并未讲怎么进行窗口的拆分。按`cmd + d `进行水平拆分，`cmd + shift + d`进行垂直拆分。然后就可以通过 `cmd + ]`, `cmd + [`, `cmd + opt + arrow keys`进行拆分窗口间的导航。

### 设定标记

---

通过`cmd + shift + m `设定书签，然后按`cmd + shift + j` 跳转到指定位置。这在用terminal进行vi的时候特别有用。

### 任何文本的自动完成

---

注意是**任何文本**的自动完成！
只要是在当前tab或者buffer当中的任何文本都能被自动完成。输入文本内容的首几个字符，然后`cmd + ;`，就可以呼出自动完成菜单。
继续输入后续字符可以在选项中进行筛选。

### 粘贴历史

---

在iTerm中的每次复制都会被保存到粘贴历史当中，按下`cmd + shift + H` 打开粘贴历史。

### 场景重放

---

有些命令会不停的输出，比如`top`不停的刷新屏幕。通过iTerm的重放可以返回到之前某一个时刻的屏幕输出。按下`cmd + opt + b`会在终端最下方显示一个进度条，通过按下左右方向键就能在不同的时刻之间切换，查看历史屏幕。很hacker的感觉有木有？？

基本特性这样，其他的可以通过Menu和Profile去查看并配置，Have fun！