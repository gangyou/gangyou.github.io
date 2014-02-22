---
layout: post
title: "Python数字转大写金额"
description: "python translate digital numbers to chinese number."
category: Coding
tags: [Python, Coding]
---
下午在看Python相关代码，看到一个兄弟用来实现数字转大写金额的程序。整个代码80行，而且逻辑相当复杂，实在看不下去了，动手写了一个。

代码如下：

{% highlight python linenos %}
    # coding:utf-8
    # 将数字转换为大写数字
    
    CNDIGIT = ['','壹','贰','叁','肆','伍','陆','柒','捌','玖']
    CNUNIT = ['','拾','佰','仟','万','十万','百万','千万','亿']
    
    def to_chinese_digital(number, unit=0):
    	results = []
    	# 当前处理的数字位
    	unit, _number = 0, number
    	while _number:
    		_number, remainder = divmod(_number, 10)
    		chinese_digit = CNDIGIT[remainder] + CNUNIT[unit]
    		unit += 1
    		results.append(chinese_digit)
    
    	return ''.join(reversed(results))
    
    if __name__ == '__main__':
    	assert to_chinese_digital(1234) == '壹仟贰佰叁拾肆', '1234 翻译成中文是 壹仟贰佰叁拾肆'
    	assert to_chinese_digital(12345) == '壹万贰仟叁佰肆拾伍','12345 翻译成中文是 壹万贰仟叁佰肆拾伍'

{% endhighlight %}