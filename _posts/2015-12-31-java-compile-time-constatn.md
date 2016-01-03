---
layout: post
title: Java Compile-time Constant 编译时常量
description: 在Java中遇到的编译时常量问题，JDK1.8 规范中对于编译时常量的解释
category: Java
tags: [Java]
---

# Java Compile-time Constant 编译时常量

## 问题描述

如何将非字符串常量转为字符串常量？`toString`和 `String.valueOf` 貌似都无法编译。

在给注解属性赋值的时候：

> private final static String MAX_VALUE_AS_STRING = Long.toString(Long.MAX_VALUE);
> ...
> @Annotation(value = MAX_VALUE_AS_STRING)

编译器一直报错：

> attribute must be constant 值类型必须是常量

`MAX_VALUE_AS_STRING` 不是明明就是个常量，而且是运行时常量啊。而且在官方的文档中，明明就有 `Integer.MAX_VALUE / 2`的说明。

为了搞清楚这一点，还是要从官方文档入手，细细分析什么是常量。

**## Java编译时常量解释**

 首先，编译器告诉了你这个属性必须是个常量值，但是并没有告诉你，这个属性其实必须是一个**编译时常量值**。所谓编译时常量就是在编译阶段已经可以确定其值的常量。

 Oracle的官方文档 [15.28 Constant Expressions](https://docs.oracle.com/javase/specs/jls/se7/html/jls-15.html#jls-15.28) 也详细的解释了，什么是 ** Compile-time Constant **

```
1. 原始类型字面量，或者String字面量
2. 能转型为原始类型字面量，或String字面量的常量
3. 一元运算符（+,-,~,!，但不包含++, --) 和1，2组成的表达式 
4. 多元运算符（*，/和%）和1，2组成的表达式
5. 附加运算符( additive operators) （+ 或 -）与之前几条组成的表达式
6. 位移运算符（<<，>>, >>>）和之前几条组成的表达式
7. 关系运算符（<,<=,>,>= ，不包括 instanceof）与之前几条组成的表达式
8. 关系运算符（==，!=）与之前几条组成的表达式
9. 位运算符（&, ^, |）与之前几条组成的表达式
10. 条件与和条件或运算符（&&, ||) 与之前几条组成的表达式
11. 三元运算符 (？：）和之前几条组成的表达式
12. 带括号的表达式，括号内也是常量表达式
13. 引用常量变量的简单变量 [§6.5.6.1](https://docs.oracle.com/javase/specs/jls/se7/html/jls-6.html#jls-6.5.6.1)
14. 类中的常量变量引用，使用类的全限定名或类名进行引用（String.class)
```

由上述14条规则组成的常量成为编译时常量。

所以针对上一个问题，任何的方法调用其实都不在描述范围当中。因此不管是使用 `Long.toString(Long.MAX_VALUE)` 还是使用 `String.valueOf(Long.MAX_VALUE)`，在编译时都是非法的。

## 解决方案

既然不能使用方法调用，进行类型转换，如何实现将 Long.MAX_VALUE 转换为常量字符串呢？
其实很简单：

> public static final String MAX_VALUE_AS_STRING = Long.MAX_VALUE + "";

这个方式就符合原始类型字面量和String字面量的二元运算这条规则。

终于搞明白了：）

