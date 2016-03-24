#!/usr/bin/python
#_*_ coding=utf-8


'''
a = '8*8'

print eval(a)

eval 可以将字符串直接当表达式进行使用

'''

'''
temp = 'sys'

model = __import__(temp)

__import__()  可以将字符串直接将模块导入
print model.path

'''
'''
func = getattr(model,'function')
获取model模块的函数名,并返回该函数
hasattr() 判断是否模块中有该函数
delattr() 从模块中删除该函数
'''