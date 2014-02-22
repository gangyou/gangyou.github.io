---
layout: post
title: Ubuntu安装jekyll
description: Ubuntu安装jekyll
category: Blogging
tags: [Jekyll, Github Pages, Installation, Ubuntu]
---

Step1 安装Ruby
--------------------
在Ubuntu下安装Ruby最快的方式当然是通过apt-get，不过需要注意的是gem的安装很多都需要依赖ruby-dev，要同时把ruby-dev安装

	$ sudo apt-get install ruby ruby-dev rubygems

到此，Ruby的安装就算告一段落了

Step2 安装Jekyll
------------------------
中国特色的原因gem命令会卡很久，感谢taobao团队把rubygem做了国内镜像，立马更换gem源

	$ sudo gem sources --remove http://rubygem.org/
	$ sudo gem sources -a http://ruby.taobao.org/
	$ sudo gem sources -l
	#*** CURRENT SOURCES ***

	#http://ruby.taobao.org/

然后就是安装Jekyll
	$ sudo gem install jekyll

Step3 Markdown引擎
------------------------
很多Github友人推荐了rdiscount作为Markdown引擎

	$ sudo gem install rdiscount

到此，jekyll就安装完成了

