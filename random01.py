#!/usr/bin/python
#_*_ coding=utf-8

import random

a = random.random()
print a
#random 生成随机数 值为在 0--1 之间


print random.randint(1,5)
# random定义一个区间,生成一个整数 该整数大于等于1小于等于5

print random.randrange(1,3)
#定义一个区间生成一个整数   该整数大于等于1 小于3

code = []
for i in range(6):
    if i == random.randint(1,5):
        code.append(str(random.randint(1,5)))
    else:
        temp = random.randint(65,97)
        code.append(chr(temp))
print ''.join(code)






