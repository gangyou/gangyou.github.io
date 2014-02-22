---
layout: post
title: "Ant核心任务"
description: "Ant Core Tasks"
category: Coding
tags: [Java, Ant]
---

Project
---------------

###Attributes

- basedir(all, File, N)
- default(all, String, Y)
- name(all, String, N)

###Content

- 0-n description
- 0-n filelist
- 0-n fileset
- 0-n filterset
- 0-n mapper
- 0-n path
- 0-n property
- 0-n target
- 0-n taskdef

Target
--------------------

###Attribute

- depends(all, String, N)
- description(all, String, N)
- if(all, Strng, N)
- name(all, String, Y)
- unless(all, String, N)

###Content

- DataType

Core Task
=================
***
ant
-------------

###attribute
- antfile(all, String, N)
- dir(all, File, N)
- inheritall(1.4, boolean, N)
- output(all, String, N)
- target(all, String, N)

###Content

- 0-n property


###Example

{% highlight xml %}
	<ant dir="gui" antfile="build.xml" target="clean" />
{% endhighlight %}

antcall
------------

###Attribute

- inheritall(1.4, boolean, N)
- target(all, String, Y)

###Content
- 0-n param

###Example

{% highlight xml %}
	<target name="clean">
		<antcall target="cleandir">
			<param name="dir-to-clean" value="javadocs">
		</antcall>
	</target>

	<target name="cleandir">
		<delete dir="${dir-to-clean}" />
	</target>
{% endhighlight %}

antstructure
-------------------

###Attribute

- output(all, File, Y)

###Content

###Example

{% highlight xml %}
	<target name="createdtd">
		<antstructure output="project.dtd" />
	</target>
{% endhighlight %}
apply
-------------------

###Attribute

- dest(1.3, 1.4, File, *)
- dir(1.3, 1.4, File, N)
- executable(1.3, 1.4, String, Y)
- failonerror(1.3, 1.4, boolean, N)
- newenvironment(1.3, 1.4, boolean, N)
- os(1.3, 1.4, String, N)
- output(1.3, 1.4, File, N)
- outputproperty(1.4, String, N)
- parallel(1.3, 1.4, boolean, N)
- skipemptyfilesets(1.4, boolean, N)
- timeout(1.3, 1.4, int, N)
- type(1.3, 1.4, Enum, N)
- vmlauncher(1.4, boolean, N)

if nest <mapper>, dest is required.

###Content

- 0-n arg
- 0-n env
- 1-n fileset
- 0-1 mapper
- 0-1 srcfile
- 0-1 targetfile

###Example

{% highlight xml %}
	<apply executable="type" vmlauncher="false" os="Windows" 2000="">
		<fileset dir=".">
			<include name="build.xml"></include>
		</fileset>
	</apply>
{% endhighlight %}

available
-------------

###Attribute

- classname(all, String, *)
- classpath(all, Path, N)
- classpathref(all, Reference, N)
- file(all, File, *)
- filepath(1.4, Path, N)
- property(all, String, Y)
- resource(all, String, *)
- type(1.4, String, N)
- value(all, String, N)

classname, file, resource must set one

###Content

- 0-1 classpath
- 0-1 filepath

###Example

{% highlight xml %}
	<available classname="javax.servlet.ServletRequestWrapper" property="Servlet23.present"></available>
{% endhighlight %}

chmod
--------------
Only in Unix

###Attribute

- defaultexcludes(all, boolean, N)
- dir(all, File, *)
- excludes(all, String, N)
- excludesfile(all, File, N)
- file(all, File, *)
- includes(all, String, N)
- includesfile(all, File, N)
- parallel(all, boolean, N)
- perm(all, String, Y)
- type(all, Enum, N)

either dir or file must be setted, or must nest a fileset element.

###Content

- 0-n patternset: exclude, include, patternset, excludesfile, includesfile
- 0-n fileset

###Example

{% highlight xml %}
	<chmod perm="444">
		<fileset dir="${javadocs}">
			<include name="**/*.html"></include>
		</fileset>
	</chmod>
{% endhighlight %}

condition
-----------------------


###Attribute

- property(1.4, String, Y)
- value(1.4, String, N)

###Content

Only on nested condition is allowed.

- not
- and
- or
- available
- uptodate
- os
- equals

###Example

{% highlight xml %}
	<condition property="Environment.configured">
		<and>
			<available classname="javax.servlet.ServletRequestWrapper"></available>
			<available classname="javax.xml.transform.TransformerFactory"></available>
			<or>
				<equals arg1="${java.version}" arg2="1.3.0"></equals>
				<equals arg1="${java.version}" arg2="1.4.0-beta"></equals>
				<equals arg1="${java.version}" arg2="1.4.0"></equals>
			</or>
		</and>
	</condition>
{% endhighlight %}

equals to servlet 2.3 and jaxp1.1 and (java= 1.3.0 or 1.4.0-beta or java=1.4.0))

