#!/usr/bin/python
#_*_ coding=utf-8
'''
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



'''

#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
def input_n():

    while True:
        n = raw_input('请输入A上的盘子个数:')
        try:
            n = int(n)
            if n < 1:
              print '请输入大于0的整数!'
            else:
              break
        except Exception, e:
            print '请不要随意输入字符!'

    return n

def move_info(n, from_table, to_table):

    step_info = '将%s号盘:%s ----> %s' % (n, from_table, to_table)
    return step_info

def recursion_hano(n, a, b, c, step_info_list = []):

    if n == 1:  # 当n=1时，直接将盘子移动至目的桌，递归终止条件
        step_info_list.append(move_info(1, a, c))

    else:
        recursion_hano(n-1, a, c, b)  # 先借助C将A上n-1个盘子移至B
        step_info_list.append(move_info(n, a, c))  # 将A最后一个盘子移动到C
        recursion_hano(n-1, b, a, c)  # 借助A将B上的n-1个盘子移至C

    return step_info_list

def main():

    n = input_n()
    step_info_list = recursion_hano(n,'A', 'B', 'C')
    for i,k in enumerate(step_info_list):
        print '第%s步:%s' % (i+1, k)


if __name__ == '__main__':
    main()
'''
def fourHanoi(a, b, c, d, n):
	global i
	i=0
	if n == 1:
		print("将盘号为 ", n,"的盘子从", a, "移动到", d)

	elif n == 2:
        print ("将盘号为 ", n-1,"的盘子从", a, "移动到", b)
        print ("将盘号为 ", n,"的盘子从", a, "移动到", d)
        print ("将盘号为 ", n-1,"的盘子从", b, "移动到", d)
    '''
		#print("please move the number is ", n-1,"plate from the base", a, "to the base", b)
		#print("please move the number is ", n,"plate from the base", a, "to the base", d)
		#print("please move the number is ", n-1,"plate from the base", b, "to the base", d)
	'''
	else:
		fourHanoi(a, b, d, c, n - 2)
        print ("将盘号为 ", n-1,"的盘子从", a, "移动到", b)
        print ("将盘号为 ", n,"的盘子从", a, "移动到", d)
        print ("将盘号为 ", n-1,"的盘子从", b, "移动到", d)
		#print("please move the number is ", n-1,"plate from the base", a, "to the base", b)
		#print("please move the number is ", n,"plate from the base", a, "to the base", d)
		#print("please move the number is ", n-1,"plate from the base", b, "to the base", d)
		fourHanoi(c, a, b, d, n - 2)
n = input("please input the number of plate: ")
fourHanoi("a", "b", "c", "d", n)