---
layout: post
title: "Linux脚本处理用户输入"
description: "Linux脚本中处理用户输入的知识总结，包括了几个$带头特殊变量，getopt/getopts等命令"
category: Coding
tags: [Linux, Shell]
---

## 1. 脚本的常见输入类型

-----

###  1.1 选项

选项就是在命令后面，用一个横线或者两个横线开头的内容。`ls -a`或`ls --all`就是选项。Linux推荐单横线开头的选项使用一个英文字母，两个横线开头的选项使用完整的英文单词或几个英文单词。在多个英文单词之间可以用横线分割，比如`ls --almost-all`。

Linux推荐了一些通用命令选项，大部分的命令都实现了这些通用选项。在遇到新命令时，可以做适当的类比。在自己实现脚本命令时，也推荐实现这些选项

选项 | 描述
---- | ----
-a | 显示所有对象
-c | 生成一个计数
-d | 指定一个目录
-e | 扩展一个对象
-f | 指定读入数据的文件
-h | 显示命令的帮助信息
-i |  忽略文本大小写
-l |  产生输出的长格式版本
-n | 使用非交互模式（后台批量）
-o | 指定将输出重定向到的输出文件
-q | 以安静模式运行
-r | 递归的处理
-s | 以安静模式运行
-v | 生成详细输出
-x | 排除某个对象
-y | 对所有问题回答yes

###     1.2 参数

参数分为选项参数和一般参数，脚本后面非选项的内容就是参数。每个参数间用默认使用空格分隔。如果要忽略2个参数之间的空格，需要把两个参数用双引号括起来，如`cat "Hello World" > testout`。
    
## 2. 脚本中$带头的几个特殊变量

------

脚本中不可避免的需要处理命令行参数，在shell 脚本中，提供几个特殊变量，通过这些变量我们可以获得命令行参数的相关信息：

参数名 | 描述
----- | -----
$0 | 表示命令名称，包含了脚本的全路径
$1~$9 | 位置索引的参数，每一个之间以空格进行划分
$10+ | bash shell 支持10以上的参数位置索引，使用时需要以 ${10}的形式
$# | 命令行参数的个数
$* | 用一整个字符串表示的命令行参数
$@ | 用类似数组形式表示的命令行参数，可以进行`for`循环

一个简单的脚本示例如下：

{% highlight bash linenos %}
#!/bin/bash
# example of CLI parameters

echo "File name is $0"
echo "Parameter numbers: $#"

count=1
for param in "$@"
do
    echo "Parameter NO$count: $param"
    count=$[ $count + 1 ]
done
{% endhighlight %}

输出结果为

    >cli-parameters.sh hello world
    File name is cli-parameters.sh
    Parameter numbers: 2
    Parameter NO1: hello
    Parameter NO2: world

**注：选项的处理可以通过case或者getopt/getopts处理，在下一节中介绍**
    
##  3. 脚本中处理参数常用指令

---

### *     3.1 basename

在上一节中我们说到了`$0`会保存命令的全路径，有时我们并不关心全路径，只关心脚本名称是什么，这个时候就可以用`basename`命令来处理。

    >basename /bin/bash
    bash
    

### *     3.2 shift

`shift` 在脚本参数处理中是一个很重要的命令，作用是讲参数数组左移一个位置，移出去的那个就被丢弃了。同时可以带一个数字类型的参数，表示左移N个位置，如`shift 2`

### *    3.3  getopt

这个命令在MAC上测试不通过，可以用`getopts`代替，更好用。

### *     3.4 getopts

使用格式如下：

    getopts optstring variable
    
其中`optstring`列出你要再脚本中用到的每个命令行选项字母，然后在每个需要参数的选项字母后加一个冒号。`getopt`命令会基于你定义的optstring解析提供的参数。在optsting最前面的还可以加一个冒号，这个冒号表示忽略不在列表中的选项，不然会报错。

例子：

{% highlight bash linenos %}
#!/bin/bash
# processing options and parameters with getopts

while getopts :abc:d opt
do
	case "$opt" in
		a) echo "Found the -a option" ;;
		b) echo "Found the -b option, with value $OPTARG" ;;
		c) echo "Found the -c option" ;;
		d) echo "Found the -d option" ;;
		*) echo "Unknown option: $opt" ;;
	esac
done

shift $[ $OPTIND - 1]

count=1
for param in "$@"
do
	echo "Parameter $count: $param"
	count=$[ $count + 1 ]
done
{% endhighlight %}

### *    3.5  read

#### 3.5.1 标准用法

在脚本中获取用户输入的神器。接受从标准输入（键盘）或另一个文件描述符的输入。在收到输入后，read命令会将数据放进一个标准变量。如：

    echo "What's your name?"
    read name
    echo $name
    
####     3.5.2 显示提示语
    
 实际上，`read`包含了`-p`的选项，允许你直接在read命令指定提示符，我们用-p将上一个例子改写一下：
 
     read -p "What's you name?" name
     echo $name
     
#### 3.5.3 多个输入

`read`也可以同时接受多个输入，并保存在不同的变量当中

    read -p "What's you full name?" first last
    echo $first $last
    
在例子当中呢，我们接受了2个参数，如果输入了3个参数或更多，那么多余的部分将被保存到最后一个变量当中。

####  3.5.4 默认保存变量 - REPLY

你也可以在`read`命令中不指定变量，如果这样，read命令会把他接受到的所有数据保存在特殊环境变量`REPLY`当中

{% highlight bash linenos %}
#!/bin/bash
# testing the REPLY environment variable

read -p "Enter a number:" 
factorial=1
for (( count=1; count<=$REPLY; count++))
do
	factorial=$[ $factorial * $count ]
done
echo "The factorial of $REPLY is $factorial"
{% endhighlight %}

#### 3.5.5 设置读取超时时间 -t

`read`命令会hang住进程，等待输入。我们肯定不想一直等待输入，`-t`选项给了我们设置超时的能力，选项接受一个整型参数`-t n`表示等待的秒数。

{% highlight bash %}
#!/bin/bash
# timing the data entry

if read -t 5 -p "Please enter your name:" name
then
	echo "Hello ${name}, welcome to my script."
else
	echo
	echo "Sorry, too slow!"
fi
{% endhighlight %}

#### 3.5.6 限制读取的字符数 -nX

`-n1`或`-n2`类似的选项，允许限制读入的字符数。比如询问用户'Y/N'的场景只需要`read -n1`即可

#### 3.5.7 隐藏输入字符 -s

对于输入密码的场景，并不希望输入字符显示在终端上，可以通过`-s`选项。
