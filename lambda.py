#!/usr/bin/python
#_*_ coding=utf-8
#lambda表示匿名函数 没有名称
#相当于一个匿名函数有两个参数x y
#然后返回一个值为 x+y相当于
'''
def tempx(x,y):
    print x+y
''' 
temp = lambda x,y:x+y
print temp(4,6)
