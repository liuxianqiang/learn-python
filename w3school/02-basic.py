#!/usr/bin/python
# -*- coding: UTF=8 -*-

#标识符

#保留字符

#行与缩进
#缩进代替{}
#缩进是python语法的一部分, 空行不是.

#多行语句
total = 1 + \
        2 + \
        3
print total

strs = "hello world " + \
       "python!"
print strs

lists = [1, 2, 3, 4,
         5, 6, 7, 8]
print lists

#引号
str1 = 'hello world'
str2 = "hello world"
str3 = """ hello
        world"""
print str1
print str2
print str3

#注释
#只有单行注释

#用户输入
input1 = raw_input("\n\nPress the enter key to exit.")
print input1

#同一行使用多条语句
var1 = "var1"; var2 = "var2"; var3 = "var3"
print var1, var2, var3

#expression vs statement
if 1 > 0:
    print 1
else:
    print 0

#python 命令行参数
#帮助 python -h
#版本 python -V
