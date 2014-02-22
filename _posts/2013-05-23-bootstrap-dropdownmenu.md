---
layout: post
title: "Bootstrap学习笔记7-下拉菜单"
description: "Bootstrap学习笔记7-下拉菜单"
category: Front-End
tags: [css, twitter, bootstrap, components, dropdownmenu]
---

**[Dropdown menus](http://twitter.github.io/bootstrap/components.html)**

CSS部分
=======================

示例
-------------------------

	<div class="dropdown">
		<ul class="dropdown-menu">
		  <li><a tabindex="-1" href="#">Action</a></li>
		  <li><a tabindex="-1" href="#">Another action</a></li>
		  <li><a tabindex="-1" href="#">Something else here</a></li>
		  <li class="divider"></li>
		  <li><a tabindex="-1" href="#">Separated link</a></li>
		</ul>
	</div>

<div class="bs-docs-example" style="height: 150px;">
	<span class="text-left">Example:</span>
	<div class="dropdown">
		<ul class="dropdown-menu" style="display:block">
		  <li><a tabindex="-1" href="#">Action</a></li>
		  <li><a tabindex="-1" href="#">Another action</a></li>
		  <li><a tabindex="-1" href="#">Something else here</a></li>
		  <li class="divider"></li>
		  <li><a tabindex="-1" href="#">Separated link</a></li>
		</ul>
	</div>
</div>

选项
--------------------

-	菜单对齐

 在 `ul.dropdown-menu`中加入`.pull-right`右对齐，左对齐 `.pull-left`

	 <div class="well" style="height:150px">
	 	<span class="text-left">Example</span>
	 	<div class="dropdown">
	 		<ul class="dropdown-menu pull-right" style="block">
	 			<li>
	 				<a href="#" tabindex="-1">Item1</a>
	 				<a href="#" tabindex="-1">Item2</a>
	 				<a href="#" tabindex="-1">Item3</a>
	 				<a href="#" tabindex="-1">Item4</a>
	 			</li>
	 		</ul>
	 	</div>
	 </div>


<div class="well" style="height:150px">
	<div class="container-fluid" style="height:150px">
	<div class="text-left">左对齐</div>
	<div class="dropdown">
		<ul class="dropdown-menu pull-left" style="display:block">
			<li>
				<a href="#" tabindex="-1">Item1</a>
				<a href="#" tabindex="-1">Item2</a>
				<a href="#" tabindex="-1">Item3</a>
				<a href="#" tabindex="-1">Item4</a>
			</li>
		</ul>
	</div>
	<div class="text-right">右对齐</div>
	<div class="dropdown">
		<ul class="dropdown-menu pull-right" style="display:block">
			<li>
				<a href="#" tabindex="-1">Item1</a>
				<a href="#" tabindex="-1">Item2</a>
				<a href="#" tabindex="-1">Item3</a>
				<a href="#" tabindex="-1">Item4</a>
			</li>
		</ul>
	</div>
</div>
</div>

-	禁用菜单项

`<li>`标签中加入css 类`.disabled`

	<div class="well" style="height: 150px;">
		<span class="text-left">Example:</span>
		<div class="dropdown">
			<ul class="dropdown-menu" style="display:block">
			  <li class="disabled"><a tabindex="-1" href="#">Action</a></li>
			  <li><a tabindex="-1" href="#">Another action</a></li>
			  <li><a tabindex="-1" href="#">Something else here</a></li>
			  <li class="divider"></li>
			  <li><a tabindex="-1" href="#">Separated link</a></li>
			</ul>
		</div>
	</div>

<div class="well" style="height: 150px;">
	<span class="text-left">Example:</span>
	<div class="dropdown">
		<ul class="dropdown-menu" style="display:block">
		  <li class="disabled"><a tabindex="-1" href="#">Action</a></li>
		  <li><a tabindex="-1" href="#">Another action</a></li>
		  <li><a tabindex="-1" href="#">Something else here</a></li>
		  <li class="divider"></li>
		  <li><a tabindex="-1" href="#">Separated link</a></li>
		</ul>
	</div>
</div>

-	子菜单

在当前菜单项的任意`<li>`标签上添加`.dropdown-submenu`属性，并增加一级dropdown-menu

	<div class="well text-left" style="height:170px">
		<span class="text-left">Example:</span>
		<div class="dropdown">
			<ul class="dropdown-menu" style="display:block">
				<li><a href="#" tabindex="-1">Item1</a></li>
				<li><a href="#" tabindex="-1">Item2</a></li>
				<li><a href="#" tabindex="-1">Item3</a></li>
				<li class="dropdown-submenu">
					<a href="#" tabindex="-1">子菜单</a>
					<ul class="dropdown-menu" style="display:block">
						<li><a href="#" tabindex="-1">子菜单1</a></li>
						<li><a href="#" tabindex="-1">子菜单2</a></li>
						<li><a href="#" tabindex="-1">子菜单3</a></li>
					</ul>
				</li>
			</ul>
		</div>
	</div>

<div class="well text-left" style="height:170px">
	<span class="text-left">Example:</span>
	<div class="dropdown">
		<ul class="dropdown-menu" style="display:block">
			<li><a href="#" tabindex="-1">Item1</a></li>
			<li><a href="#" tabindex="-1">Item2</a></li>
			<li><a href="#" tabindex="-1">Item3</a></li>
			<li class="dropdown-submenu">
				<a href="#" tabindex="-1">子菜单</a>
				<ul class="dropdown-menu" style="display:block">
					<li><a href="#" tabindex="-1">子菜单1</a></li>
					<li><a href="#" tabindex="-1">子菜单2</a></li>
					<li><a href="#" tabindex="-1">子菜单3</a></li>
				</ul>
			</li>
		</ul>
	</div>
</div>


JavaScript部分
=====================

示例
-------------------

下拉菜单几乎可以加到任何组件当中，包含了`navbar`, `tabs`, `pills`

###在 `navbar` 当中

	<div class="well">
		<div class="navbar">
		  <div class="navbar-inner">
		    <a class="brand" href="#">Title</a>
		    <ul class="nav" style="float:left">
		      <li class="dropdown">
		      	<a href="#" class="dropdown-toggle" data-toggle="dropdown">
		      		Home <b class="caret"></b>
		      	</a>
		      	<ul class="dropdown-menu">
		      		<li><a href="">Item1</a></li>
		      		<li><a href="">Item2</a></li>
		      		<li><a href="">Item3</a></li>
		      	</ul>
		      </li>
		      <li><a href="#">Link</a></li>
		      <li><a href="#">Link</a></li>
		    </ul>
		  </div>
		</div>
	</div>

<div class="well">
	<div class="navbar">
	  <div class="navbar-inner">
	    <a class="brand" href="#">Title</a>
	    <ul class="nav" style="float:left">
	      <li class="dropdown">
	      	<a href="#" class="dropdown-toggle" data-toggle="dropdown">
	      		Home <b class="caret"></b>
	      	</a>
	      	<ul class="dropdown-menu">
	      		<li><a href="">Item1</a></li>
	      		<li><a href="">Item2</a></li>
	      		<li><a href="">Item3</a></li>
	      	</ul>
	      </li>
	      <li><a href="#">Link</a></li>
	      <li><a href="#">Link</a></li>
	    </ul>
	  </div>
	</div>
</div>

如果要载入远程菜单，用`data-target=#`属性代替`href=#`,然后在`href`中填入远程地址

###通过JS调用

	$('.dropdown-toggle').dropdown()



<!-- 放在最后 -->
<script src="http://code.jquery.com/jquery.js"></script>
<!-- 这里和主题相关了。。。没办法 -->
<script src="/assets/themes/twitter/bootstrap/js/bootstrap.min.js"></script>