---
layout: post
title: "Restful Web API 设计最佳实践译文"
description: "Restful Web API 设计最佳实践译文"
category: Coding
tags: [code, restful, software design]
---

原文地址： [http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api](http://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api)

设计目标
------------------

- 基于web标准设计
- 对开发者和浏览器友好
- 简单，直观，容易保持一致性
- 对UI组件保持一定的灵活性
- 对修改维护应该是高效的

设计准则
---------------------

###API资源定义

resource的命名应该为名词（不能为动词），不能暴露无关的内部实现。
在你定义完成你的资源后，需要设计使用这些资源的操作，以及如何将这些操作映射到API上。 RESTful准则提供了`CRUD`操作和HTTP Method之间的映射关系：

	GET /tickets - 获取ticket列表
	GET /tickets/12 - 获取特定的ticket信息
	POST /tickets - 创建新的ticket
	PUT /tickets/12 - 更新#12的ticket
	PATCH /tickets/12 - 更新#12的部分字段
	DELETE /tickets/12 - 删除#12的ticket

###endpoint该定义为单数还是复数
坚持使用复数

###如何处理资源间的关系
如果一种资源依赖于另外的一种资源存在，RESTful也提供了设计实践

	GET /tickets/12/messages - Retrieves list of messages for ticket #12
	GET /tickets/12/messages/5 - Retrieves message #5 for ticket #12
	POST /tickets/12/messages - Creates a new message in ticket #12
	PUT /tickets/12/messages/5 - Updates message #5 for ticket #12
	PATCH /tickets/12/messages/5 - Partially updates message #5 for ticket #12
	DELETE /tickets/12/messages/5 - Deletes message #5 for ticket #12

相对的，如果一个资源是独立存在的，应该另外定义。可以为资源间关系定义一个关系资源。

###CRUD之外的操作

1. 属性的存取。通过操作来实现：比如一个avtivate操作能够映射到 `boolean activated`域，通过`PATCH`方法更新这个资源
2. 当作子资源处理。例如Github允许 star 一个 gist `PUT /gists/:id/star` unstar `DELETE /gists/:id/star`
3. 有时无法将一个操作映射到Restful的框架中，比如一个多资源的查找确实无法找到一个对应的资源，此时诸如`/search`这样的也许是最合理的设计

####使用SSL
API的设计要始终使用SSL，既可保证安全，二来只需要简单的交换`access token`而不用对每个API REQUEST签名验签

####版本控制
始终保持对你的API进行版本控制，这样不近能保证快速迭代，也能保证新旧API的平滑过度
对于`API的版本号是否应该包含在URL或者HEADER`里，目前还存在这争议。学术上认为应该包含在HEADER里，不过包含在URL当中那个可以给开发者更多的可控性，能够自行的选择所调用的API版本
作者本人推崇`官阶制`，URL包含主版本号（如V1），在HTTP header当中包含子版本号。这样可以保持API主版本的稳定，又能屏蔽小的版本修改

####结果集过滤，排序和查询
- Filtering: 通过唯一的字段查询参数实现过滤 `GET /tickets?state=open`
- Sorting： 跟Filtering类似，可以使用通用的`sort`参数来描述排序条件，多个排序条件之间可以通过逗号分割，用`-`表示降序
- Searching：有时Filtering不能够满足全文搜索的需求。

