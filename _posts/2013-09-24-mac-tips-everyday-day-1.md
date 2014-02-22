---
layout: post
title: "每天一点Mac技巧 1 - 快捷键"
description: "Mac Tips Every Day - Day 1 每天一点Mac技巧-快捷键 前几天刚刚入手Mac,把池建强Mac军的MacTalk从头到尾开始翻阅。[池先生的博客](http://macshuo.com/) 上面也有微信公众号Mac说，推荐关注。"
category: Mac
tags: [Mac]
---
篇首语
-----------

---

前几天刚刚入手Mac,把池建强Mac军的MacTalk从头到尾开始翻阅。[池先生的博客](http://macshuo.com/) 上面也有微信公众号Mac说，推荐关注。

池先生的文章有个特点，最后通常会附上一写MacTips，又看文章又学技巧，本是极好的。不过对于我这样的Mac小白，想马上把Mac用的顺手的人，技巧点有点太分散了！

于是有了这些系列文章，希望把池先生分享的Mac Tips和本人在学习Mac的过程中学到的知识点整理出来。这些内容可能会结合本人的情况，如果你是深度的Win用户，然后又有部分的Ubuntu/Linux使用经验，欢迎你同我一起学习。如果不是，那么这些内容可能不是很适合你，[Hater](http://macshuo.com/?p=342)请绕道。


启用Root
=========

----

1. 从 Apple 菜单中选取系统偏好设置...。
2. 从显示菜单中选取用户与群组。
3. 点按锁图标并使用管理员帐户进行鉴定。
4. 点按“登录选项...”。
5. 点按右下部的“编辑...”或“加入...”按钮。
6. 点按“打开目录实用工具...”按钮。
7. 点按“目录实用工具”窗口中的锁图标。
8. 输入管理员帐户名称和密码，然后点按“好”。
9. 从编辑菜单中选取启用 Root 用户。
10. 在“密码”和“验证”字段中输入您想要使用的 root 密码，然后点按“好”。

## Root 方法2

用过Linux/Unix系统的都知道root用户，它具备具有读写文件系统所有区域的特权，是最高级别的用户。OS X一样有root用户，只不过默认情况是不开启的。我们想在命令行执行需要root权限的操作时，可以在命令之前增加sudo指令，比如执行每日维护指令，`sudo periodic daily`，系统会提示你输入用户密码，执行root权限。在GUI（图形界面）执行root级别的命令时也会提示输入用户密码。一般情况下我们是不需要开启root用户的。

用惯了Linux系统的用户有时很想启用root用户，其实也很简单，打开Finder，输入shift+command+g，在前往文件夹中输入：`/System/Library/CoreServices`，然后在目录中找到目录实用工具并打开，解开左下角的小锁，然后点击顶部菜单的，你就会看到启用或停用root用户的选项了。然后我们在命令行下执行`su -`，就可以切换到root目录下，root的默认目录是`/var/root`。也可以在系统启动时用root用户登录。

如果仅仅是想在终端里切换到root用户下，直接执行`sudo su -`，然后输入当前的用户密码即可。

root有风险，启用须谨慎！



常用快捷键
==========

----

![常用快捷键][shortcut]


###Shell

--

* #### sips

使用sips批量处理图片文件（尺寸，旋转，翻转等）

{% highlight bash linenos %}
# 把当前用户图片文件夹下的所有JPG图片宽度缩小为800px，高度按比例缩放
> sips -Z 800 ~/Pictures/*.jpg

# 顺时针选装90˚
> sips -r 90 ~/Pictures/*.jpg

# 垂直翻转
> sips -f vertical ~/Pictures/*.jpg
{% endhighlight %}

* #### homebrew

Homebrew的功能和OS X自带的MacPorts很像，但是更为轻量级，由于大量利用了系统自带的库，安装方便，编译快速，实在是OS X系统开发中之必备工具。
安装方式：ruby -e “$(curl -fsSkL raw.github.com/mxcl/homebrew/go)”
使用方式：brew install wget //安装wget工具。
具体的使用请参考：https://github.com/mxcl/homebrew/wiki

* #### mdfind

{% highlight bash linenos %}
mdfind是一个非常灵活的全局搜索命令，类似Spotlight的命令行模式，可以在任何目录执行文件名、文件内容进行检索，例如：
mdfind 苹果操作系统    
//搜索文件内容或文件名包含苹果操作系统的文件
mdfind -onlyin ~/Desktop 苹果操作系统
//在桌面上搜索文件内容或文件名包含苹果操作系统的文件
mdfind -count -onlyin ~/Desktop 苹果操作系统
//统计搜索到的结果
mdfind -name 苹果操作系统
//搜索文件名包含苹果操作系统的文件
{% endhighlight %}

* #### mdls

mdls可以列出某个文件或文件夹的所有元数据信息，针对不同文件显示不同的元数据信息，例如文件创建时间、类型、大小等，如果是图片或音视频文件，则会显示更多元数据信息。使用方式非常简单：

{% highlight bash linenos %}
	mdls ~/Desktop/a.jpg
	# 如果想查看图片的ISO数据，可以使用如下命令：
	mdls ~/Desktop/a.jpg|grep ISO
{% endhighlight %}

* #### man to pdf

打开OS X的终端，通过man命令可以直接查看该命令的使用手册，但有时我们会觉得在命令行查看不太方便，如果可以提供一个pdf文档就完美了。这很容易做到，在终端输入如下命令，即可在预览程序打开grep的使用手册，另存为你需要的文件名即可：

`man -t grep | open -f -a Preview`

* #### 在Mac下如何进行文件比较？1、对于单个文件的比较，一般使用diff或vimdiff就可以了，比如：

	`vimdiff destfile.txt sourcefile.txt`

vim会非常清晰的显出时文件的不同，还有很多快捷方式帮助你查看和操作文件，这个命令比较适合命令行爱好者，如果大家喜欢，后续可以讲讲。

2、对于大批量文件的比较，还是图形化比较工具更合适一些。OS X自带了FileMerge比较工具，可以满足部分需求，但对于中文编码文件或大文件经常会崩溃，很奇怪Apple一直不解决这个问题。

3、推荐一款收费软件，VisualDiffer（25元），UI、功能和稳定性都非常不错，实在是居家旅行、代码比较、查找问题的必备利器，有需要的童靴可以感受下。








[shortcut]: /assets/images/2013-09-24-mac-osx-tracepad-gesture.png "Mac OS X Lion常用快捷键"
