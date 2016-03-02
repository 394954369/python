#!/usr/bin/python
coding=utf-8

def foo():
	'''
	生成器
	'''
	yield 1    



a = range(10)
'''
a = ['0','1','2','3','4','5','6','7','8','9','10']
这里会直接在内存中生成一个列表
'''
b = xrange(10) 
'''
xrange 就是一个生成器，这里b什么都没有生成
只有当遍历的时候才会生成，每次循环只执行一次
'''

re = foo()

for item in re:
	print item
	'''
	这里会生成为1
	'''


def readline():
	seek = 0
	with open('/tmp/123.txt','r') as f: 
		'''
		with 的用法就是一般用于打开文件，当离开代码所在
		缩进，则with会自动将文件关闭，会自动 f.close()
		'''
		f.seek(seek) 
		#seek 会跳转到到指定字符处
		data = f.readline()
		#这里会读一行
		if data:
			seek = f.tell()
			yield data
		else:
			return


for item in readline():
	print item 

