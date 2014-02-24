---
layout: post
title: Cross Document Messaging 简介
categories: HTML5, Javascript
tags: HTML5, javascript, CDM, postMessage
date: 2014-02-24 19:17:00 +0800
---

上一篇文章 [CORS跨域资源共享介绍](2014/02/23/cors-introduction.html)，介绍了在现在浏览器中跨域Ajax的方法，本文记录下现代浏览器中的 **Cross Document Messaging API**，即跨文档通信API。

听着很大，其实就2个API：

- otherWindow.postMessage(message, otherOrigin)
  - otherWindow: 对接收信息页面的window应用。可以是页面中iframe的`contentWIndow`属性；`window.open` 的返回值； 通过name或下标从`window.frames` 取到的值
  - message: 要发送的数据，字符串类型
  - targetOrigin: 用于限制`otherWindow`源安全策略的源， "*"表示不做限制

- window.addEventListener('message', handler)

现代浏览器都将支持这个功能：Chrome 2.0+、Internet Explorer 8.0+, Firefox 3.0+, Opera 9.6+, 和 Safari 4.0+， 用来支持基于web的实时消息传递。

### 代码示例

--- 

*假设 a.com/index.html 的代码如下：*

{% highlight html %}
<iframe id="ifr" src="b.com/index.html"></iframe>  
<script type="text/javascript">  
window.onload = function() {  
    var ifr = document.getElementById('ifr');  
    var targetOrigin = 'http://b.com';  
    //此处使用的源安全策略同js安全策略，具体可google SOP
    
    ifr.contentWindow.postMessage('I was there!', targetOrigin);  
};  
</script> 
{% endhighlight %}

*b.com/index.html 代码如下：*

{% highlight html %}
<script type="text/javascript">  
    window.addEventListener('message', function(event){  
        // 通过origin属性判断消息来源地址  
        if (event.origin == 'http://a.com') {  
            alert(event.data);    // "I was there!"  
            // 这里的source是访问不到a.com/html中的window对象的
            alert(event.source);
        }  
    }, false);  
</script> 
{% endhighlight %}

结束~






