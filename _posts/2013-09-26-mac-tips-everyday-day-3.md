---
layout: post
title: "每天一点Mac技巧 3 - Spotlight和Alfred"
description: "Mac Tips Everyday day 3.每天一点Mac技巧3-Spotlight和Alfred"
category: Mac
tags: [Mac, Spotlight, Alfred]
---

快速工具
---------

Mac上的神器一个是自带的Spotlight，另外一个是收费的Alfred，免费也可以用，但是很多强大功能都是在PowerPack里面的。不过入门也够用了，等以后爷不够用了花个几刀买一个！

Spotlight
============

---

* ### 呼出： 

ctrl+space

* ### 注释

Spotlight注释可以帮助用户更有针对性的定位文件。选中一个文件或文件夹，command+I打开简介，在Spotlight注释功能中加入自己特定的关键词。关掉简介窗口，呼出Spotlight并输入刚才的关键词，可以准确定位到具备相关关键词注释的文件或文件夹。

* ### 逻辑判断

增加逻辑条件：NOT, AND, NOT。例如Spotlight搜索框输入mac and python，就会找出同时包含mac和python的文件。

* ### 设定检索内容的名称或类别

设定检索内容的名称或类别：例如检索”name: system”表示只搜索名称为system的内容，而检索”system kind: image”则表示搜索类型为内容含system 的图片（kind还可以是pdf和applications 等）



Alfred
==============

---

* ### 在小帽子Alfred中查询iOS和Mac App

之前的文章中介绍过Alfred这个Mac必备神器，有兴趣的童靴可以去我的博客上翻翻关于Alfred的介绍，今天再为大家介绍一个功能，就是通过Alfred查询iOS和Mac App。
通过热键呼出Alfred，点击右上角的小齿轮，打开设置窗口，点击Features-Custom Search，在右侧栏添加自定义搜索。

1、搜索iOS App：

	Search URL：itunes://ax.search.itunes.apple.com/WebObjects/MZSearch.woa/wa/search?term={query}
	Title：iOS App
	Keyword：ios
	
2、搜索Mac App：

	Search URL：macappstore://ax.search.itunes.apple.com/WebObjects/MZSearch.woa/wa/search?q={query}
	Title：Mac App
	Keyword：mac
	
设置完之后，再次呼出Alfred，输入mac go2shell，试一下效果吧。






## OS X

---

* ### 删除应用

删除Mac上的程序有很多种，比如直接去应用程序文件夹下删除、用CleanApp删除等等，今天介绍一个最好玩的。

打开launchpad，按住option键，就会看到所有的程序图标都会像iOS图标那样晃动起来，点击图标左上角的叉，即可删除程序，操作和iOS一样。

* ### 快捷键帮你找到保存的文件

我们经常会使用文件下载、另存为或导出等功能，这时系统会提示你选择要保存的文件路径，保存完之后我们往往要到保存的文件路径下查看保存的文件，事实上我们可以提前打开要保存的Finder窗口，具体操作就是在选择保存的窗口时，通过command+r直接打开Finder，Finder会自动跳到你选择的路径，完成保存操作后切换到这个Finder窗口即可。

* ### command+上下方向键

这两个快捷键很多应用程序都支持，具体功能就是屏幕滚动到应用程序的顶部或底部，类似很多网站提供的“回到顶部/底部”功能。Safari、Chrome、Firefox、Pages、Evernote等默认支持这样的功能。

在使用快捷键呼出Spotlight的时候，使用command+上下方向键还可以在搜索分组之间切换，非常方便。

* ### 查看电源状况

按住option键，点击右上角的苹果－系统信息，在打开窗口的左侧栏中找到电源，点击即可查看电源的详细信息，主要的指标包括电池循环计数、状况等信息。如果您安装了Alfred，呼出后直接输入sys，也可以找到系统信息。

如果想简单查看一下电池的使用状况，按住option键点击顶部工具栏上的电池图标，可以显示电池使用状况。如果出现“尽快更换”、“修理电池”等信息，那么有可能是电池出了问题，建议先重置系统管理控制器（SMC），如何重置可以去Apple的官方支持网站查一下。还没效果的话，可能就需要换电池了。

* ### 功能键设置

很多程序猿在调试程序的时候总会用到f7、f8这些键，但在OS X里这些功能键默认分配了一些功能，想使用的话需要同时按fn+f8…

如果希望将这些f按键用作标准功能键而且不需要按 fn，可以执行以下操作：

打开系统偏好设置-键盘，选中“将 F1、F2 等键用作标准功能键”，启用此选项时，顶部一行按键将用作标准功能键 (F1 – F12)，而不执行音量控制等特殊功能。启用此选项后，若要使用这些按键的特殊功能，请按fn，比如请fn+f8来播放音乐。

* ### 配置多种网络环境

如何配置多种网络环境 我自己无论在公司还是家里都是DHCP自动分配IP，所以不需要进行网络环境切换。但有些用户有时自动有时手动，需要多套网络配置方案，每次修改实在是太麻烦了。曾经有人问我Mac上是否有这样的第三方软件？我说没有，因为OS X的网络设置本身就提供了这样的功能。

打开系统偏好设置-网络，点击位置下拉菜单，找到编辑位置，打开后即可增删编辑多套网络设置，设置完成后保存。

这时点击屏幕左上角的苹果图标，在下拉菜单里增加了一个位置选项，里面就是你配置好的多种网络设置，点击切换即可。

* ### Space使用

隐藏的空间切换功能 以前介绍过OS X中Space的使用，我们可以定义多个Space，每个程序都可以在特定的Space中打开，多手势上推下滑选择程序，也可以通过ctrl+数字切换Space，很方便。今天再为大家介绍一个隐藏的功能，就是通过四指双击触控板，可以在你最近使用的两个Space之间切换，这个功能就类似电视频道中的返回功能，当你使用了Space1中的一些APP，切换到Space4，通过四指双击可以在Space1和Space4之间切换，对于协同工作非常有效。典型的应用场景：在Space1里编码，在Space4里参考各类文档。

* ### 不必要的右键菜单

去除右键菜单的重复项 OS X 系统有个问题，某个程序反复安装后，选中某种类型的文件，点右键-打开方式，你会看到不少重复的选项，我们可以用以下命令去除重复项。 
	/System/Library/Frameworks/CoreServices.framework/	Versions/A/Frameworks/LaunchServices.framework/	Versions/A/Support/lsregister -kill -r -domain local 	-domain system -domain user

* ### 分别设置Mac的鼠标和触控板的滚动方向？

很多人习惯鼠标使用相反的滚动方向，而触控板类似iPad那样的自然滚动，问如何设置，当时我的回答是不知道，因为目前OS X的系统设置里，鼠标和触控板的设置是统一的。今天发现了一个免费的软件Scroll Reverser，可以实现鼠标和触控板的分别设置。

下载地址：http://www.macupdate.com/app/mac/37872/scroll-reverser

启动后程序显示在顶部菜单栏，设置简单明了，有需要的同学体验一下吧。

* ### 文件重命名

文件重命名的问题以前说过，但最近又有些童靴问起，就再说一下。
如果你没有装任何插件的话，在Finder中重命名文件或文件夹的快捷键就是回车。打开文件用command+o，返回上级目录用command+向上的方向键。
如果你装了原来推荐过的XtraFinder，可以把回车改为打开文件（与windows操作类似），把option+r设置为文件重命名。
如果你在命令行下重命名文件，命令是这样的：mv oldname newname