copy
------------------

###Attribute

- file(all, File, *)
- filtering(all, boolean, N)
- flatten(all, boolean, N)
- includeemptydirs(all, boolean, N)
- overwrite(all, boolean, N)
- preservelastmodified(1.3, 1.4, String, N)
- todir(all, File, *)
- tofile(all, File, *)

要么必须设置file属性，要么至少指定一个嵌套fileset。若设置了file属性，则todir或tofile属性必须设置其一。若使用了嵌套fileset元素，则只允许设置todir。

###Content

- 0-n fileset
- 0-n filterset
- 0-1 mapper

###Example

将所有Java源文件复制到一个新目录，并将所有@VERSION@替换为app.version的值

{% highlight xml %}
	<copy todir="${builddir}/srccopy">
		<fileset dir="${srcdir}">
			<include name="**/*.java"></include>
		</fileset>
		<filterset>
			<filter token="VERSION" value="${app.version}"></filter>
		</filterset>
	</copy>
	{% endhighlight %}


delete
-----------------

###Attribute

- defaultexcludes(all, boolean, N)
- dir(all, File, *)
- excludes(all, String, N)
- excludesfile(all, File, N)
- failonerror(1.4, boolean, N)
- file(all, File, *)
- includeemptydirs(1.3, 1.4, boolean, N)
- includes(all, String, N)
- includesfile(all, File, N)
- quiet(1.3, 1.4, boolean, N)
- verbose(all, boolean, N)

dir或file至少要取其一，或者要有一个嵌套的fileset

###Content

- 0-n patternset
- 0-n fileset

###Example

{% highlight xml %}
	<target name="clean" description="Remove" all="" generated="" code="">
		<delete dir="${builddir}"></delete>
	</target>
{% endhighlight %}

dependset
------------------

###Attribute

###Content

至少需要一个srcfileset 或 srcfilelist, 以及至少一个targetfileset或targetfilelist。如果缺少的文件不重要，则使用fileset,若使用filelist，缺少任何文件都会导致所有目标文件被删除。

- 0-n srcfileset
- 0-n srcfilelist
- 0-n targetfileset
- 0-n targetfilelist

###Example

如果Ant构建文件或任何.java文件比任何.class文件都要新，此例将删除构建目录中所有.class文件

{% highlight xml %}
	<dependset>
		<srcfileset dir="basedir" includes="build.xml" />
		<srcfileset dir="srcdir" includes="**/*.java" />
		<targetfileset dir="builddir" includes="**/*.java" />
	</dependset>
{% endhighlight %}

ear
------------------

###Attribute

- appxml(1.4, File, Y) 部署描述文件
- basedir(1.4, File, N)
- compress(1.4, boolean, N)
- defaultexcludes(1.4, boolean, N)
- earfile(1.4, File, Y)
- encoding(1.4, String, N)
- excludes(1.4, String, N)
- excludesfile(1.4, File, N)
- filesonly(1.4, boolean, N): if true, DO NOT create empty directory
- includes(1.4, String, N)
- includesfile(1.4, file, N)
- manifest(1.4, File, N)
- update(1.4, boolean, N)
- whenempty(1.4, Enum, N): fail, skip, create

###Content

- 0-n patternset
- 0-1 metainf
- 0-n fileset
- 0-n zipfileset

###Example

{% highlight xml %}
	<ear earfile="builddir/myapp.ear" appxml="ear_deploy_descriptor/application.xml" basedir="builddir" includes="*.jar,*.war" />
{% endhighlight %}

{% highlight xml %}
	<ear earfile="builddir/myapp2.ear" appxml="ear_deploy_description/application.xml">
		<fileset dir="builddir" includes="*.jar,*.war" />
	</ear>
{% endhighlight %}

echo
--------------------

###Attribute

- append(all, boolean, N)
- file(all, File, N)
- message(all, String, *)

除非文本作为xml标签的内容包括在内，否则message属性必输

###Content

- 文本内容，如果未指定message属性，则允许文本内容。也允许特性引用。

###Example

	{% highlight xml %}
	<echo message="Building to ${builddir}" />
	<echo>You are using ${java.version} of Java! This message spans two lines.</echo>
	{% endhighlight %}

exec
----------

不能包含filelist

###Attribute

- command(1.1, CommandLine, *):deprecated
- dir(all, File, N)
- executable(all, String, *)
- failonerror(all, boolean, N)
- newenvironment(1.3, 1.4, boolean, N)
- os(all, String, N)
- output(all, File, N)
- outputproperty(1.4, String, N)
- timeout(all, int, N)
- vmlauncher(1.4, boolean, N)

###Content

- 0-n arg
- 0-n env

###Example

	{% highlight xml %}
	<exec executable="dir" dir="builddir" vmlauncher="false" os="Windows 2000">
		<arg line="/b"></arg>
	</exec>
	{% endhighlight %}

fail
-------------

throw a BuildException, and terminate.

###Attribute

