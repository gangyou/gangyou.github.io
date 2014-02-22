---
layout: post
title: Django入门第一课-一个简单的应用
description: Django第一课
category: Coding
tags: [coding, python, django]
---

First Django App
====================

创建项目命令
-------------------
安装完Django之后,在运行路径应该有`django-admin.py`命令,运行:

{% highlight python %}
django-admin.py startproject mysite
{% endhighlight %}

运行项目
--------------------
是的,没错!你的项目已经可以运行了,执行:
{% highlight python %}
python manage.py runserver [[address]:[port]]
{% endhighlight %}

数据库安装
----------------
基本来说,Django项目还是围绕着关系数据库来构建的,因此数据库也是很重要的一个内容.Django可以支持很多类型的数据库:Mysql, SQLite, Oracle等等.
数据库配置在`settings.py`的`DATABASES default`当中,基本参数如下:

-	ENGINE #数据库引擎
-	NAME #数据库名称
-	USER #用户名
-	PASSWORD #密码
-	HOST #主机地址,如果留空则为本地机器

TIMEZONE 设置
------------------

Django为国际化做了很多工作,如果设置了Timezone,那么内置的很多应用,包括了最有用的`admin`也会做相应的本地化,我们可以趁设置数据库时候顺道设置了~

{% highlight python linenos %}
# TIME_ZONE = 'America/Chicago'
TIME_ZONE = 'Asia/Shanghai'

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-cn'
{% endhighlight %}
[其他可用值](http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE)

已经安装的Apps
-------------------
Django为我们安装了很多默认应用:

{% highlight python linenos %}
django.contrib.auth
django.contrib.contenttypes
django.contrib.sessions
django.contrib.sites
django.contrib.messages
django.contrib.staticfiles
{% endhighlight %}

安装完应用之后,需要对应用需要的数据库进行初始化,使用命令: ` python manage.py syncdb `

创建一个App
----------------
{% highlight python linenos %}
python manage.py startapp application_name
{% endhighlight %}

创建应用所需的sql
--------------------

{% highlight python linenos %}
python manage.py sql polls
{% endhighlight %}

该命令会将初始话应用需要的SQL打印到控制台,如果要把这些SQL存成文件,使用命令行重定向

其他的SQL命令:

{% highlight python linenos %}
python manage.py validate # 检查models.py下的对象是否合法
python manage.py sqlcustom polls # 输出用户自定义SQL.
python manage.py sqlclear polls # 在表创建之前输出` drop if exists table_name;`
python manage.py sqlindexes polls # 在建表语句中输出索引创建语句
python manage.py sqlall polls # 输出所有SQL语句
python manage.py syncdb # 将model层的更改刷到数据库
{% endhighlight %}

更多关于manage.py的信息[django-admin.py documentation](https://docs.djangoproject.com/en/1.5/ref/django-admin/)