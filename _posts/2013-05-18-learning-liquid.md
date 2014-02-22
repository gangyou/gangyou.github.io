---
layout: post
title: Liquid学习笔记
description: Liquid学习笔记
category: Blogging
tags: [Jekyll, Github Pages, Liquid]
---

[Liquid](https://github.com/Shopify/liquid)中有2种Markups:

-	Output

	Hello \{\{ title \}\}
-	Tag 非文本
	\{\% 对称的大括号加百分号 \%\}

输出Output
---------------
简单的输出如 
	Hello {{ name }}
另外输出还可以使用过滤器 Filter，如:
	Hello {{ 'tobi' | upcase }}
	Hello tobi has {{ 'tobi' | size }} letters!
	Helo {{ 'now' | date: "%Y %h" }}

###标准过滤器 Standard Filters
标准的Filter, 通过名字基本可以猜得出来，filter的用法类似Linux Pipeline，左边是右边的输入；对于Filter可以有输入参数。
例如plus，将左边数与右边数连接或相加， plus:1, 就代表左边数加1。

	- date
	- capitalize
	- downcase
	- upcase
	- first
	- last
	- join
	- sort
	- map
	- size
	- escape
	- escape_once
	- strip_html
	- strip_newlines
	- newline_to_br
	- replace
	- replace_first
	- remove
	- remove_first
	- truncate
	- truncatewords
	- prepend
	- append
	- minus
	- plus
	- times
	- divided_by
	- split
	- modulo

####Example:
	{% raw %}
	{{ 'foofoo' | replace:'foo','bar' }} #=> 'barbar'
	{{ 'barbar' | replace_first:'bar','foo' }} #=> 'foobar'
	{{ 'foobarfoobar' | remove:'foo' }} #=> 'barbar'
	{{ 'barbar' | remove_first:'bar' }} #=> 'bar'
	{{ 'bar' | prepend:'foo' }} #=> 'foobar'
	{{ 'foo' | append:'bar' }} #=> 'foobar'
	{{ 4 | minus:2 }} #=> 2
	{{ '1' | plus:'1' }} #=> '11', {{ 1 | plus:1 }} #=> 2
	{{ 5 | times:4 }} #=> 20
	{{ 10 | divided_by:2 }} #=> 5
	{{ "a~b" | split:~ }} #=> ['a','b']
	{{ 3 | modulo:2 }} #=> 1
	{% endraw %}

###标签 Tags
Tags是用来表达模板中的页面逻辑。
当前支持的tag包含了：
-	assign 变量赋值 

{% raw %}
	{% assign var = value %}
{% endraw %}
-	capture Block tag that captures text into a variable (还没理解。。。)
-	case 类似switch
-	comment 注释
-	cycle 在一组备选值当中循环
-	for 循环
-	if if/else
-	include 包含另外的模板
-	raw 临时停止处理markup
-	unless	条件判断

####Case
{% raw %}
	{% case condition %}
	{% when 1 %}
	hit 1
	{% when 2 or 3 %}
	hit 2 or 3
	{% else %}
	... else ...
	{% endcase %}
{% endraw %}

####Cycle
{% raw %}
	{% cycle 'one', 'two', 'three' %}
	{% cycle 'one', 'two', 'three' %}
	{% cycle 'one', 'two', 'three' %}
	{% cycle 'one', 'two', 'three' %}

	will result in

	one
	two
	three
	one
{% endraw %}

####Comments
{% raw %}
	We made 1 million dollars {% comment %} in losses {% endcomment %} this year
{% endraw %}

####Raw
{% raw %}
	\{% raw %\}
	  In Handlebars, {{ this }} will be HTML-escaped, but {{{ that }}} will not.
	\{% endraw %\}
{% endraw %}

####If / else
	{% raw %}
	{% if user %}
	  Hello {{ user.name }}
	{% endif %}

	{% if user.name == 'tobi' %}
	  Hello tobi
	{% elsif user.name == 'bob' %}
	  Hello bob
	{% endif %}

	{% if user.name == 'tobi' or user.name == 'bob' %}
	  Hello tobi or bob
	{% endif %}

	{% if user.name == 'bob' and user.age > 45 %}
	  Hello old bob
	{% endif %}

	{% if user.name != 'tobi' %}
	  Hello non-tobi
	{% endif %}

	# Same as above
	{% unless user.name == 'tobi' %}
	  Hello non-tobi
	{% endunless %}

	# Check if the user has a credit card
	{% if user.creditcard != null %}
	   poor sob
	{% endif %}

	# Same as above
	{% if user.creditcard %}
	   poor sob
	{% endif %}

	# Check for an empty array
	{% if user.payments == empty %}
	   you never paid !
	{% endif %}

	{% if user.age > 18 %}
	   Login here
	{% else %}
	   Sorry, you are too young
	{% endif %}

	# array = 1,2,3
	{% if array contains 2 %}
	   array includes 2
	{% endif %}

	# string = 'hello world'
	{% if string contains 'hello' %}
	   string includes 'hello'
	{% endif %}
	{% endraw %}

####For loops
	{% raw %}
	{% for item in array %}
	  {{ item }}
	{% endfor %}
	{% endraw %}

在for循环中还包含了很多辅助变量

	-	forloop.length # => for的循环总次数
	-	forloop.index  # => 当前循环的index，从1开始
	-	forloop.index0 # => 当前循环的index，从0开始
	-	forloop.rindex # => 当前循环剩余次数
	-	forloop.rindex0 # => 当前循环剩余次数，从0开始
	-	forloop.first   # => 是否是循环的第一次
	-	forloop.last    #=> 是否是循环的最后一次

通过offset:int 控制循环的起始， limit: int控制循环的次数， reversed 反转循环
	{% raw %}
		# array = [1,2,3,4,5,6]
		{% for item in array limit:2 offset:2 %}
		  {{ item }}
		{% endfor %}
		# results in 3,4
		{% for item in collection reversed %} {{item}} {% endfor %}
	{% endraw %}

Python Range重现~
{% raw %}
	# if item.quantity is 4...
	{% for i in (1..item.quantity) %}
	  {{ i }}
	{% endfor %}
	# results in 1,2,3,4
{% endraw %}
