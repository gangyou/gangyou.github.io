---
layout: post
title: "解决iPhone 4S安装IOS7后外放无声音问题"
description: "iphone4s after install ios7, no sound bug."
category: Apple
tags: [iOS7, iPhone4S]
---
丈母娘馈赠她淘汰的4S给我。终于，苦逼的安卓男第一次拥有了自己的iPhone手机。摆弄了两天之后，触发了bug（话说我这手就是bug手，第一天更新OS X Mavericks就发现了好几个bug）。外放没声音了！不论是游戏还是音乐，调整声音都只出现了铃铛的图示，没有了调整的进度条。

在网上找了很多帖子之后，终于发现了方法，再次做简单记录

## Step 1：越狱

没错，越狱！现在的越狱已经傻瓜式了，而且最新的iOS 7.0.4 也出了越狱工具，只要前往[Evasi0n越狱小组官方](http://evasi0n.com/)下载即可。前端时间沸沸扬扬的太极助手已经在最新版本内去除，可放心越狱。

## Step 2: 删除某文件

这里的文件是指 `/System/Library/LaunchDaemons/com.iapd.plist`。但是要访问到这个文件还要花一番功夫，你可以有两个选择。

### Option A: 安装 MobileTerminal

这是我个人最喜欢的方式，在手机上安装命令行工具。安装完之后，点开MT的App，按照以下输入：

    usernamde-iPhone: ~ mobile$su root
    Password:
    root# rm -i /System/Library/LaunchDaemons/com.iapd.plist
    
知道的童鞋看出来了，其实就是个Unix，本来iOS就是用OS X改的嘛。这里root的默认密码是 `alpine`

删除完成后，重启！声音就回来了。

### Option B: 安装 OpenSSH

既然是Unix，没什么理由让我们这些伟大的程序员不能通过ssh登录，是吧？通过`Cybia` 搜索安装OpenSSH。

安装完OpenSSH后，通过`通用-无线局域网`，点击wifi SSID旁边的叹号，查看手机获得的ip。

在你的MAC/Linux上，执行命令：

    ssh root@[iPhone ip]
    
然后执行相应的Option A 的操作就可以啦！

希望能够解决你的问题！

