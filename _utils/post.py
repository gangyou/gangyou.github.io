# coding:utf8

import argparse
from os import path
from datetime import date
from re import sub

DEFAULT_FORMAT_MATTER = '''---
layout: post
title: {}
published: false
---
'''

def create_post_file(title):
    today = date.isoformat(date.today())
    file_title = sub("\s+", "-", title.lower())
    post = open("../_posts/{}-{}.md".format(today, file_title), "w")
    # 输出FrontMatter
    post.write(DEFAULT_FORMAT_MATTER.format(title))
    post.close()
    return post

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("title", type=str, help="title of post")

    args = parser.parse_args()

    if args.title:
        f = create_post_file(args.title)
        if f:
            print "Created: ", path.abspath(f.name)
            return

if __name__ == '__main__':
    main()


