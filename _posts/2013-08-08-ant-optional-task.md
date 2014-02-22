---
layout: post
title: "Ant 可选任务"
description: ""
category: Coding
tags: [Java, Ant]
---

ftp
--------------
***

netcomponents.jar

###Attribute

- action(all, String, N)
	
	values: send(default), put, recv, get, del, delete, list, mkdir 

- binary(all, boolean, N)
- depends(all, boolean, N) false
- ignorenoncriticalerrors(1.4, boolean, N) false
- listing(all, File, *)
- newer(all, boolean, N) alias to `depends`
- passive(1.3, 1.4, boolean, N)
- password(all, String, Y)
- port(all, int, N)
- remotedir(all, String, N)
- separator(all, String, N) `/` default
- server(all, String, Y)
- skipfailedtransfers(1.4, boolean, N) `false`
- userid(all, String, Y)
- verbose(all, boolean, N) `false`

当`action="list"`时， listing属性是必要的

###Content

- 0-n filesest

junit
-------------
***

org.apache.tools.ant.taskdefs.optional.junit.JUnitTask
JUnit 3.0 or above

###Attribute

- dir(all, File, N): directory of jvm, only affected in fork=true
- errorproperty(1.4, String, N)
- failureproptery(1.4, String, N)
- fork(all, boolean, N)
- haltonerror(all, boolean, N)
- haltonfailure(all, boolean, N)
- jvm(all, String, N)
- maxmemory(all, String, N)
- printsummary(all, Enum, N)
- timeout(all, int, N) only `fork=true`

###Content

- 0-n batchtest
- 0-1 classpath
- 0-n formatter
- 0-n jvmarg
- 0-n sysproperty
- 0-n test

junitreport
--------------
***

org.apache.tools.ant.taskdefs.optionnal.junit.XMLResultAggregator

Xalan XSLT Processor required

###Attribute

- todir(1.3, 1.4, File, N)
- tofile(1.3,1.4, String, N)

###Content

- 0-n fileset: xml reports need to be merged.
- 0-n report

mimemail
----------------------
***

*deprecated, Use mail instead.*
org.apache.tools.ant.taskdefs.optional.net.MimeMail
send emails with attachments. JavaMail API and JavaBeans Activation Framework are required.

###Attribute

- bcclist(1.4, String, *)
- cclist(1.4, String, *)
- failonerror(1.4, boolean, N)
- from(1.4, String, Y)
- mailhost(1.4, String, N) default `localhost`
- message(1.4, String, *)
- messagefile(1.4, File, *)
- messagemimetype(1.4, String, N)
- subject(1.4, String, N)
- tolist(1.4, String, *)

native2ascii
---------------
***

###Attribute

- defaultexcludes(all, boolean, N)
- dest(all, File, Y)
- encoding(all, String, N)
- excludes(all, String, N)
- excludesfile(all, File, N)
- ext(all, String, N)
- includes(all, String, N)
- includesfile(all, File, N)
- reverse(all, boolean, N)
- src(all, File, N)

###Content

- 0-n patternset
- 0-1 mapper

propertyfile
----------------
***

###Attribute

- comment(1.3, 1.4, String, N)
- file(1.3, 1.4, File, Y)

###Content

- 0-n entry
	- key(String, Y)
	- value(String, *)

	Value to set(=), to add(+) or subtract(-)

	- default

	initial value to set for a property if it is not already defined in the property file. For type date, and aditional keywords is allowed: "now"

	- type

	Regard the value as : int, date or string(default)

	- operation

	One of the following operations:
	for all datatypes:

		- del: deletes an entry
		- +: adds a value to the existing value
		- =: sets a value instead of the existing value(default)

	for date and int only:

		- \-: subtracts a value from the existing value

	- pattern
	- unit

	The unit of the value to be applied to date +/- operation. Valid values are:
		- millisecond
		- second
		- minute
		- hour
		- day(default)
		- week
		- month
		- year

telnet
-----------------
***

###Attribute

- initialcr(1.3, 1.4, boolean, N)
- passowrd(1.3, 1.4, String, N)
- port(1.3, 1.4, int, N)
- server(1.3, 1.4, String, Y)
- timeout(1.3, 1.4, int, N)
- userid(1.3, 1.4, String, N)

###Content

- 0-n read
- 0-n write

xmlvalidate
----------------
***

org.apache.tools.ant.taskdefs.optional.XMLValidateTask
使用SAX解析程序，验证XML文档为良构的

###Attribute

- classname(1.4, String, N)
- classpath(1.4, Path, N)
- classpathref(1.4, Reference, N)
- failonerror(1.4, boolean, N)
- file(1.4, File, N)
- lenient(1.4, boolean, N)
- warn(1.4, boolean, N)

###Content

- 0-1 classpath
- 0-n fileset
