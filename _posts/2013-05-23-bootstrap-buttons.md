---
layout: post
title: Bootstrap学习笔记5-按钮
description: Bootstrap学习笔记5-按钮
category: Front-End
tags: [css, twitter, bootstrap, buttons]
---

CSS部分
========================

默认样式
------------------------

只要将`.btn`放在任意元素上，都可以成为一个按钮。应用在`<a>`和`<button>`标签上，可以获得最理想的效果。其他常用样式如下：

-	Default `<button class="btn">Default</button>` <button class="btn">Default</button>
-	Primary `<button class="btn btn-primary">Primary</button>` <button class="btn btn-primary">Primary</button>
-	Info `<button class="btn btn-info">Info</button>` <button class="btn btn-info">Info</button>
-	Success `<button class="btn btn-success">Success</button>` <button class="btn btn-success">Success</button>
-	Warning `<button class="btn btn-warning">Warning</button>` <button class="btn btn-warning">Warning</button>
-	Danger `<button class="btn btn-danger">Danger</button>` <button class="btn btn-danger">Danger</button>
-	Inverse `<button class="btn btn-inverse">Inverse</button>` <button class="btn btn-inverse">Inverse</button>
-	link `<button class="btn btn-link">Link</button>` <button class="btn btn-link">Link</button>

控制大小
------------------

可以在`<button>`标签上通过添加`.btn-large, .btn, .btn-small, .btn-mini, .btn-block`控制按钮的大小，具体效果如下：

-	Large Button `.btn-large`

`<button class="btn btn-large btn-primary" type="button">Large button</button>` <button class="btn btn-large btn-primary" type="button">Large button</button>

-	Default Button `.btn`

`<button class="btn btn-primary" type="button">Default button</button>` <button class="btn btn-primary" type="button">Default button</button>

-	Small Button `.btn-small`

`<button class="btn btn-small btn-primary" type="button">Small button</button>` <button class="btn btn-small btn-primary" type="button">Small button</button>

-	Mini Button `.btn-mini`

`<button class="btn btn-mini btn-primary" type="button">Mini button</button>` <button class="btn btn-mini btn-primary" type="button">Mini button</button>

-	Block level Button `.btn-block`

{% highlight html%}
<button type="button" class="btn btn-large btn-block btn-primary">Block level button</button>
<button type="button" class="btn btn-large btn-block">Block level button</button>
{% endhighlight %}

<div class="bs-docs-example">
	<button type="button" class="btn btn-large btn-block btn-primary">Block level button</button>
	  <button type="button" class="btn btn-large btn-block">Block level button</button>
</div>

不可用状态
----------------------

BS通过把背景透明度提高50%，表现按钮的不可用状态。

###&lt;a&gt;按钮

把`.disabled`样式应用到`a.btn`

	<a href="#" class="btn btn-large btn-primary disabled">Primary link</a>
	<a href="#" class="btn btn-large disabled">Link</a>

<div class="bs-docs-example">
	<a href="#" class="btn btn-large btn-primary disabled">Primary link</a>
	<a href="#" class="btn btn-large disabled">Link</a>
</div>

###&lt;button&gt;按钮

在`<button>`标签中加入`disabled`属性

	<button type="button" class="btn btn-large btn-primary disabled" disabled="disabled">Primary button</button>
	<button type="button" class="btn btn-large" disabled>Button</button>

<div class="bs-docs-example">
	<button type="button" class="btn btn-large btn-primary disabled" disabled="disabled">Primary button</button>
	<button type="button" class="btn btn-large" disabled>Button</button>
</div>

###一个样式,多种标签

可以将`.btn`样式,应用到`a, button, input`标签,如下:

	<a class="btn" href="">Link</a>
	<button class="btn" type="submit">Button</button>
	<input class="btn" type="button" value="Input">
	<input class="btn" type="submit" value="Submit">

<div class="bs-docs-example">
	<a class="btn" href="">Link</a>
	<button class="btn" type="submit">Button</button>
	<input class="btn" type="button" value="Input">
	<input class="btn" type="submit" value="Submit">
</div>

按钮组
---------------------

###单组按钮

将一组`.btn`的`<button>`标签包裹在`.btn-group`中

	<div class="btn-group">
	  <button class="btn">Left</button>
	  <button class="btn">Middle</button>
	  <button class="btn">Right</button>
	</div>

<div class="bs-docs-example">
	<div class="btn-group">
	  <button class="btn">Left</button>
	  <button class="btn">Middle</button>
	  <button class="btn">Right</button>
	</div>
</div>

###多组按钮

将一组`div.btn-group`包裹在`div.btn-toolbar`中

	<div class="btn-toolbar">
		<div class="btn-group">
			<button class="btn">1</button>
			<button class="btn">2</button>
			<button class="btn">3</button>
			<button class="btn">4</button>
		</div>
		<div class="btn-group">
			<button class="btn">1</button>
			<button class="btn">2</button>
			<button class="btn">3</button>
		</div>
		<div class="btn-group">
			<button class="btn">1</button>
		</div>
	</div>

<div class="bs-docs-example">
	<div class="btn-toolbar">
		<div class="btn-group">
			<button class="btn">1</button>
			<button class="btn">2</button>
			<button class="btn">3</button>
			<button class="btn">4</button>
		</div>
		<div class="btn-group">
			<button class="btn">1</button>
			<button class="btn">2</button>
			<button class="btn">3</button>
		</div>
		<div class="btn-group">
			<button class="btn">1</button>
		</div>
	</div>
</div>

###垂直方向按钮组

在`div.btn-group`上添加`.btn-group-vertical`

	<div class="btn-group btn-group-vertical">
		<i class="icon-align-left"></i>
		<i class="icon-align-center"></i>
		<i class="icon-align-right"></i>
		<i class="icon-align-jutify"></i>
	</div>

<div class="bs-docs-example">
	<div class="btn-group btn-group-vertical">
		<button class="btn"><i class="icon-align-left"></i></button>
		<button class="btn"><i class="icon-align-center"></i></button>
		<button class="btn"><i class="icon-align-right"></i></button>
		<button class="btn"><i class="icon-align-justify"></i></button>
	</div>
</div>

###复选框和单选按钮

BS可以把成组的复选框和单选按钮渲染成一组按钮,具体请参看JS部分
