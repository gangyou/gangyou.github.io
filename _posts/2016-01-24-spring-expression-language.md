---
layout: post
title: Spring Expression Language 4 学习笔记
description: Spring Expression Language 4 memo
category: Coding
tags: [Spring, Java, J2EE]
---

## 前言

时隔多年重新开始学习Spring，之前只用过Spring 2，掰掰指头已经过了快10年了。
看到书里提到了SpEL，一头雾水，在2的时代好像从来没见过。把学习到的做个总结。

## SpEL概述

SpEL是Spring内置的表达式语言，语法与OGNL等其他表达式语言十分类似。SpEL设计之初就是朝着做一个表达式语言的通用框架，可以独立运行。

## SpEL的主要相关类

SpEL对表达式语法解析过程进行了很高的抽象，抽象出解析器、表达式、解析上下文、估值(Evaluate)上下文等对象，非常优雅的表达了解析逻辑。主要的对象如下：

| 类名 | 说明|
|----|----|
| ExpressionParser| 表达式解析器接口，包含了`(Expression) parseExpression(String)`, `(Expression) parseExpression(String, ParserContext)`两个接口方法|
|ParserContext|解析器上下文接口，主要是对解析器Token的抽象类，包含3个方法：`getExpressionPrefix`,`getExpressionSuffix`和`isTemplate`，就是表示表达式从什么符号开始什么符号结束，是否是作为模板（包含字面量和表达式）解析。一般保持默认。|
|Expression|表达式的抽象，是经过解析后的字符串表达式的形式表示。通过`expressionInstance.getValue`方法，可以获取表示式的值。也可以通过调用`getValue(EvaluationContext)`，从评估（evaluation)上下文中获取表达式对于当前上下文的值|
|EvaluationContext|估值上下文接口，只有一个setter方法：`setVariable(String, Object)`，通过调用该方法，可以为evaluation提供上下文变量|

完整的例子：

```
{%highlight java%}
public static void main(String[] args) {        
    String greetingExp = "Hello, #{ #user }";                             （1）     
    ExpressionParser parser = new SpelExpressionParser();           （2）
    EvaluationContext context = new StandardEvaluationContext();        
    context.setVariable("user", "Gangyou");        (3)

    Expression expression = parser.parseExpression(greetingExp, 
        new TemplateParserContext());     (4)
    System.out.println(expression.getValue(context, String.class)); (5)
}
{% endhighlight %}
```

代码解释：
1. 创建一个模板表达式，所谓模板就是带字面量和表达式的字符串。其中**#{}**表示表达式的起止，`#user`是表达式字符串，表示引用一个变量。
2. 创建表达式解析器，SpEL框架创建了一个语言无关的处理框架，所以对于其他的表达式语言，完全可以创建不同的ExpressionParser。在这里我们学习的是SpEL所以使用`SpelExpressionParser()`
3. 通过`evaluationContext.setVariable`可以在上下文中设定变量。
4. 解析表达式，如果表达式是一个模板表达式，需要为解析传入模板解析器上下文。如果不传入模板解析器上下文，指定表达式为模板，那么表达式字符串`Hello, #{ #user }`，解析器会首先去尝试解析`Hello`。例子中的模板表达式，与`'Hello, ' + #user`是等价的。
5. 使用`Expression.getValue()`获取表达式的值，这里传入了Evalution上下文，第二个参数是类型参数，表示返回值的类型。

## SpEL语法

本节介绍下SpEL中的各类语法，在语法中会发现很多熟悉的影子，比如Java，JavaScript, Groovy等等。依次介绍SpEL中的

- 字面量
- 数组和Map字面量
- 二元操作符和三元操作符
- 来自Groovy的操作符
- 数组列表和Map的访问
- Java Bean属性访问
- Java Bean方法调用
- Java 类型访问
- Java 实例访问

### 字面量

SpEL支持如下类型的字面量：

|类型|说明|示例|
|---|---|---|
|数字|支持任何数字类型，包括了各种进制的数字，科学计数法等|6.0221415E+23，0xFFFFFFFF|
|布尔量||true, false|
|字符串|用单引号包围的字符串，单引号要用2个单引号转义|'Gangyou''s, Blog'|
|日期| |没写成功 //TODO|
|null|直接转成字符串null|null|

### 属性

SpEL对属性的访问遵循Java Bean语法，对于表达式中的属性都要提供相应的setter。

比如这样一个Bean:

```
{%highlight java%}
private static class Person {    
    private String firstName;    
    private String lastName;    
    public Person(String firstName, String lastName) {        
         this.firstName = firstName;        
         this.lastName = lastName;    
    }    
    public String getFirstName() {        
        return firstName;    
    }    
    public String getLastName() {        
        return lastName;    
    }
}
{% endhighlight %}
```