- message(all, String, N)

###Content

- text node

###Example

以下例子终止构建时不带任何描述性消息：

	`<fail/>`

这种情况下，Ant显示以下消息，在此104为行号

	BUILD Failed
	C:\XXXXXX\build.xml:104: No message

	{% highlight xml %}
	<fail>Java Version ${java.versions} is not allowed!</fail>

	<fail message="Java Version ${java.version} is not allowed!"></fail>
	{% endhighlight %}

filter

###Attribute

- filtersfile(all, File, *)
- token(all, String, *)
- value(all, String, *)

###Content

None

###Example

<div class="well">
	{% highlight xml %}
	<target name="example-filter">
		<filter token="VERSION" value="1.0"></filter>
		<copy todir="build" filtering="true">
			<fileset dir="src">
				<include name="**/*.java"></include>
			</fileset>
			<filterset begintoken="%" endtoken="!">
				<filter token="COPYRIGHT" value="Copyright (C) 2013 NBCB"></filter>
			</filterset>
		</copy>
	</target>
	{% endhighlight %}
</div>

第一个filter元素负责在复制文件时将@VERSOIN@替换为1.0，为此copy任务的filtering属性必须为true

fixcrlf
----------------------------

清除源文件中的特殊字符，如制表符，回车符，换行符和EOF字符

###Attribute

- cr(all, Enum, N): deprecated in 1.4, values: add, asis, remove
- defaultexcluds(all, boolean, N)
- destdir(all, File, N)
- eof(all, Enum, N): values: add, asis, remove
- eol(1.4, Enum, N): replace of cr attribute, support for Macintosh. values: asis, cr, lf, crlf. lf for Unix, cr for Macintosh, crlf for Windows.
- excludes(all, String, N)
- excludesfile(all, File, N)
- includes(all, String, N)
- includesfile(all, File, N)
- javafiles(1.4, boolean, N)
- srcdir(all, File, Y)
- tab(all, Enum, N) values: add, asis, remove
- tablength(all, int, N)

###Content

- 0-n patternset

###Example

replace tab for 4 spaces.

<div class="well">
	{% highlight xml %}
	<fixcrlf srcdir="srcdir" destdir="builddir" eol="asis" tab="remove" tablength="4" eof="asis" includes="**/*.java" javafiles="true" />
	{% endhighlight %}
</div>

genkey
--------------

###Attribute

- alias(all, String, Y)
- dname(all, String, *)
- keyalg(all, String, N) key algorithm
- keypass(all, String, *)
- keysize(all, String, N)
- keystore(all, String, N)
- sigalg(all, String, N)
- storepass(all, String, Y)
- storetype(all, String, N)
- validity(all, String, N)
- verbose(all, boolean, N)

###Content

- 0-1 dname
	- 0-n param

###Example

<div class="well">
	{% highlight xml %}
	<genkey dname="CN=Eric Burke, OU=Authors, O=NBCB, L=Sebastopol, S=california, C=US" alias="ericb" storepass="aidansdaddy" />

	<genkey alias="ericb" storepass="aidansdaddy">
		<dname>
			<param name="CN" value="Eric Burke">
			<param name="OU" value="Authors">
			<param name="O" value="O'Reilly">
			<param name="L" value="Sebastopol">
			<param name="S" value="California">
			<param name="C" value="US">
		</dname>
	</genkey>
	{% endhighlight %}
</div>

get
-----------------

###Attribute

- dest(all, File, Y)
- ignoreerrors(all, boolean, N)
- src(all, URL, Y)
- usetimestamp(all, boolean, N): only Http
- verbose(all, boolean, N): display a dot in every 100k

###Content

###Example

<div class="well">
	{% highlight xml %}
	<get src="http://www.oreilly.com/" dest="${builddir}/oreilly_home.html"></get>
	{% endhighlight %}
</div>

如果在一个防火墙之后，在运行Ant之前要使用ANT_OPTS指定代理服务器配置

gunzip
-----------------------

展开一个GZip文件（其实就是变成tar)

###Attribute

- dest(all, String, N)
- src(all, String, Y)

###Content

###Example

将manuscript.tar.gz展开为同一目录下的manuscript.tar

<div class="well">
	{% highlight xml %}
	<gunzip src="manuscript.tar.gz"></gunzip>

	<gunzip src="manuscript.tar.gz" dest="build/"></gunzip>
	{% endhighlight %}
</div>

gizp
------------------

tar to tar.gz

###Attribute

- src(all, File, Y)
- zipfile(all, File, Y)

###Content

###Example

<div class="well">
	{% highlight xml %}
	<gzip src="manuscript.tar" dest="manuscrip.tar.gz" />
	{% endhighlight %}
</div>

jar
-----------------

###Attribute

