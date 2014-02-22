---
layout: page
title: Bootstrap学习笔记1-排版
description: Bootstrap学习笔记1-排版
catrgory: Front-End
tags: [css, twitter, bootstrap, typography]
---

排版
====================
	
标题Headings
---------------
h1-h6

正文Body Copy
---------------------

-	默认 `font-size`: 14px
-	默认 `body line-height`: 20px
-	`<p>` margin-bottom 为 line-height一半
-	p.lead让一段文字突出

着重Emphasis
---------------------

-	inline的不强调用`<small>`标签
-	加粗使用`<strong>`
-	斜体用`<em>`

note: <b> highlight words <i> for voice, technical terms

对齐Classes Alignment classes
-------------------------

-	.text-left for left aligned
-	.text-center for center aligned
-	.text-right for right aligned

着重Classes Emphasis classes
--------------------------------

-	.muted <p class="muted">Fusce dapibus, tellus ac cursus commodo, tortor mauris nibh.</p>
-	.text-warning <p class="text-warning">Etiam porta sem malesuada magna mollis euismod.</p>
-	.text-error <p class="text-error">Donec ullamcorper nulla non metus auctor fringilla.</p>
-	.text-info <p class="text-info">Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis.</p>
-	.text-success <p class="text-success">Duis mollis, est non commodo luctus, nisi erat porttitor ligula.</p>

缩写 Abbreviations
--------------------------

-	`<abbr title="attribute">attr</abbr>`
-	add .initialism to an abbreviation for a slightly smaller font-size

地址 Addresses
----------------------

-	`<address>` preserve formatting by ending all lines with `<br>`

引用 Blockquotes
-------------------------

-	Default blockquote
	-	Wrap `<blockquote>`around any HTML as the quote.
	-	For straight quotes recommend a <p>
-	Blockquote options
	-	Naming a source
		-	Add <small> tag for identifying the source
		-	Wrap the name of the source work in <cite>
	-	Alternate displays
		-	use .pull-right for floated, right-aligned blockquote

列表 Lists
---------------------

-	Unordered
	`<ul> & <li>`
-	Ordered
	`<ol> & <li>`
-	Unstyled
	-	use .unstyled for `<ul>` to remove the default list-style and left padding on list items(immediate children only)
-	Inline
	-	use .inline for `<ul>` to place all list items on a single line with inline-block and some light padding

描述 Description
----------------------
`<dl> & <dd>`

-	Horizontal description
	-	use .dl-horizontal for dl to make terms and descriptions in `<dl>` line up side-by-side

NOTE: Horizontal description lists will truncate terms that are too long to fit in the left column fix text-overflow