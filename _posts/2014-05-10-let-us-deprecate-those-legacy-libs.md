---
layout: post
title: let us deprecate those legacy libs
tags: [Java, Java8]
categories: [Coding]
---

# 有了Java8, 这些库你就应该废弃了！

---

原文地址： [Let's Deprecate Those Legacy Libs](http://blog.jooq.org/2014/05/02/java-8-friday-lets-deprecate-those-legacy-libs/)

Java8为JDK带来了很多新的特性，比如Lambdas、Streams API等等。是时候来审视下哪些历史库应该进入垃圾桶了。

## LINQ-style 

有很多Java类库试图实现[LINQ](http://baike.baidu.com/view/965131.htm)风格，以操作数据库的方式操作内存数据集。现在，我们有了Stream API，就不再需要LINQ了。

来看几个例子：

### LambdaJ

此库试图在Java中通过晦涩难懂的ThreadLocal等，模拟闭包。

{% highlight java linenos %}
// This lets you "close over" the
// System.out.println method
Closure println = closure(); { 
  of(System.out).println(var(String.class));
}
 
// in order to use it like so:
println.apply("one");
println.each("one", "two", "three");
{% endhighlight %}

这是个好主意，不过 `closure();`后面的分号和丑陋闭包实现block，实在是很奇怪。

现在我们可以这样写：

{% highlight java linenos %}
Consumer<String> println = System.out::println;
 
println.accept("one");
Stream.of("one", "two", "three").forEach(println);
{% endhighlight %}

这就是很简单的Java8语法。



## 一半的Guava的

Guava是个相当优秀的库，Java8的很多实现借鉴了这个库。（这可是Google的几位Java大神共同维护的库啊）现在这些操作已经内置在JDK中了，比如`com.google.guava.base.Joiner`:

{% highlight java linenos %}
Joiner joiner = Joiner.on("; ").skipNulls();
. . .
returnjoiner.join("Harry", null, "Ron", "Hermione");
{% endhighlight %}

现在我们这样写：

{% highlight java linenos %}
Stream.of("Harry", null, "Ron", "Hermione")
      .filter(s -> s != null)
      .collect(joining("; "));
{% endhighlight %}

下面的几个类更能证明：

   - com.google.common.base.Optional -> java.util.Optional
   - com.google.common.base.Predicate -> java.util.function.Predicate
   - com.google.common.base.Supplier -> java.util.function.Supplier

另外，Guava的[`Functional`](https://code.google.com/p/guava-libraries/wiki/FunctionalExplained)实现也可以全部扔掉了：

如果你熟悉Guava，那在JDK8中这些同名类的用法基本同出一辙。相信不久后，Guava库也会把Java8中的内容从库中剔除。

## JodaTime

JodaTime库就是JSR-310的完整实现，全部API都被移植到了`java.time `包中。

## Apache commons-io

集成了Stream API，`java.nio`包更加的完善了。Apache Common IO之前为什么这么流行，也是因为在Java 7/8之前，读取文件实在太令人头痛了，谁会喜欢下面这样的代码？：

{% highlight java linenos %}
try(RandomAccessFile file = 
     newRandomAccessFile(filePath, "r")) {
    byte[] bytes = newbyte[size];
    file.read(bytes);
    returnnewString(bytes); // encoding?? ouch!
}
{% endhighlight %}

Common-IO 给我们带来了：

{% highlight java linenos %}
List<String> lines = FileUtils.readLines(file);
{% endhighlight %}

现在你可以忘了他们了：

{% highlight java linenos %}
List<String> lines = Files.readAllLines(path);
{% endhighlight %}

已经不需要第三方库帮我们处理IO了。

## 一系列的并发API和辅助类

除了某些并发类的改进，大神为我们带来了LongAdders, 并发环境下的高效计数器。可以看下左耳朵耗子的文章 [http://coolshell.cn/articles/11454.html](http://coolshell.cn/articles/11454.html)


## Base64 编码器

在2003年，已经提交了RFC 3548，提出了Base16, Base32, Base64规范。这些都是基于1993年提交的 RFC 1521和 1996年提交的RFC 2045 中的Base 64 编码规范。

2014年，JEP 135 终于成为了JavaSE8的一部分，有了 `java.util.Base64`！

下面的这些类可以退休了：

   - Apache Commons Codec 
   - JAXB’s internal Base64 encoders
   - Gauva, again
   - JEE’s javax.mail.internet.MimeUtility
   - Jetty’s implementation
   - This weird thing here
   - Or this weird thing here

## 其他的？

欢迎在评论中提出 ^_^
