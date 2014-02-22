---
layout: page
title: Github Flavored Markdown(GFM)学习笔记
descirption: Github Flavored Markdown(GFM)学习笔记
catrgory: Blogging
tags: [Blog, Markdown, Github Pages]
---

[Github Flavored Markdown](https://help.github.com/articles/github-flavored-markdown)
==========================

与传统Markdown的不同
-------------------------

###New Lines
Markdown行的结尾默认不添加`<br>`,会造成格式混乱，GFM对于段落文字的换行以`<br>`处理

###Multiple underscores in words
GFM忽略单词连字符，比如 perform_complicated_task，中间的下划线将被忽略。在Markdown中会被当做emphasis处理

###Url autolinking
GFM中的标准url将被自动链接

###Fenced code blocks
GFM中可以用\`\`\`表示代码块，类似Python中的多行字符串语法

###Syntax highlighting
\`\`\`后紧跟语言名称，比如：  
\`\`\`ruby  
require 'redcarpet'  
markdown = Redcarpet.new('Hello World!')  
puts mardown.to_html  
\`\`\`
将产生
```ruby
require 'redcarpet'
markdown = Redcarpet.new('Hello World!')
puts mardown.to_html
```

###Task Lists
任务清单
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

###Quick quoting
仅在Github交互编辑器,键入r

###Name and Team @mentions autocomplete
仅在Github交互编辑器，键入@

另外还有Emoji autocomplete, issue autocomplete， Zend Mode writing 这些都要是在Github的编辑器中实现
