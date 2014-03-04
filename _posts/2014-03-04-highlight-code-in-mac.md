---
layout: post
title: 在Keynote演示中使用语法高亮
categories: Mac, 工作
tags: Mac, Keynote,  RTF
---

作为一名程序YUAN，不管你是初级中级还是高级，总有一天会开始传道授业解惑。如果你同时也是一名MAC用户，那么肯定会遇到需要在`Keynote`当中粘贴程序代码的时候。乔帮主给我们留下了这么精致的Keynote，如果在里面贴一点都没有美感的纯文本代码，绝逼不是我们的完美主义倾向可以容忍的！

可惜乔帮主没写过代码，不会冲进Keynote开发组大喊：“你们这帮蠢货！我们需要Keynote支持语法高亮，我们的用户需要这个！”我们只能通过第三方工具来帮忙了。

只需要简单四步，我们就可以实现在Keynote中粘贴语法高亮的美丽代码。

### Step 0

---

首先安装 MAC 上的 `Apt-get`[ **Homebrew** ](http://mxcl.github.com/homebrew/)，不知道这是何物和还没有安装的童鞋请猛戳链接。

### Step 1

----

通过命令行

    brew install highlight 
    
安装 [highlight](http://www.andre-simon.de/) 工具。工具使用在 Step 2，需要了解更多的可戳 [Highlight Wiki](http://www.andre-simon.de/)

### Step 2

---

加入你要高亮的内容存放在 `index.php` 中，执行

    highlight -O rtf index.php | pbcopy
    
highlight 会把高亮后的代码内容以**rtf**保存在剪贴板中，**rtf**就是 **Rich Text Format** 是mac支持的富文本格式。

很多情况下只需要格式化一段内容，那么可以把内容复制后，执行：

    pbpaste | highlight -O rtf -S java | pbcopy
    
上面假设需要高亮的是java代码，你可以把java替换成任意你喜欢的语言，只要 pygments 支持。 支持的语言列表请戳 [Pygments Supported Languages](http://pygments.org/languages/)

### Step 3

---

在Keynote中粘贴，然后调整位置、调整字体。 推荐在文本加上打字过渡效果。

**一个高大上的精美技术演示就这样产生了。 撒花~**