表达式`firstName + ' ' + lastName`就等价于`person.getFirstName() + " " + person.getLastName()`。如果属性本身是对象，还支持嵌套属性，如`person.address.city`，就等价于`person.getAddress().getCity()`

### 数组、列表和Map

数组和列表都可以用过数字下标进行访问，比如`list[0]`。

Map的访问就类似JavaScript的访问方式，使用key访问。例如java代码`map.put("name", "gangyou")`其中的map对象，可以通过`map['name']`获取到字符串**gangyou**。

### 内联的数组和Map

Spel允许在表达式内创建数组（列表）和Map，如`{1,2,3,4}`,`{'firstName': 'Gang', 'lastName': 'You'}`。

### 方法调用

SpEL使用java的相同语法进行方法调用，如`'Hello`.concat(', World!')`，输出** Hello, World!**。

### 类型

SpEL中可以使用特定的Java类型，经常用来访问Java类型中的静态属性或静态方法，需要用`T()`操作符进行声明。括号中需要包含类名的全限定名，也就是包名加上类名。唯一例外的是，SpEL内置了`java.lang`包下的类声明，也就是说`java.lang.String`可以通过`T(String)`访问，而不需要使用全限定名。

两个例子： `T(Math).random()` 或 `T(java.lang.Math).random()`

### 创建实例

使用new可以直接在SpEL中创建实例，需要创建实例的类要通过全限定名进行访问，如：`new java.util.Date().now()`

### 二元操作符

SpEL中的二元操作符同Java中的二元操作符，包括了数学运算符、位运算符、关系运算符等等。

### 三元操作符

SpEL的三元操作符主要是 ** if else then ** 操作符 `condition ? true statement : false statement`与Java中的一致。

另外一个就是借鉴自Groovy的 Elvis 操作符`?:`，Elvis就是猫王！

![22571c16e399948037ed26756945c6fd.jpg](http://upload-images.jianshu.io/upload_images/1334699-4f1ee84cf12e7674.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这个操作符的样子就跟猫王的发型一样：）。

举一个例子

```
{%highlight java%}
String expressionStr1 = " name != null ? name : 'Default Value'";
String expressionStr2 = "name ?: 'Default Value'";
{% endhighlight %}
```

上面的两个表达式都是先判断 `getName() `的返回值是不是null，如果是就返回`Default Value`，通过下面的Elvis操作符可以让代码更加的清晰。

### 安全访问符

同样借鉴自Groovy，在SpEL中引入了安全访问符**Safe Navigator Operator**——`.?`，解决了很大问题。相信每个Javaer都遇到过NullPointException的运行时异常，通常是对象还未实例化或者找不到对象，却访问对象属性造成的。通过安全访问符就可以避免这样的问题。

```
{%highlight java%}
String expStr = "thisMayBeNull.?property"
{% endhighlight %}
```

这句表达式在求值的时候，不会因为`thisMayBeNull`是Null值而抛出NullPointException，而是会简单的返回null。个人认为此处结合Elvis操作符，是一个很完善的处理方式。

### 集合选择

同样借鉴自Groovy，SpEL提供了集合选择语法，如下面的例子：

```
{%highlight java%}
List<Inventor> list = (List<Inventor>) parser.parseExpression(
        "Members.?[Nationality == 'Serbian']").getValue(societyContext);
{% endhighlight %}
```

如果Members List不是Null，则在列表中选择`getNationality() == 'Serbian'`的对象集合返回。这个很类似于Java 8中的`stream and filter`方式，只是更加的简洁。

在`[]`中间可以利用任何的布尔表达式，创建筛选条件。例如`age > 18`，`name.startsWith('You')`等等。

## 自定义函数

SpEL提供了Java的基础功能，也引入了3个借鉴自Groovy的特性语法提供更为简洁的表达能力。作为一款设计为框架的语言，更提供了自定义的扩展能力。

比如下面的例子：

```
{%highlight java%}
public abstract class StringUtils {

    public static String reverseString(String input) {
        StringBuilder backwards = new StringBuilder();
        for (int i = 0; i < input.length(); i++)
            backwards.append(input.charAt(input.length() - 1 - i));
        }
        return backwards.toString();
    }

    public static void main(String[] args){
        ExpressionParser parser = new SpelExpressionParser();
        StandardEvaluationContext context = new StandardEvaluationContext();

        context.registerFunction("reverseString",
        StringUtils.class.getDeclaredMethod("reverseString", new Class[] { String.class }));

        String helloWorldReversed = parser.parseExpression(
            "#reverseString('hello')").getValue(context, String.class);
    }
}
{% endhighlight %}
```

通过使用`StandardEvalutinContext.registerFunction`可以注册自定义的函数，唯一的一点要求就是需要在表达式中通过`#注册函数名`的方式引用函数。

## 参考资料

[Spring Expression Language 官方文档](http://docs.spring.io/spring/docs/current/spring-framework-reference/html/expressions.html) 
 

