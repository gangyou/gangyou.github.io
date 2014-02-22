---
layout: post
title: "Ant 自定义任务之间数据或对象的共享"
description: "Ant share data and object between user define tasks. Ant 自定义任务之间数据或对象的共享"
category: Coding
tags: [Ant, Java]
---
问题
--------------------

在编写Ant自定义任务时，产生了这样一个问题：

1. Task1 完成了一系列操作，将操作结果存储在一个静态域当中
2. Task2 要先读取这个静态域，根据取值做相应的操作

结果Task2当中怎么都取不到这个静态域更改后的值！原因是什么？在2个自定义任务之间怎么共享对象呢？

`Apache Ant Manual`中有这么一段：

	If you are defining tasks or types that share the same classpath with multiple taskdef or typedef tasks, the corresponding classes will be loaded by different Java ClassLoaders. Two classes with the same name loaded via different ClassLoaders are not the same class from the point of view of the Java VM, they don't share static variables and instances of these classes can't access private methods or attributes of instances defined by "the other class" of the same name. They don't even belong to the same Java package and can't access package private code, either.

	The best way to load several tasks/types that are supposed to cooperate with each other via shared Java code is to use the resource attribute and an antlib descriptor. If this is not possible, the second best option is to use the loaderref attribute and specify the same name for each and every typedef/taskdef - this way the classes will share the same ClassLoader. Note that the typedef/taskdef tasks must use identical classpath definitions (this includes the order of path components) for the loaderref attribute to work.

翻译结果如下：

	如果你通过多个taskdef或typedef定义了自己的tasks和types，并且他们有用相同的classpath，那么相应的类会通过不同的`ClassLoader`加载。对于JVM来说，通过不同的ClassLoader加载的同名类，并不是同一个类。自然，他们之间无法共享静态的变量和实例。他们甚至都不属于同一个包。
	
	加载需要通过共享Java对象互相协作的Ant tasks/types的最好方法是，使用`resources`属性和`antlib`属性定义任务和类型。次好的方式是通过指定`loaderref`属性，通过同一个ClassLoader来加载这些写作的tasks/types。

这下问题就很清楚了～
