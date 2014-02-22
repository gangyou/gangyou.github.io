 ---
layout: post
title: "Ant's DataType"
description: "Ant's DataType"
category: Coding
tags: [Java, Ant]
---
Ant DataType类型
-----------------------

- argument

对于由一个Ant构建文件调用的程序，向其传递命令行参数

- environment

对于由一个Ant构建文件调用的外部命令或程序，指定向其传递的环境变量。

- filelist

定义一个文件的命名列表，这些文件*无需*确实存在

- fileset

定义一个文件的命名列表，这些文件*必须*确实存在

- patternset

将一组模式分组在一起

- filterset

将一组过滤器分组在一起

- path

以某种在不同操作系统间可移植的方式指定路径（如类路径）

- mapper

定义一组输入文件和一组输出文件间的一个复杂关系

###Argument DataType

- file(all, File, *)

作为一个参数的文件名，在构建文件中，此文件名相当与当前的工作目录。“当前工作目录”依此类型所用的环境而有所不同。在作为一个参数传递时，此文件名要转换为一个绝对路径

- line(all, Stirng, *)

用空格分隔的多个参数的列表

- path(all, Path, *)

路径

- value(all, String, *)

一个命令行参数。如果你的参数中有空格，但又想将它作为单独一个值，则使用此属性。

示例：
<div class="well">
{% highlight xml %}
	<java fork="true" classname="org.apache.xalan.xslt.Process" failonerror="true">
		<arg line="-IN" />
		<arg line="${xmldata}" />
		<arg line="-XSL" />
		<arg line="${stylesheet}" />
	</java>
{% endhighlight %}
</div>

附加示例：
向一个进程传递两个不同的命令行参数
<div class="well">
{% highlight xml %}
	<arg line="-mode verbose" />
{% endhighlight %}
</div>

传递一个包含空格字符的参数
<div class="well">
{% highlight xml %}
	<arg value="Eric You" />
{% endhighlight %}
</div>

将一个路径形式的结构作为一个命令行参数传递：
<div class="well">
{% highlight xml %}
	<arg path="/temp;/tmp" />
{% endhighlight %}
</div>
在Windows系统中，这将转换为C:\temp;C:\tmp
在Unix系统中，这将转换为/temp;/tmp


###environment


