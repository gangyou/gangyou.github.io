---
layout: post
title: Django入门第三课-Model继承关系 
description: Django Lesson 3
category: Coding
tags: [coding, python, django, models]
---

Django的模型继承和Python中的模型集成类似，唯一需要决定的是父模型的可见性，是让父模型单独建立一张表，还是仅仅让父模型持有公共信息，然后通过子类去访问修改这些信息。

根据上面的策略，Django提供了三种继承方式：

- Abstract base classes 抽象基类方式，父模型仅仅保存信息，但不暴露出来
- Multi-table inheritance 多表继承，继承已经存在的模型，并且希望继承体系中每个模型都拥有自己的一张表
- Proxy models 代理模型，仅仅需要Python级别的model特性，不需要将该类映射到数据库中

###抽象基类
在`Meta`类中设置 `abstract=True`，就可以把一个model设置为抽象model。继承该基类的子类模型，会拥有基类的字段属性。注意：子类中不能包含和基类同名的字段，Django会抛出异常

{% highlight python linenos %}
class CommonInfo(models.Model):
	name = models.CharField(max_length=100)
	age = models.PositiveIntegerField()

	class Meta:
		abstract = True

class Student(CommonInfo):
	home_group = models.CharField(max_length=5)
{% endhighlight %}

Student模型会具有3个字段：name, age, home_group. CommonInfo没办法作为Django Model进行访问

####Meta继承
子模型在创建时如果没有声明Meta，会自动继承父类的Meta，如果子模型想扩展父类的Meta，可以在定义时自行扩展

{% highlight python linenos %}
class CommonInfo(models.Model):
    ...
    class Meta:
        abstract = True
        ordering = ['name']

class Student(CommonInfo):
    ...
    class Meta(CommonInfo.Meta):
        db_table = 'student_info'
{% endhighlight %}

Django对Meta类的装载有一项调整，就是会把Meta的`abstract=False`，通过这种方式保证抽象类的子类为非抽象类

####Be careful with related_name
大概意思是，在继承具有ForeignKey或者ManyToManyField，并且在这些字段中已经指定了`related_name`的情况下，需要注意，要这样设置`related_name = "%(app_label)s_%(class)s_related"` 避免继承后关联表的重建

###多表继承 Multi-table inheritance
多表继承是在每个Model都持有自己的数据表的情况下

{% highlight python linenos %}
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField()
    serves_pizza = models.BooleanField()
{% endhighlight %}

在Place中的所有字段，Restaurant模型都能访问，这是通过一个自动建立的`OneToOneField`来实现的，在上例中会在`Restaurant`表中建立`place_ptr_id`字段，建立一对一联系

###代理模式
有时只是在Python层面改变部分模型的行为，比如改变默认排序等，此时就是代理模型 Proxy Model发挥作用的时候了
定义一个Proxy Model只需要在Meta中设置`proxy = True`就可以了
{% highlight python linenos %}
class MyPerson(Person):
	class Meta:
		proxy = True
	def do_something(self):
		...

>>> p = Person.objects.create(first_name = "foobar")
>>> MyPerson.objects.get(first_name="foobar")
<MyPerson: foobar>
{% endhighlight %}
