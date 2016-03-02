

def show(*arg):
	'''
	这里*arg代表可以传递多个参数，该函数会将这些参数
	转换成列表来使用
	'''
	for item in arg:
		print item

show('yang','ya','ma')
		'''
		输出结果为
		yang
		ya
		ma
		'''

假如直接传递一个列表的话 
list = ['1','2', '3']
show(*list)  这样才可以直接使用 *list




def show2(**kargs):
	'''
	这个**kargs呆料可以传递多个参数，该函数可以将这些
	参数转换成字典使用
	'''
	for item in kargs.iterms():
		print item

show2(name = 'yang'，age = '25')
'''
输出结果为
（'name', 'yang'）
('age', '25')
'''


user_dict = {'k1':123,'k2':456}
show2(**user_dict)    
'''这里如果直接传递为字典需要加上**
上面一种直接传入key=value 这样就不需要需要**'''



def fun(arg,*arg,**kargs):
	pass