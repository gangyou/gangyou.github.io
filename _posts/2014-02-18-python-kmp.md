---
layout: post
title: "用Python实现KMP算法"
description: "kmp algorithm implemented by python"
category: Coding
tags: [Python, Coding, Algorithm]
---
前几天完完整整的看完了阮一峰老师写的[字符串匹配的KMP算法](http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html) 。文章深入浅出，将KMP算法剖析的相当彻底，难得的好文章，推荐大家看看。

顺便想起要多练习练习之前掌握的Python，就给自己布置了一个作业：用Python 实现KMP算法。

整个练习过程加上测试案例的编写历时大概1个多小时，疏于编程思维训练的结果啊！

最后的代码如下，测试案例用的是阮一峰老师文章中的示例

{% highlight python %}
    # coding:utf8
    
    def kmp_search(by_search, keyword):
        '''kmp 字符串搜索算法'''
        table = partial_match_table(keyword)
        compare_index, partial_index, saved_index = 0, 0, 0
        while compare_index < len(by_search):
            # 记录当前主字符串匹配位置
            saved_index = compare_index
            # 已匹配的字符数
            matched_numbers = 0
            for partial_index in range(len(keyword)):
                if by_search[compare_index] != keyword[partial_index]:
                    break
                else:
                    compare_index += 1
                    matched_numbers += 1
    
            print matched_numbers
            # 第一个字就不匹配
            if not matched_numbers:
                compare_index = saved_index + 1
            # 部分匹配
            elif matched_numbers < len(keyword):
                move_steps = matched_numbers - table[keyword[:matched_numbers]]
                compare_index = saved_index + move_steps
            # 全部匹配
            else:
                return saved_index
            print "Compare Index: {}, Matched Numbers: {}".format(saved_index, matched_numbers)
    
        return -1
    
    def partial_match_table(keyword):
        '''计算查找关键词的部分匹配表'''
        table = {}
        if not keyword:
            return table
        for i in range(len(keyword)):
            part_keyword = keyword[:i+1]
            table[part_keyword] = common_partials(part_keyword)
        return table
    
    def common_partials(keyword):
        '''关键词前缀和后缀的共同元素
            "前缀"指除了最后一个字符以外，一个字符串的全部头部组合；"后缀"指除了第一个字符以外，一个字符串的全部尾部组合。
            "ABCD"的前缀为[A, AB, ABC]，后缀为[BCD, CD, D]，共有元素的长度为0；
        '''
        if not keyword: return 0
        prefix_set = get_prefix_set(keyword)
        suffix_set = get_suffix_set(keyword)
        # print prefix_set.intersection(suffix_set)
        commons = set(prefix_set).intersection(set(suffix_set))
        if not commons: return 0
        else: return len(commons.pop())
    
    def get_prefix_set(keyword):
        ''' 计算关键词的前缀 '''
        prefixs = []
        for i in range(1, len(keyword)):
            prefixs.append(keyword[:i])
        return set(sorted(prefixs, lambda x,y: cmp(len(x), len(y))))
    
    def get_suffix_set(keyword):
        ''' 计算关键词的后缀 '''
        suffixes = []
        for i in range(1, len(keyword)):
            suffixes.append(keyword[i:])
        return set(sorted(suffixes, lambda x,y: cmp(len(x), len(y))))
    
    if __name__ == '__main__':
        by_search = 'BBC ABCDAB ABCDABCDABDE'
        keyword = 'ABCDABD'
    
        excepted_partial_match_table = {
            'A': 0, 'AB': 0, 'ABC': 0, 'ABCD': 0,
            'ABCDA': 1, 'ABCDAB': 2, 'ABCDABD': 0 
        }
    
        assert get_prefix_set('ABCDA') == set(('A', 'AB', 'ABC', 'ABCD')), "前缀表达式测试失败 {}".format(get_prefix_set('ABCDA'))
        assert get_suffix_set('ABCDA') == set(('BCDA', 'CDA', 'DA', 'A')), "后缀表达测试失败 {}".format(get_suffix_set('ABCDA'))
    
        # Test for common_partials
        assert common_partials('') == 0
        assert common_partials('A') == 0
        assert common_partials('AB') == 0
        assert common_partials('ABC') == 0
        assert common_partials('ABCD') == 0
        assert common_partials('ABCDA') == 1
        assert common_partials('ABCDAB') == 2
        assert common_partials('ABCDABD') == 0
    
        assert partial_match_table(keyword) == excepted_partial_match_table, "计算出来的部分匹配表不一致 {} ".format(partial_match_table(keyword))
        assert kmp_search(by_search, keyword) == 15, "存在匹配，返回匹配位置 {}".format(kmp_search(by_search, keyword))
        assert kmp_search(by_search, keyword + 'Not exist') == -1, "不存在匹配模式，应该为 -1"
{% endhighlight %}

如果有幸被各位程序YUAN们阅读到，欢迎多提意见谢谢~
