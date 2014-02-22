---
layout: post
title: "Python格式化迷你语言"
description: "python mini format language. Python内置了一个格式化字符串的mini语言，可以完成大部分的格式化任务"
category: Coding
tags: [Python]
---
对于现在大部分的应用程序，处理最多的数据类型应该就是字符串了。对于很多格式化需求，高手和初学者的区别就在于：高手会用format函数去处理格式化任务，初学者做的更多的是用字符串拼接来处理。

Python作为一个Everything is Object的函数式编程语言，会格式化字符串的工作提供更大的自由度和灵活性。除了C Style的`%x`语法，还提供了Java的String Format语法，借助强大的内置数据类型List, Turple, Dict，用Python的字符串格式化可以完成更复杂的任务。

要活用Python的字符串格式化语法，需要掌握2块内容：**Format String Syntax** 和 **Format Specification Mini-Language** 中文我翻译的可能不准确，暂且叫**格式化字符串语法** 和 **格式化专用迷你语言** 吧。

## 格式化字符串语法

---

包含格式化信息的字符串形如`' Hello {name}'` 被**{}**包裹的部分就是格式化字符串了，在{}外面的部分，在进行格式化时候都将原样输出，{}的转义使用`{{` 和 `}}`。

格式化字符串的语法用上下文无关文法表示为：

    replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
    field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
    arg_name          ::=  [identifier | integer]
    attribute_name    ::=  identifier
    element_index     ::=  integer | index_string
    index_string      ::=  <any source character except "]"> +
    conversion        ::=  "r" | "s"
    format_spec       ::=  <described in the next section>
    
对每个部分做下解释：

* replacement_field: 格式化的替换部分
* field_name: 替换域的名称，是一个arg_name的类型。这个arg_name可以是一个合法的标示符或者一个整型数。这些跟后面format的参数传递有关。如果是一个标示符，format函数通过key,value传值，如果是整型，则按照参数的位置传值。如果arg_name是一个对象，还可以使用**.**操作符访问属性，如果是一个**Sequence** 或者 **DIct**，通过**[]**操作符以索引访问。
* arg_name: 参加field_name的描述
* attribute_name: 通过**.**操作符访问的属性名
* element_index: 通过数字下表或者键值访问
* index_string: 键值
* conversion: **r或者s**，`r`表示使用参数`repr(argument)`方法的返回值填充，`s`表示使用参数的`str(argument)`返回值填充（默认）。形如`{name!r}`
* format_spec: 这块就是**Format Specification Mini-Language**，下一节给出解释。形如`{name:format_spec}`
* 如果什么都不指定，比如`"{} welcome to {}"`，则格式化时候就Python会自动把其中的**{}**按照出现顺序填充参数。也就是说这句和`{0} welcom to {1}`是等价的。


### Examples

    "First, thou shalt count to {0}" # format的第一个参数
    "Bring me a {}"                  # 隐式的指定第一个参数
    "From {} to {}"                  # 和 Form {0} to {1} 等价
    "My quest is {name}"             # 命名参数name
    "Weight in tons {0.weight}"      # 第一个参数的weight属性
    "Units destroyed: {players[0]}"  # players的第一个元素
    "Harold's a clever {0!s}"        # 第一个参数的str()返回值
    "Bring out the holy {name!r}"    # 第一个参数的repr()返回值
    
## 格式化专用迷你语言

---

格式化专用迷你语言(Format Specification Mini-Language)就是在**replacement_filed**中冒号后面的部分。它的上下文无关文法是这样的：

    format_spec ::=  [[fill]align][sign][#][0][width][,][.precision][type]
    fill        ::=  <a character other than '{' or '}'>
    align       ::=  "<" | ">" | "=" | "^"
    sign        ::=  "+" | "-" | " "
    width       ::=  integer
    precision   ::=  integer
    type        ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
    
其中每一个部分的含义如下：

* fill: 填充字符，在实际宽度小于用`width`指定的宽度时，用fill指定的字符进行填充。默认为空格
* align: 对齐方式，选项有：

    选项 | 含义
    ------ | --------
    <|左对齐，并尽可能用fill字符填充（默认）
    \> | 右对齐
    = | 只对数字类型有效，右对齐不过在符号后面增加填充
    ^ | 居中对齐

* sign: 只对数字格式化有效。选项有：

    选项 | 含义
    ------- | -------
    \+ | 始终显示正负符号
    \- | 只显示负数符号，不显示正数符号
    空格 | 在正数前面显示空格，在负数前面始终显示负数符号

* \#: 只对整数的二进制，八进制和十六进制的输出有效，在格式化结果前显示`0b, 0o, 0x`
* 0: 在宽度前面的**0**表示同时设置 `sign=+, fill=0`, 始终显示符号并用0进行填充 
* width: 默认为显示的内容宽度，如果设置为一个正整数，则表示显示的最小宽度
* ,: 只针对数字有效，是否显示千分位
* .precision: 精度，precision表示的数字，对浮点数有效。表示保留小数点之后几位，**注意：不会进行四舍五入**
* type: 决定格式化字符串如何显示，选项比较多：

对于字符串类型

Type | 含义
--- | ---
s | 就以字符串显示，默认

对于字符串类型，基本不用去理这个字段啦。

整型类型的显示

Type | 含义
--- | ---
b | 二进制显示
c | 字符显示，将整型转换为对应的Unicode字符
d | 十进制数字
o | 八进制数字
x | 十六进制数字，其中字母用小写显示
X | 十六进制数字，其中字母用大写显示
n | The same as d，不过设置为n会尝试着进行本地化的显示

浮点数的显示，如果对整型也进行了如下设置，那么整型也会被格式化成浮点数

Type | 含义
--- | ---
e | 科学计数法显示
E | 科学计数法显示，e大写
f | 定点数，默认为6位，关于什么是定点数，请戳 [百度百科-定点数](http://baike.baidu.com/view/686808.htm)
g, G, n | 这三个说实话，看英文文档我没看懂。。。求高人解释
% | 百分比数

### Examples

宽度与对齐

    >>> '{:<30}'.format('left aligned')
    'left aligned                  '
    >>> '{:>30}'.format('right aligned')
    '                 right aligned'
    >>> '{:^30}'.format('centered')
    '           centered           '
    >>> '{:*^30}'.format('centered')  # use '*' as a fill char
    '***********centered***********'

符号

    >>> '{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
    '+3.140000; -3.140000'
    >>> '{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
    ' 3.140000; -3.140000'
    >>> '{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
    '3.140000; -3.140000'


进制的转换

    >>> # format also supports binary numbers
    >>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
    'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
    >>> # with 0x, 0o, or 0b as prefix:
    >>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
    'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'


千分位

    >>> '{:,}'.format(1234567890)
    '1,234,567,890'


百分数和精度

    >>> points = 19.5
    >>> total = 22
    >>> 'Correct answers: {:.2%}'.format(points/total)
    'Correct answers: 88.64%'

