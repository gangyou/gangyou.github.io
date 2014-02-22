---
layout: page
title: Bootstrap学习笔记4-表单
description: Bootstrap学习笔记4-表单
catrgory: Front-End
tags: [css, twitter, bootstrap, form]
---


Default styles
---------------

-	form
-	fieldset
-	legend
-	label tags results in stacked
-	left-aligned labels on top of form controls

Optional layouts
------------------

###Search form
	Add .form-search to the form and .search-query to the `<input>` for an extra-rounded text input
###Inline form
	Add .form-inline for left-aligned labels and inline-block controls for a compact layout
	NOTE: Add .input-small to the input results in a shorted input width
###Horizontal form
	Right align labels and float them to the left to make them appear on the same line as controls. Requires the most markup changes from a default form:

-	Add .form-horizontal to the form
-	Wrap labels and controls in .control-group
-	Add .control-label to the label
-	Wrap any associated controls in .controls for proper alignment

Supported form controls
---------------------------

-	Inputs
-	Textarea
-	Checkboxes and radios

	-	Default

		<label class="checkbox">
			<input type="checkbox" value="">
			Option one
		</label>
		<label class="radio">
			<input type="radio" name="optionsRadios" id="options1" checked>
			Option Radio one
		</label>
		<label class="raido">
			<input type="radio" name="optionsRadios" id="options2" checked>
		</label>
	-	Inline checkboxes

		Add the .inline class to a series of checkboxes or radios for controls appear on the same line  
		<label class="checkbox inline">
		  <input type="checkbox" id="inlineCheckbox1" value="option1"> 1
		</label>
		<label class="checkbox inline">
		  <input type="checkbox" id="inlineCheckbox2" value="option2"> 2
		</label>
		<label class="checkbox inline">
		  <input type="checkbox" id="inlineCheckbox3" value="option3"> 3
		</label>
-	Selects
	
	Use the default option or specify a multiple="multiple" to show multiple options at once

Extending form controls
--------------------------

###Prepended and appended inputs
-	Default options

	Wrap an .add-on and an input with one of two classes to prepend or append text to an input
	<div class="input-prepend">
	  <span class="add-on">@</span>
	  <input class="span2" id="prependedInput" type="text" placeholder="Username">
	</div>
	<div class="input-append">
	  <input class="span2" id="appendedInput" type="text">
	  <span class="add-on">.00</span>
	</div>

-	Combined

	Use both classes and two instances of .add-on to prepend and append an input
	<div class="input-prepend input-append">
	  <span class="add-on">$</span>
	  <input class="span2" id="appendedPrependedInput" type="text">
	  <span class="add-on">.00</span>
	</div>

-	Buttons instead of text

	Instead of a <span> with text, use a .btn to attach a button (or two ) to an input.
	<div class="input-append">
	  <input class="span2" id="appendedInputButton" type="text">
	  <button class="btn" type="button">Go!</button>
	</div>

-	Button dropdowns

	<div class="input-append">
	  <input class="span2" id="appendedDropdownButton" type="text">
	  <div class="btn-group">
	    <button class="btn dropdown-toggle" data-toggle="dropdown">
	      Action
	      <span class="caret"></span>
	    </button>
	    <ul class="dropdown-menu">
	      ...
	    </ul>
	  </div>
	</div>

-	Segmented dropdown groups

	<form>
	  <div class="input-prepend">
	    <div class="btn-group">
	    	<button class="btn" tabindex="-1">Action</button>
	    	<button class="btn dropdown-toggle" data-toggle="dropdown" tabindex="-1">
              <span class="caret"></span>
            </button>
            <ul class="dropdown-menu">...</ul>
	    </div>
	    <input type="text">
	  </div>
	  <div class="input-append">
	    <input type="text">
	    <div class="btn-group">...</div>
	  </div>
	</form>

-	Search form

	<form class="form-search">
	  <div class="input-append">
	    <input type="text" class="span2 search-query">
	    <button type="submit" class="btn">Search</button>
	  </div>
	  <div class="input-prepend">
	    <button type="submit" class="btn">Search</button>
	    <input type="text" class="span2 search-query">
	  </div>
	</form>

Control sizing
--------------------

-	Block level inputs

	Make any `<input>` or `<textarea>` element behave like a block level element.

	<input class="input-block-level" type="text" placeholder=".input-block-level">

-	Relative sizing

	-	.input-mir 

	<input class="input-mir" type="text" />
	-	.input-small 

	<input class="input-small" type="text" />
	-	.input-medium

	<input class="input-medium" type="text" />
	-	.input-large

	<input class="input-large" type="text" />
	-	.input-xlarge

	<input class="input-xlarge" type="text" />
	-	.input-xxlarge

	<input class="input-xxlarge" type="text" />

-	Grid sizing

	Use .span1 to .span12 for inputs that match the same sizes of the grid columns  
	<input class="span2" type="text" placeholder=".span2">
	<select class="span2">
	  <optin>1</option>
	  <optin>2</option>
	</select>

	For multiple grid inputs per line, use the .controls-row modifier class for proper spacing. It floats the inputs to collapse white-space, sets the proper margins, and clears the float

Uneditable inputs
---------------------
.uneditable-input  
<input type="text" class="uneditable-input" value="Hello" disabled>

Form actions
----------------------
When placed within a .form-actions to form tag, the buttons will automatically indent to line up with the form controls.

Help text
----------------------
.help-inline .help-block

<input type="text"><span class="help-inline">Inline help text</span>  
<input type="text"><span class="help-block">A longer block of help text that breaks onto a new line and may extend beyond one line.</span>

Form control states
-------------------------

-	Input focus: auto removed by bootstrap
-	Invalid inputs: auto for html5 required property
-	Disabled inputs: auto for disabled
-	Validation states: .warning, .error, .info, .success
