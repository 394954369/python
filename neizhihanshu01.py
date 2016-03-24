#!/usr/bin/python
#_*_ coding=utf-8


a = []
help(a)
#help 可以列出整个使用方法

print dir()
#dir 列出该模块的所有方法,相当于给出key
print vars()
# vars 不仅给出方法而且给出值,相当于给出key 也给出value
print type(a)
# 查看a的类型
b = 111
print id(b)
#id 表示的是查看a的内存地址
print divmod(9,4) 
# dirmod 这里表示的是商和余数得出的为（2,1）

print all([1,2,3,4,0])
#all()返回一个bool值,里面数据有一个不为真则为false

print any([1,2,3,4,0])
#any()返回一个bool值,里面数据有一个为真则为真

print chr(65)
# 表示一个Ascii码的生成 65--->A
print ord('A')
#表示一个Ascii的值 A--->65

print hex(2) 
#表示16进制 0X2

print bin(2)
#表示8进制ob10

print oct(2)
#表示2进制 02



li = ['ss','ssdf','fff']

for item in enumerate(li,1):
    print item
#enumerate 为列表加了一个序列 1 表示从将1作为起始值，默认为0

#(1, 'ss')
#(2, 'ssdf')
#(3, 'fff')

for item in enumerate(li,1):
    print item[0],item[1]
help(enumerate)
#1 ss
#2 ssdf
#3 fff


s = 'i am {0},{1}'

print s.format('yyp','goodboy')

#i am yypgoodboy  格式化输出 等同于%s 等














