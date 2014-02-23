---
layout: post
title: 让Mac记住 Github 的账号密码
categories: Coding, OS
tags: Mac, Git, Github, SSH
---

在MAC工作平台上的你是否使用了 `**Git**`，那么你是否曾经在提交 Github 的时候，不停的输入你的用户名跟密码呢？ 本文就告诉你一个优雅而又安全的办法，来解决这个问题。

### Mac Keychain

让我们先把问题放一放，回想一下Mac上一个更加重要也更加常用的工具 **keychain**。来自 `wikipedia` 的说明是这样的：

> 钥匙串（英文：Keychain）是苹果公司Mac OS中的密码管理系统。它在Mac OS 8.6中被导入，并且包括在了所有后续的Mac OS版本中，包括Mac OS X。一个钥匙串可以包含多种类型的数据：密码（包括网站，FTP服务器，SSH帐户，网络共享，无线网络，群组软件，加密磁盘映像等），私钥，电子证书和加密笔记等。

那自然我们就可以想到为什么不把 Github 密码也存储到我们的钥匙串中呢？

### Github 钥匙

只要通过以下简单的配置就可以解决

    # Set git to use the osxkeychain credential helper
    git config --global credential.helper osxkeychain

经过这样的设置之后，下次再克隆 HTTPS 地址时会询问你的用户名和密码，并授权给 OSX keychain。完成这些之后你的用户名和密码就会存储到 keychain 中，再也不会在 Git 中询问了。

是不是很轻松？ Enjoy it！






