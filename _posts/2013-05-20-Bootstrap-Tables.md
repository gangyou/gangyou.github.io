---
layout: page
title: Bootstrap学习笔记3-表格
description: Bootstrap学习笔记3-表格
catrgory: Front-End
tags: [css, twitter, bootstrap, tables]
---

表格
===================

默认 Default styles
--------------------
for basic styling-light padding and only horizontal dividers-add the base class .table to any <table>

可选Table属性 Optional classes
---------------------------
Add any of the following classes to the .table base class

-	.table-striped: zebra-striping
-	.table-bordered: add borders and rounded corners to the table
-	.table-hover: enable a hover state on table rows
-	.table-condensed: makes tables more compact by cutting cell padding in half

可选行属性 Optionnal row classes
-----------------------------------
Add any of the following classes to the tr tag

-	.success: Indicates a successful or positive action
-	.error: Indicates a dangerous or potentially negative action
-	.warning: Indicates a warning that might need attention
-	.info: used as an alternative to the default styles

支持的Table标签 Supported table markup
--------------------------------------
List of supported table HTML elements and how they should be used
	<table>: Wrapping element for displaying data in tabular format 
	<thead>: Container element for table headers rows(<tr>) to label table columns
	<tbody>: Container element for table rows(<tr>) in the body of the table
	<tr>: Container element for a set of table cells that appears on a single row
	<td>: Default table cell
	<th>: Special table cel for column labels
	<caption>: Description or summary of what the table holds, especially useful for screen readers