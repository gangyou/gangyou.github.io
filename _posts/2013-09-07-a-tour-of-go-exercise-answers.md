---
layout: post
title: "《A Tour of Go》练习答案"
description: "A tour of go exercise answers. Google Go语言教程《A tour of go》答案"
category: Coding 
tags: [Go]
---

自己的答案，仅作参考，不喜勿喷
使用中文版教程 [Go之旅中文版](http://go-tour-zh.appsp0t.com/ ) 编号跟英文版可能有部分不一致

{% highlight go linenos %}
// Exercise: Loops and Functions #24
package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z, s := float64(2.), float64(0)
	for {
		z = z - (z*z - x) / (2*z)
		if math.Abs(s - z) < 1e-15 {
			break;
		}
		s = z
	}
	return s
}

func main() {
	fmt.Println(Sqrt(2))
}
{% endhighlight %}

{% highlight go linenos %}
// Exercise 36: slice

package main

import "code.google.com/p/go-tour/pic"

func Pic(dx, dy int) [][]uint8 {
    result := make([][]uint8, dy)
    for i,_ := range result {
        
        result[i] = make([]uint8, dx)
        
        for j,_ := range result[i] {
        	result[i][j] = Value(i,j)
        }
        
    }
    return result
}

func Value(x, y int) uint8 {
    return uint8((x+y)/2)
}

func main() {
    pic.Show(Pic)
}
{% endhighlight %}

{% highlight go linenos %}
// Exercise 41 Map

package main

import (
    "code.google.com/p/go-tour/wc"
    "strings"
)

func WordCount(s string) map[string]int {
    var dict = make(map[string] int)
    for _,v := range strings.Fields(s) {
    	dict[v] += 1
    }
    return dict
}

func main() {
    wc.Test(WordCount)
   
}

{% endhighlight %}

{% highlight go linenos %}
//Exercise 44 fibonacci

package main

import "fmt"

// fibonacci 函数会返回一个返回 int 的函数。
func fibonacci() func() int {
    x,y := 0, 1
    return func() int{
    	x, y = x+y, x
        return x
    }
}

func main() {
    f := fibonacci()
    for i := 0; i < 10; i++ {
        fmt.Println(f())
    }
}

{% endhighlight %}
