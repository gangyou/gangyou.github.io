---
layout: post
title: "Python super 方法的理解"
description: "Python super method Python super 方法的理解"
category: Coding
tags: [Python]
---

Python的教程当中，我觉得讲的最不清楚的就是继承。这应该和Python的价值观有关，

    Flat is better than nested.
    扁平胜于嵌套
                                               ————The zen of python
                                               
(插播一句，通过import this 查看 the zen of python)

Python更倾向于通过组合(mixin)来解决继承问题。

但是！很多库你不得不继承！那这个时候我们的主角`super`就出现了。

### super Doc

---

在Python Document中，该方法的解释是这样的：

    super(type, [, object-or-type])
        Return a proxy object that delegates method calls to a parent or sibling class of type. This is useful for accessing inherited methods that have been overridden in a class. 
        Note: super() only works for new-style classes
        There are two typical use cases for super. In a class hierarchy with single inheritance, super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable. This use closely parallels the use of super in other programming languages.
    The second use case is to support cooperative multiple inheritance in a dynamic execution environment. This use case is unique to Python and is not found in statically compiled languages or languages that only support single inheritance. This makes it possible to implement “diamond diagrams” where multiple base classes implement the same method. Good design dictates that this method have the same calling signature in every case (because the order of calls is determined at runtime, because that order adapts to changes in the class hierarchy, and because that order can include sibling classes that are unknown prior to runtime).
        返回父类或者兄弟类的代理对象。用于访问被覆盖的继承方法。
        注意： super() 只对new-style classes 有效
        super有2个典型的用途。在单继承的类中，不显式指定父类就可以访问父类方法，代码更易维护。这种用法跟其他语言中super方法的用法十分类似。
        还有一种是多继承访问多父类当中定义的同名方法。这个Document里没仔细说明，我也就不仔细翻译了。
        
###  访问父类的方法
        
在Doc中，注意到super只对 **new-style classes**有效。在Python 2.2之前的类都是**old-style classes**。Python 2.2之后，如果在定义类的时候这么写`class A(object):`那这个就是new的；如果这么写`class A:`，那么就是old的。差别就在是不是都继承自object，这个就很有java继承设计的意思了。

那同样的，子类中访问父类方法也有old和new的了。

#### 一个old的用法是这样的：

{% highlight python linenos %}
class A:
    def method(self, arg):
        print arg

class B(A):
    def method(self, arg):
        A.method(self, arg)

b =  B()
b.method('hello') # 'hello'
{% endhighlight %}

#### 那一个new的用法是这样的：

{% highlight python linenos %}
class A(object):
    def method(self, arg):
        print arg
        
class B(A):
    def method(self, arg):
        super(B, self).method(arg)

b = B()
b.method('hello') # 'hello'
{% endhighlight %}

#### 我不需要知道我的父亲是谁

我的机器上是Python 2.7.3，两种方法都工作的很好。差别就在本节的标题，我不需要知道我的父亲是谁！我也可以活的很好！有点韩剧的味道了，呵呵。

在old的用法当中，B中调用父类方法通过`A.methid`实现，这就是说B和A的关系被绑定了，而不是Python喜欢的动态的。目前我们程序规模较小，`A.xmethod`这样的调用还很少。不过想像一下，有一天你的B找到了一个养父，不认自己的生父了。

`class B(C)`！那所有代码中对A的调用都要改成C，生父在我的生活中留下了很多照片啊、衣服啊、车子啊、房子啊，为了不让养父知道，都要销毁！！是的，在old的方法中，车子房子也不得不还回去^_^

那new用法就不一样了，只要改掉B的继承声明就可以了！

### 还有一个问题

父亲是old-style的，孩子是new-style的，那必然父子之间有代沟啊！Python中也是一样，不过父亲在Python脾气相当火爆，如果孩子主动找他，他还要发火，raise一个Error

{% highlight python linenos %}
class A:
     def method(self) : print 'hello'
 
class B(A):
    def method(self): super(B, self).method()

b = B()
b.method()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in method
TypeError: must be type, not classobj
{% endhighlight %}

### 为什么是TypeError

super提供的不是一个class，是一个proxy type有没有？所以就must be a type啦~具体怎么实现的。。。我也不知道，看了源码是C的。。。
        

                                                        

    

