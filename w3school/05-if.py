#!/usr/bin/python
# -*- coding: UTF=8 -*-

#选择(if elif else), 没有switch开关语句
num = 3     
if num == 3:            # 判断num的值
    print 'boss'        
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出
    print 'error'
else:
    print 'roadman'     # 条件均不成立时输出

#简单if语句
if 1 > 0: print '1 > 0'