- basedir(all, File, N)
- compress(all, boolean, N)
- defaultexcludes(all, boolean, N)
- encoding(1.4, String, N)
- excludes(all, String, N)
- excludesfile(all, File, N)
- filesonly(1.4, boolean, N)
- includes(all, String, N)
- includesfile(all, File, N)
- jarfile(all, File, Y)
- manifest(all, File, N)
- update(1.4, boolean, N
- whenempty(all, Enum, N) values: fail, skip, create(default)

###Content

- 0-n attribute(name, value)
- 0-n patternset
- 0-n fileset
- 0-1 metainf
- 0-n section>attribute
- 0-n zipfileset

###Example

<div class="well">
	{% highlight xml %}
	<jar jarfile="sample.jar" basedir="build" includes="**/*.class" />

	<jar jarfile="build/sample.jar">
		<fileset dir="build" includes="**/*.class"></fileset>
	</jar>

	<jar jarfile="build/sample.jar" basedir="src" includes="**/*.class">
		<manifest>
			<attribute name="Version" value="3.2"></attribute>
			<attribute name="Release-Date" value="20 Mar 2002"></attribute>
			<section name="drinks">
				<attribute name="favoriteSoda" value="Coca Cola"></attribute>
				<attribute name="favoriteBeer" value="Amber Bock"></attribute>
			</section>
			<section name="snacks">
				<attribute name="cookie" value="chocklateChip"></attribute>
				<attribute name="iceCream" value="mooseTracks"></attribute>
			</section>
		</manifest>
	</jar>
	{% endhighlight %}
</div>

java
---------------

if call System.exit() must set fork=true, otherwise Ant will terminate.

###Attributes

- args(all, String, N), deprecated in 1.2, replace with nested <arg>
- classname(all, String, *)
- classpath(all, Path, N)
- classpathref(all, Reference, N)
- dir(all, File, N)
- failonerror(all, boolean, N)
- fork(all, boolean, N)
- jar(1.4, File, *), fork must be true
- jvm(all, String, N)
- jvmargs(all, String, N), deprecated in Ant 1.2, replace with nested <jvmarg>
- maxmemory(all, String, N), only affected in fork=true
- output(1.3, 1.4, File, N)

one of classname or jar must be set

###Content

- 0-n arg/jvmarg
- 0-n sysproperty
- 0-1 classpath

###Example

<div class="well">
	{% highlight xml %}
	<java classname="com.nbcb.antbook.JavaTest">
		<sysproperty key="oreilly.home" value="${builddir}"></sysproperty>
		<arg value="Eric"></arg>
		<arg line="-verbose -debug"></arg>
		<arg path="/home;/index.html"></arg>
		<classpath>
			<pathelement path="${builddir}"></pathelement>
		</classpath>
	</java>
	{% endhighlight %}
</div>

it equals to: `java -Doreilly.home=build Eric -verbos -debug C:\home;C:\index.html`

{% highlight xml %}
	<!-- this is defined at the "target level", parallel to <target> s  -->
	<path id="thirdparty.class.path">
		<pathelement path="lib/crimson.jar"></pathelement>
		<pathelement path="lib/jaxp.jar"></pathelement>
		<pathelement path="lib/xalan.jar"></pathelement>
	</path>

	<target name="rundemo">
		<java classname="com.oreilly.antbook.JavaTest">
			<classpath refid="thirdparty.class.path"></classpath>
		</java>
	</target>
{% endhighlight %}

javac
-------------
***

###Attribute

- bootclassapth(all, Path, N)
- bootclasspathref(all, Reference, N)
- classpath(all, Path, N)
- classpathref(all, Reference, N)
- debug(all, boolean, N)
- defaultexcludes(all, boolean, N)
- depend(all, boolean, N)
- deprecation(all, boolean, N)
- destdir(all, File, N)
- encoding(all, String, N)
- excludes(all, String, N)
- excludesfile(all, String, N)
- extdirs(all, Path, N)
- failonerror(1.3, 1.4, boolean, N)
- fork(1.4, boolean, N)
- includeantruntime(1.3, 1.4, boolean, N)
- includejavaruntime(1.3, 1.4, boolean, N)
- includes(all, String, N)
- includesfile(all, File, N)
- memoryinitialsize(1.4, String, N) when fork=true
- memorymaximumsize(1.4, String, N) when fork=true
- nowarn(1.4, boolean, N)
- optimize(all, boolean, N)
- source(1.4.1, String, N)
- srcdir(all, Path, *)
- target(all, String, N)
- verbose(all, boolean, N)

###Content

- 0-n patternset
- 0-n path: bootclasspath, classpath, extdirs, src

###Example

compile the java source file in package com.oreilly.antbook and its sub packages.

{% highlight xml %}
	<javac srcdir="${srcdir}" destdir="${builddir}" includes="com/oreilly/antbook/**" />
{% endhighlight %}

javadoc
-----------
***

###Attribute

- access(1.4, Enum, N) values: public, protected, package, private
- additionalparam(all, String, N)
- author(all, boolean, N)
- bootclasspath(all, Path, N)
- bootclasspathref(all, Reference, N)
- bottom(all, String, N)
- charset(all, String, N)
- classpath(all, Path, N)
- classpathref(all, Reference, N)
- defaultexcludes(1.4, boolean, N)
- destdir(all, File, *)
- docencoding(all, String, N)
- doclet(all, String, N)
- docletpath(all, Path, N)
- docletpathref(all, Reference, N)
- doctitle(all, String, N)
- encoding(all, String, N)
- excludepackagenames(1.4, String, N), comma splitted packages to be exclude
- extdirs(all, String, N)
- failonerror(all, boolean, N)
- footer(all, String, N)
- group(all, String, N)
- header(all, String, N)
- helpfile(all, File, N)
- link(all, String, N)
- lineoffline(all, String, N)
- locale(all, String, N)
- maxmemory(all, String, N)
- nodeprecated(all, boolean, N)
- nodeprecatedlist(all, boolean, N)
- nohelp(all, boolean, N)
- noindex(all, boolean, N)
- nonavbar(all, boolean, N)
- notree(all, boolean, N)
- old(all, boolean, N)
- overview(all, File, N)
- package(all, boolean, N)
- packagelist(all, String, N)
- packagenames(all, String, *)
- private(all, boolean, N)
- protected(all, boolean, N)
- public(all, boolean, N)
- serialwarn(all, boolean, N)
- sourcefiles(all, String, *)
- sourcepath(all, Path, *)
- sourcepathref(all, Reference, *)
- splitindex(all, boolean, N)
- stylesheetfile(all, File, N)
- use(all, boolean, N)
- useexternalfile(1.4, boolean, N)
- verbose(all, boolean, N)
- version(all, boolean, N)
- windowtitle(all, String, N)

###Example

{% highlight xml %}
	<javadoc excludepackagenames="com.oreilly.test.*" destdir="docs" windowtitle="My Documentation">
		<package name="com.oreilly.antbook"></package>
		<package name="com.oreilly.util.*"></package>
		<sourcepath location="${srcdir}"></sourcepath>
		<classpath location="${builddir}"></classpath>
		<bottom>
			<![CDATA[<em>Copyright (C) 2001, O'Reilly</em><br>All Rights Reserved]]>
		</bottom>
	</javadoc>
{% endhighlight %}

mail
-----------
***

###Attribute

- files(all, String, *)
- from(all, String, Y)
- mailhost(all, String, N)
- message(all, String, *)
- subject(all, String, N)
- tolist(all, String, Y)

###Content

None

###Example

{% highlight xml %}
	<property name="my.mailhost" value="mail.oreilly.com"></property>
	<mail from="ant@foobar.com" tolist="developers@foobar.com" subject="Build Results" mailhost="${my.mailhost}" files="buildlog.txt"></mail>
{% endhighlight %}

mkdir
----------------
***

###Attribute

- dir(all, File, Y)

###Content

None

###Example

{% highlight xml %}
	<target name="prepare">
		<mkdir dir="${builddir}"></mkdir>
		<mkdir dir="${deploydir}/docs"></mkdir>
	</target>
	<target name="compile" depends="prepare"></target>
{% endhighlight %}

move
--------------
***

###Attribute

- file(all, File, *)
- filtering(all, boolean, N)
- flatten(all, boolean, N)
- includeemptydirs(all, boolean, N)
- overwrite(all, boolean, N)
- todir(all, File, *)
- tofile(all, File, *)

###Content

- 0-n fileset
- 0-n filterset
- 0-1 mapper


###Example

{% highlight xml %}
	<move todir="builddir/foo">
		<fileset dir="builddir">
			<include name="**/*.class"></include>
		</fileset>
	</move>
{% endhighlight %}

parallel
-------------
***

###Attribute

None

###Content

every tasks, include parallel task

###Example

{% highlight xml %}
	<parallel>
		<sequential>
			<!-- copy some critical files first -->
			<copy></copy>
			<!-- run a code generator -->
			<java></java>
			<!-- now compile the client code -->
			<javac srcdir="client_srcdir" destdir="client_builddir" includes="com/oreilly/client/**"></javac>
		</sequential>

		<!-- compile the server code in parallel with everything contained in the <sequential> task -->
		<javac srcdir="server_srcdir" destdir="server_builddir" includes="com/acme/server/**"></javac>
	</parallel>
{% endhighlight %}

path
---------------
***

apply a diff

###Attribute

- backups(all, boolean, N)
- ignorewhitespace(all, boolean, N)
- originalfile(all, File, N)
- patchfile(all, File, Y)
- quiet(all, boolean, N)
- reverse(all, boolean, N)
- strip(all, int, N)

###Content

None

###Example

{% highlight xml %}
	<patch patchfile="foo.patch" />
{% endhighlight %}

pathconvert
---------------
***

将Ant路径或fileset转换为平台专有的路径，并将结果保存在一个特性中。

###Attribute

- dirsep(1.4, String, *) directory seperator, default to File.seperator
- pathsep(1.4, String, *) path seperator, default to File.pathSeperator
- property(1.4, String, Y)
- refid(1.4, Reference, *)
- targetos(1.4, String, *)

###Content

- 0-n map
- 0-1 path

###Example

{% highlight xml %}
	<fileset id="sources1" dir="src" includes="**/*.java" excludes="**/test/**/*.java" />
	<pathconvert targetos="unix" property="p1" />
{% endhighlight %}

p1 = /home/eric/src/com/oreilly/Book.java:/home/eric/src/com/oreilly/Chapter.java

property
---------------
***

###Attribute

- classpath(1.3, 1.4, Path, N)
- classpathref(1.3, 1.4, Reference, N)
- enviroment(1.3, 1.4, String, *)
- file(all, File, *)
- location(all, File, *)
- name(all, String, N)
- refid(all, Reference, *)
- resource(all, String, *)
- value(all, String, *)

若指定name, 则value, location或refid三者必选其一。否则，在resource, file或environment中必取其一。

###Content

- 0-1 classpath, replace of attribute "classpath"

###Example

{% highlight xml %}
	<property name="builddir" value="build"></property>
	<property name="srcdir" value="src"></property>
	<property resource="com/oreilly/antbook/test.properties">
		<classpath>
			<pathelement path="${srcdir}" />
		</classpath>
	</property>
	<!-- display the property values... -->
	<echo message="book.title = ${book.title}" />
	<echo message="book.author = ${book.author}" />
	
	<property environment="env"></property>
	<property name="tomcat.home" value="${env.TOMCAT_HOME}"></property>
{% endhighlight %}

record
--------------
***

为创建过程创建一个监听者，将输出记录到一个文件中。对于同一个文件可以存在多个记录器(recorder)

###Attribute

- action(1.4, Enum, N)
- append(1.4, boolean, N)
- loglevel(1.4, Enum, N)
- name(1.4, String, Y)

###Content

None

###Example

{% highlight xml %}
	<record name="javac.log" loglevel="debug" action="start" append="false" />
	<javac srcdir="srcdir" destdir="builddir" includes="com/oreilly/antbook/**" />
	<record name="javac.log" action="stop" />
{% endhighlight %}

replace
---------------
***

###Attribute

- defaultexcludes(all, boolean, N)
- dir(all, File, *)
- excludes(all, String, N)
- excludesfile(all, File, N)
- file(all, File, *)
- includes(all, String, N)
- includesfile(all, File, N)
- propertyfile(1.3, 1.4, File, *)
- summary(1.4, boolean, N)
- token(all, String, *)
- value(all, String, N)

在file或dir中必取其一。如果使用了一个嵌套replacetoken元素，则需要token属性。如果指定了一个嵌套replacefilter元素的property属性，则propertyfile属性是必须的。

###Content

- 0-n patternset
- 0-n replacefilter
	- token(1.3, 1.4, String, Y)
	- value(1.3, 1.4, String, *)
	- property(1.3, 1.4, String, *)
- 0-1 replacetoken replacevalue

###Example

{% highlight xml %}
	<replace file="${builddir}/replaceSample.txt" token="@builddate@" value="DSTAMP" />

	<replace file="builddir/replaceSample.txt">
		<replacetoken>
			<![CDATA[Token line 1
			Token line 2]]>
		</replacetoken>
		<replacevalue>
			<![CDATA[Line 1
			Line 2]]>
		</replacevalue>
	</replace>

	<replace dir="srcdir" includes="**/*.java" propertyfile="tokens.properties">
		<replacefilter token="@vendor@" property="vendor.name" />
		<replacefilter token="@version@" property="version.name"></replacefilter>
	</replace>
{% endhighlight %}

rmic
--------------
***

Generate Java RMI stub and skeleton

###Attribute

- base(all, File, Y)
- classname(all, String, N)
- classpath(all, Path, N)
- classpathref(all, Referece, N)
- debug(1.3, 1.4, boolean, N)
- defaultexcludes(all, boolean, N)
- excludes(all, String, N)
- excludesfile(all, File, N)
- extdirs(1.4, Path, N)
- filtering(all, boolean, N)
- idl(1.3, 1.4, boolean, N)
- idlopts(1.3, 1.4, String, N)
- iiop(1.3, 1.4, boolean, N)
- iiopopts(1.3, 1.4, String, N)
- includeantruntiem(1.4, boolean, N)
- includejavaruntime(1.4, boolean, N)
- includes(all, String, N)
- includesfile(all, File, N)
- sourcebase(all, File, N)
- stubversion(all, String, N)
- verify(all, boolean, N)

###Content
- 0-n patternset
- 0-1 classpath
- 0-n extdirs

###Example

{% highlight xml %}
	<rmic base="builddir" includes="com/oreilly/remote/*.class" />
{% endhighlight %}

sequential
-------------
***

###Attribute

None

###Content

###Example

signjar
----------------
***

###Attribute

- alias(all, String, Y)
- internalsf(all, boolean, N)
- jar(all, String, Y)
- keypass(all, String, *)
- keystore(all, String, N)
- sectionsonly(all, boolean, N)
- sigfile(all, String, N)
- signedjar(all, String, N)
- verbose(all, boolean, N)

###Content

- 0-n fileset

###Example

{% highlight xml %}
	<signjar jar="${builddir}/server.jar" alias="oreilly" stroepass="${password}" />
{% endhighlight %}

sleep
------------
***

###Attribute

- failonerror(1.4, boolean, N)
- hours(1.4, int, N)
- milliseconds(1.4, int, N)
- minutes(1.4, int, N)
- seconds(1.4, int, N)

###Content

None

###Example

{% highlight xml %}
	<!-- start a web server, then wait a few seconds for it to initialize -->
	<sleep seconds="10" />
	<!-- now start the client unit tests -->
{% endhighlight %}

sql
---------
***

###Attribute

- autocommit(all, boolean, N)
- classpath(all, Path, N)
- classpathref(all, Reference, N)
- delimiter(1.4, String, N)
- delimitertype(1.4, Enum, N)
- driver(all, String, Y)
- onerror(all, Enum, N) values: continue, abort, stop
- output(all, File, N)
- password(all, String, Y)
- print(all, boolean, N): if true, print all the result set.
- rdbms(all, String, N), the return value of DatabaseMetaData.getDatabaseProductName()
- showheaders(all, boolean, N): if true, print title
- src(all, File, *),
- url(all, String, Y)
- userid(all, String, Y)
- version(all, String, N)

###Content

- text content
- 0-1 classpath
- 0-n fileset
- 0-n transaction
	src(all, String, *)

如果SQL语句作为文本嵌套在<transaction>元素中，那么src属性可以被忽略

###Example

{% highlight xml %}
	<sql driver="${db.driver}" url="${db.url}" userid="${db.userid}" password="${db.password}" src="report.sql" />

	<sql driver="${db.driver}" url="${db.url}" userid="${db.userid}" password="${db.password}">
	SELECT *
	FROM ReportTbl;
	SELECT ... ;
	</sql>
{% endhighlight %}	

tar
------------
***

###Attribute

- basedir(all, File, N)
- defaultexcludes(all, boolean, N)
- excludes(all, String, N)
- excludesfile(all, File, N)
- includes(all, String, N)
- includesfile(all, File, N)
- longfile(1.3, 1.4, String, N) values: truncate, fail, warn(default), omit, gnu
- tarfile(all, File, Y)

###Content

- 0-n patternset
- 0-n tarfileset
	mode(1.3, 1.4, String, N) 用以指定用户/组和其他模式
	username(1.3, 1.4, String, N) tar项的用户名
	group(1.3, 1.4, String, N) tar项的组名

###Example

{% highlight xml %}
	<tar tarfile="dist/classes.tar" basedir="builddir" include="**/*.class" />
{% endhighlight %}

taskdef
--------------------
***

定义未在ant.jar的default.properties文件中定义的任务

###Attribute

- classname(all, String, *)
- classpath(all, Path, N)
- file(1.4, File, N) taskname=full.package.name.TaskClass
- name(all, String, *)
- resource(1.4, String, N)

###Content

- 0-1 classpath

###Example

{% highlight xml %}
	<taskdef name="mycodegen" classname="com.foobar.tasks.MyCodeGen" />
{% endhighlight %}

touch
------------
***

update the timestamp of one file or files

###Attribute
- datetime(all, String, N) MM/DD/YYYY HH:MM AM or PM. default to current time
- file(all, File, *)
- millis(all, long, N)

###Content

- 0-n fileset

###Example


{% highlight xml %}
	<touch file="build.xml" />

	<touch datetime="06/25/1999 6:15 AM">
		<fileset dir="builddir" />
	</touch>
{% endhighlight %}

tstamp
-------------
***

tstamp format:

*DSTAMP*
format: yyyyMMdd
exmaple: 20010916

*TSTAMP*
format: HHmm
example: 1923

*TODAY*
format: MMMM d yyyy
example: September 16 2001

###Content

- 0-n format
	- property(1.3, 1.4, String, Y) 符合java SimpleDateFormat格式的字符串
	- pattern(1.3, 1.4, String, Y)
	- offset(1.3, 1.4, int, N)
	- unit(1.3, 1.4, String, N), values: millisecond, second, minute, hour, day, week, month, year
	- locale(1.4, String, N)

###Example

now, one hour before now, one minute after now

{% highlight xml %}
	<tstamp>
		<format property="now" pattern="yyyyMMdd HH:mm:ss"></format>
	</tstamp>
	<echo>now = ${now}</echo>
{% endhighlight %}

typedef
-----------------
***

###Attribute

- name(1.4, String, *)
	
要增加的DataType名字

- classname(1.4, String, *)

实现DataType的Java类

- file(1.4, File, N)
	
包含DataType定义的特性文件。每行的格式如下：name=classname

- resource(1.4, String, N)

特性文件的Java资源名。使用一个ClassLoader来加载特性文件

- classpath(1.4, Path, N)

除非指定了file或resource属性，否则name和classname熟悉是必须的。

###Content

- 0-1 classpath

###Example

Java Source:
{% highlight java %}
	package taskdef;

	import org.apache.tools.ant.BuildException;
	import org.apache.tools.ant.Task;

	public class MyTask extends Task{
		private String msg;

		public void execute() throws BuildException{
			System.out.println(msg);
		}

		public void setMessage(String msg){
			this.msg = msg;
		}
	}
{% endhighlight %}

tasks.properties:
{% highlight xml %}
mytask=taskdef.MyTask
{% endhighlight%}

build.xml:
{% highlight xml %}
	<taskdef file="tasks.properties" classpath="./build" />

	<target name="example-taskdef">
		<mytask message="Hello World! My Task works!" />
	</target>
{% endhighlight %}

unjar, unwar, unzip
------------------
org.apache.tools.ant.taskdefs.Expand
***

###Attribute

- dest(all, File, Y)
- src(all, File, Y)
- overwrite(1.4, boolean, N)

###Content

None

###Example

{% highlight xml %}
	<unzip src="dist.jar" dest="${builddir}"></unzip>
{% endhighlight %}

see -unzip-

untar
-----------
***

unpack a tar

###Attribute

- dest(all, File, Y)
- overwrite(1.4, boolean, N)
- src(all, File, Y)

###Content

None

###Example

{% highlight xml %}
	<untar src="foo.bar" dest="${builddir}" />
{% endhighlight %}

uptodate
----------------
***

###Attribute

- property(all, String, Y)
- targetfile(all, File, *)
- value(1.4, String, N)

除非指定了一个嵌套<mapper>，否则targetfile属性就是必要的

###Content

- 0-n srcfiles

每个元素均为一个fileset，它定义了要比较的一组源文件

- 0-1 mapper

定义源文件如何与目标文件相关。如果未指定，此任务使用一个合并mapper,其to属性设置为uptodate任务的targetfile属性的值


###Example

如果classes.jar比.class文件新，设置属性

{% highlight xml %}
	<uptodate property="jar_ok" targetfile="${builddir}/classes.jar">
		<srcfiles dir="${builddir}" includes="**/*.class"></srcfiles>
	</uptodate>
{% endhighlight %}

如果.java比.template文件新，则设置属性

{% highlight xml %}
	<uptodate property="codegen_uptodate">
		<srcfiles dir="src" include="**/*.template"></srcfiles>
		<mapper type="glob" from="*.template" to="*.java"></mapper>
	</uptodate>
{% endhighlight %}

war
--------------
***

###Attribute

- basedir(all, File, N)
- compress(all, boolean, N)
- defaultexcludes(all, boolean, N)
- encoding(1.4, String, N)
- excludes(all, String, N)
- excludesfile(all, File, N)
- filesonly(1.4, boolean, N)
- includes(all, String, N)
- includesfile(all, File, N)
- manifest(all, File, N)
- update(1.4, boolean, N)
- warfile(all, File, Y)
- webxml(all, File, Y)
- whenempty(all, Enum, N) values: create, fail, skip

###Content

- 0-n patternset
- 0-n classes
- 0-n fileset
- 0-n lib
- 0-n metainf
- 0-n webinf
- 0-n zipfileset

###Example

{% highlight xml %}
	<war warfile="${builddir}/ecom.war" webxml="src/metadata/web.xml">
		<fileset dir="src/docroot"></fileset>
		<classes dir="${builddir}" includes="**/*.class"></classes>
		<lib dir="${builddir}" include="*.jar"></lib>
	</war>
{% endhighlight %}

zip
----------------
***

###Attribute

- basedir(all, File, N)
- compress(all, boolean, N)
- defaultexcludes(all, boolean, N)
- encoding(1.4, String, N)
- excludes(all, String, N)
- excludesfile(all, File, N)
- filesonly(1.4, boolean, N)
- includes(all, String, N)
- includesfile(all, File, N)
- update(1.4, boolean, N)
- whenempty(all, Enum, N) values: create, fail, skip
- zipfile(all, File, Y)

###Content

- 0-n patternset
- 0-n fileset
- 0-n zipfileset

每个元素均为一个zipfileset,这是fileset的扩展，zipfileset对fileset增加了以下属性：
	- fullpath(String, N)

只能对一个文件设置。当一个文件增加到压缩文件时，指定其完全路径名。

	- prefix(String, N)
	
如果指定，以此路径为前缀的所有文件均放置于压缩文件中。

	- src(File, *)

制定一个现有的zip， 可以抽取出其内容，再插入到新的ZIP文件中。

dir或src必选其一，且只能选其一。
