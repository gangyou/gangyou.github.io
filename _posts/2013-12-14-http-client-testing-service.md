---
layout: post
title: "HTTP客户端测试网站"
description: "http client testing service HTTP客户端测试网站"
category: Coding
tags: [Python, HTTP]
---

在学习 [Python Requests](http://docs.python-requests.org/en/latest/) 的时候，好多例子都用到了 `http://httpbin.org` 的Restful 服务，就特意访问过去看了下，发现了这个有趣的网站： [HTTP Client Test Service](http://htttpbin.org)。

这是一个专门提供HTTP测试的网站，全站用Restful方式提供服务，向各个`Endpoint`发出HTTP请求，网站会根据返回HTTP标准化的`Response HTTP Headers`，同时还会将Header的信息以`JSON`的形式返回。可以作为学习测试HTTPClient的工具站点。

目前网站提供了以下的**Endpoint**：

Endpoint | 用途
----- | -----
/ip | 返回客户端IP
/user-agent | 返回客户端浏览器类型
/headers | 返回请求报头
/get | 返回GET数据
/post | 返回POST数据
/put | PUT
/patch | PATCH
/delete | DELETE
/gzip | 返回GZIP编码数据
/status/:code | 用于测试各类状态码，/status/200 就是HTTP Code 200
/redirect-to?url=foo | 到foo url的重定向
/cookies | cookie的测试
/basic-auth/:user/:passwd | 测试HTTPBasic Auth

基本提供了HTTP 1.1中包含的一切， Enjoy It! ^_^


