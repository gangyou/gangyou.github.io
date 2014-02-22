---
layout: post
title: Django入门第二课-Model Field相关
description: Django第二课
category: Coding
tags: [coding, python, django, models]
---

Django notes
================

[Model](https://docs.djangoproject.com/en/dev/ref/models/)
------------------
###各种Fields
-	AutoField
-	BigIntegerField
-	BinaryField
-	BooleanField
-	CharField
-	CommaSeparatedIntegerField
-	DateField
-	DateTimeField
-	DecimalField
-	EmailField
-	FileField
-	FilePathField
-	FloatField
-	ImageField
-	IntegerField
-	IPAddressField
-	GenericIPAddressField
-	NullBooleanField
-	PositiveIntegerField
-	PositiveSmallIntegerField
-	SlugField
-	SmallIntegerField
-	TextField
-	TimeField
-	URLField

###关系 Fields
-	ForeignKey
-	ManyToManyField
-	OneToOneField
-	CharField fixed length
-	TextField no-fixed length
EmailField, URLField, IPAddressField based on CharField add -	some validation conditions
BooleanField & NullBooleanField: BooleanField only can be True -	or False, NullBooleanField can also be null
FileField: allow to upload a file to server and save the -	filepath in database, like -FilePathField-

####Fields 当中的常见属性

- null
	如果为True, Django会将空值存储为NULL, 默认为False

- blank
	是否允许为空

- choices
	一个二元元组的列表，表示字段可选值。第一个值表示数据库存储值，第二个值表示视图中显示的值。可以使用 `get_FOO_display` 方法显示对应的显示值。Foo为字段名称

{% highlight python linenos %}
	from django.db import models
	
	class Person(models.Model):
		SHIRT_SIZES = (
			('S', 'Small'),
			('M', 'Medium'),
			('L', 'Large'),
		)
		name = models.CharField(max_length=60)
		shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

	>>> p = Person(name="Fred Flintstone", shirt_size="L")
	>>> p.save()
	>>> p.shirt_size
	u'L'
	>>> p.get_shirt_size_display()
	u'Large'
{% endhighlight %}

- default
	默认值设置

-help_text
	显示为Form Widget时额外的帮助信息

- primary_key
	如果设置为True,则为主键。 如果不显式设置逐渐，Django将自动生成一个主键

- unique
	添加唯一性约束

###模型之间的关系
####外键

{% highlight python lineos %}
class Author(models.Model):
	name = models.CharField(max_length = 100)

class Book(models.Model):
	title = models.CharField(max_length = 100)
	author = models.ForeighKey(Author)
{% endhighlight %}

注:被引用的类定义在前面,不过可以用字符串代替 `'Author'`

####OneToMany
use ForeignKey

####ManytoMany
ManyToManyField 表示多对多关系，可以通过设置`through`s属性，指定多对多关系的关联表。

{% highlight python %}
	class Author(models.Model):
		name = models.CharField(max_length=100)

	class Book(models.Model):
		title = models.CharField(max_length=100)
		author = models.ManyToManyField(Author)

	class Authoring(models.Model):
		collaboration_type = models.CharField(max_length=100)
		book = models.ForeignKey(Book)
		author = models.ForeignKey(Author)

	# Pull a book off the shelf
	book = Book.objects.get(title="Moby Dick"

	# Get the book's author
	author = book.author

	# Get a set of the books the author has been credited on 
	books = author.book_set.all()

	# set related_name to change the set name 
	# In class Book author = models.ForeignKey(Author, related_name="books")
	books = author.books.all()

{% endhighlight %}

有时多对多关系还需要设定额外的属性，比如一个音乐家和乐团的例子。一个音乐家可以属于多个乐团，一个乐团可以拥有多个音乐家，音乐家和乐团之间就形成了典型的多对多关系。不过除了记录他们之间的关系之外，还会希望记录下音乐家加入乐团的具体时间，增加Date属性，通过上面提到的`through`实现

{% highlight python linenos %}
	class Person(models.Model):
		name = models.CharField(max_length=128)
		
		def __unicode__(self):
			return self.name

	class Group(models.Model):
		name = models.CharField(max_length=128)
		member = models.ManyToManyField(Person, through='Membership')

		def __unicode__(self):
			return self.name

	class Membership(models.Model):
		person = models.ForeignKey(Person)
		group = models.ForeignKey(Group)
		date_joined = models.DateField()
		invite_reason = models.CharField(max_length=64)

	>>> ringo = Person.objects.create(name="Ringo Starr")
	>>> paul = Person.objects.create(name="Paul McCartney")
	>>> beatles = Group.objects.create(name="The Beatles")
	>>> m1 = Membership(person=ringo, group=beatles,
	...     date_joined=date(1962, 8, 16),
	...     invite_reason= "Needed a new drummer.")
	>>> m1.save()
	>>> beatles.members.all()
	[<Person: Ringo Starr>]
	>>> ringo.group_set.all()
	[<Group: The Beatles>]
	>>> m2 = Membership.objects.create(person=paul, group=beatles,
	...     date_joined=date(1960, 8, 1),
	...     invite_reason= "Wanted to form a band.")
	>>> beatles.members.all()
	[<Person: Ringo Starr>, <Person: Paul McCartney>]
{% endhighlight %}

和普通的ManyToMany不同的是，不能通过`add`, `create`或赋值来创建关联关系。基于同样的原因，`remove`也被禁用，不过`clear`方法还是可用的

{% highlight python linenos %}
	#This will not work
	>>> beatles.members.add(john)
	# Neither will this
	>>> beatles.members.create(name="George Harrison")
	# And neither will this
	>>> beatles.members = [ john, paul, ringo, george]
{% endhighlight %}

使用中间关系模型，能够用集合管理对象对中间关系的额外属性进行查询

{% highlight python lineos %}
	# Find all the members of the Beatles that joined after 1 Jan 1961
	>>> Person.objects.filter(
		group__name='The Beatles',
		membership__date_joined__gt=date(1961,1,1))
	[<Person: Ringo Starr]
{% endhighlight %}

如果要获取membership的信息，需要直接查询Membership模型

{% highlight python linenos %}
	>>> ringos_membership = Membership.objects.get(group=beatles, person=ringo)
	>>> ringos_membership.date_joined
	datetime.date(1962, 8, 16)
	>>> ringos_membership.invite_reason
	u'Needed a new drumer'
{% endhighlight %}

或者也可以通过Person模型中的 many-to-many 反向关系进行查询

{% highlight python linenos %}
	>>> ringos_membership = ringo.membership_set.get(group=beatles)
	>>> ringos_membership.date_joined
	datetime.date(1962, 8, 16)
	>>> ringos_membership.invite_reason
	u'Needed a new drumer'
{% endhighlight %}

####OneToOne
OneToOneField 可以用来表达继承关系，比如你在数据库中建立了Places的模型，然后又需要建立一个Restaurants模型，那么很为了达到重用的目的，可以让Restaurant继承Places，如下代码所示：

{% highlight python linenos %}
from django.db import models, transaction, IntegrityError

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __unicode__(self):
        return u"%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place, primary_key=True)
    serves_hot_dogs = models.BooleanField()
    serves_pizza = models.BooleanField()

    def __unicode__(self):
        return u"%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%s the waiter at %s" % (self.name, self.restaurant)
{% endhighlight %}

###引用其他App中的Models
{% highlight python linenos %}
from geography.models import ZipCode

class Restaurant(models.Model):
	#...
	zip_code = models.ForeignKey(ZipCode)
{% endhighlight %}

###字段命名限制

Django对字段的命名只有2个限制

- 不能使用python 关键字
- 不能在字段中使用联系2个下划线，因为这个Django的查询语法冲突

以SQL保留字命名字段是允许的，因为Django对所有的SQL查询都会进行转义

###自定义Field类型

自定义Field类型，需要继承models.Model，通过内部类Meta定义表的元数据

{% highlight python linenos %}
class 0x(models.Model):
	horn_length = models.IntegerField()
	
	class Meta:
		ordering = ["horn_length"]
		verbose_name_plural = 'oxen'
{% endhighlight %}

所有“不是一个字段”的信息都可以在Meta中定义，包含了 Ordering， Table name, 单数复数表现形式。Meta的定义是可选的，完整的Meta属性参看[Meta全部属性表](https://docs.djangoproject.com/en/1.5/ref/models/options/)

