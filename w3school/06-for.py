#!/usr/bin/python
# -*- coding: UTF=8 -*-

#循环(while, for, break, continue, pass)

#while, while:else
total = 0
i = 1
while (i < 10):
    total = total + i
    i = i + 1
else:
    print 'while is finished'
print total

#for
for letter in 'Python':     # First Example
    print 'Current Letter :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
    print 'Current fruit :', fruit

fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
    print 'Current fruit :', fruits[index]
else:
    print 'for is finished'
