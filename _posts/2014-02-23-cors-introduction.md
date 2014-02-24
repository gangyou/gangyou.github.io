---
layout: post
title: CORS 跨域资源共享介绍
categories: Coding, Security
tags: Web, Javascript, CORS, W3C
description: CORS, Cross-Origin Resource Sharing 框架简介
---

### 吐槽部分

国内的技术研究环境实在是不怎么样，CORS这么革命性的东西已经出来了这么久了，居然没多少人知道（包括我自己）。我们说

> “一流的企业做标准，二流的企业做技术”

在技术发展的领域我先也是一样的

> 一流的程序员编写标准，二流的程序员实现标准，三流的程序员使用标准实现，四流的程序员连最新的标准也不知道，还在用老东西

上面这句话可能会有点中，但是我相信反应了国内目前技术的现状。特别是在那些已经有了十几年、二十几年的历史的领域，大家似乎都没那么求新求变，把领域的新事物新发展共享出来。比如用 **Java读取文件**，用Google(不要用baidu，不然肯定是旧的)，大部分还是使用了`JDK1.3`的 IO API，随着现在NIO被提及的次数越来越多，也逐渐出现了用 `FileChannel` 的博文示例（我自己也写了一篇），不过兄弟们，现在NIO已经出到2了，大家还在用JDK1.3？ 这里面的性能损耗，安全问题就没人关注了？

这也就是为什么IE6到现在还活的好好的，让一堆前端人员吐血！ 要我说，IE6不管是性能还是安全，特别是安全上存在这么多问题。用户访问时候直接禁止访问不就好了，还费时费力的支持，其实是自己给自己挖坑。

吐槽部分完了，回到正题！

### 什么是CORS

`CORS` 是 `Cross-Origin Resource Sharing` 的缩写，翻译成中文应该是跨源资源共享框架。更具体的内容可以参看 [CORS W3C草案](http://www.w3.org/TR/cors/) 。

#### CORS能做什么

Ajax的安全控制沿用了Javascript的同源策略，但是实际的应用中却出现了很多需要跨域的应用场景，比如一个订单的应用需要异步查询另外一台服务器上的库存系统的库存情况。伟大的程序员们利用各种HACK技巧，给我们折腾出了好多个解决方案，如JSONP、flash、ifame、xhr2等等。但是这些方案都会遇到一系列的问题，带来一定的安全隐患。越复杂的方案总会引入些东西。这些安全问题不是本文讨论的重点，感兴趣的童鞋可以看下 **《Web之困——现代Web应用安全指南》**

#### CORS的浏览器支持
    
关于CORS的浏览器支持情况，可以看下这个网址 [Can I use CROS?](http://caniuse.com/cors) 。这个页面会不断的更新浏览器对CORS的支持情况，编写本文的时候，支持率大概在79.42%。

- Chrome 3+
- Firefox 3.5 +
- Opera 12+
- Safari 4+
- Internet Explorer 8+ 

基本上你的应用不需要支持IE6，应该就可以用这套解决方案了，让IE6都去死吧！！哇卡卡卡！

### CORS和目前跨域解决方案的类比

基本上CORS和其他跨域解决方案，最大的区别就是简单、安全、标准！ 可以避免XSS， 框架注入等安全性问题

### CORS的请求类型

今时今日的CORS包括两种不同类型的 `XMLHttpRequest API` 调用。当站点企图通过CORS加载跨域内容时， 浏览器需要先区分这是简单请求( Simple Requests) 还是非简单请求 （Non-Simple Requests）。如果是前者，其所产生的HTTP流量和常规的普通请求无异，而后者则有一个握手的过程。

#### Simple Requests 简单请求

##### 规范

现在的规范规定，简单请求只能为以下方法： GET, POST 或 HEAD。 此外，发起CORS简单请求的一方只能获取到以下这些响应头的值：

- Cache-Control
- Content-Language
- Content-Type
- Expires
- Last-Modified
- Pragma

同时，只要请求头中包含自定义的请求头，哪怕是原本在规范白名单里推荐的请求头，该请求也会立刻被无条件降级为非简单请求。Webkit里还会把包含数据体提交的请求也当做非简单请求类型。

##### 通信过程

假设我们的订单页面是在 `http://www.order.com` 上，希望从 `http://www.stock.com` 上加载库存数据。

简单请求的通信过程与一般的HTTP请求无异。

1. 页面发送Ajax请求，浏览器会在请求头中写入
    
    Origin: http://www.order.com
    
2. 服务器接受到请求后进行响应。CORS的安全性检查就是在这个阶段进行的，服务器可以根据Origin头信息，判断请求源是否在白名单或者黑名单中，以此决定是否正常相应。如果决定正常响应，则会写入响应头：

    Access-Control-Allow-Origin: http://www.order.com
    
3. 浏览器在接受到该响应时，会判断是否发起请求的源在 Access-Control-Allow-Origin当中。如果在，就允许 `XMLHttpRequest API` 读取返回信息。否则就直接抛出异常，比如下面的实例。
    
    {% highlight javascript %}
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://www.163.com", false);
    xhr.send()
    
    //XMLHttpRequest cannot load http://www.163.com/. No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'http://www.cnblogs.com' is therefore not allowed access. VM550:2
NetworkError: A network error occurred.
    
    {% endhighlight %}
    
##### 完整实例

让我们完整的把通信的HTTP报文看一下。

{% highlight javascript %}

    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://www.stock.com/status", false);
    xhr.send();
    
{% endhighlight %}

这段代码发送的 HTTP 请求头大致如下：

     GET /status HTTP/1.0
     HOST: order.com
     Cookie: [Cookie data]
     Origin: http://www,order.com

服务器回应以下信息，表示它的响应确实是跨域可读的：

    HTTP/1.0 200 OK
    Access-Control-Allow-Origin: http://www.order.com
    
    相应报文体
    
**注意：** 在这里 `Access-Control-Allow-Origin` 的值是允许使用通配符 `*` 的，这是同源的检查就会被跳过，意味着接受任何网站的跨域请求。这安全性是相当低的，没有特殊情况不推荐使用。

#### Non-Simple Requests 非简单请求

CORS协议规定，如果某个请求不能严格吻合之前描述的简单请求规范，就必须使用复杂的两步握手方式。

握手的具体实现是先给目标URL发送一个`OPTIONS` 请求，在里面用若干请求头作为参数描述其后真正的XMLHttpRequest的一些基本情况，请求头包含：

- Origin 协定源地址
- Access-Control-Request-Method 协定请求方法
- Access-Control-Request-Headers 协定请求头的信息

只有在返回的相应里包含以下响应头参数: Access-Control-Allow-Origin， Access-Control-Allow-Method 和 Access-Control-Request-Headers，这个我握手才算成功。在正确的握手之后，才能发送真正的请求。

**注意：** 处于性能的考虑设计，对特定的URL的检查结果可能会在客户端缓存一段时间。

#### 安全问题考虑

CORS协议已经把跨域问题简化到了极致，相应使用范围会越来越广，不过同样的新机制在各色程序员操作下也会带来新的安全问题。

1. HTTP 请求头注入，简单请求的请求头和响应头基本受浏览器的控制，如果攻击者通过自己的HTTP AGENT发请求，服务器端的Origin处理不完善就可能引起HTTP请求头注入
2. 滥用授权。最后提到的非简单请求，客户端缓存Option结果的情况，可能造成授权滥用。
3. 其他待发掘~

Enjoy It!