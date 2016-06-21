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










#!/usr/bin/env python
# _*_ coding:utf-8 _*_



def pate_number():

    while True:
        n = raw_input('请输入A底座上总共多少盘子(盘子数量大于0):')
        try:
            n = int(n)
            if n < 1:
              print '请输入大于0的整数!'
            else:
              break
        except Exception as e:
            print "this is a error"

    return n

def move(n, src_base, dest_base):

    #step = '将%s号盘:%s ----> %s' % (n, scrap_styles, to_tase)
    step = '将',src_base,'号盘移动到:',dest_base
    return step

def hano4(n, a, b, c, d):
     if n == 1:
        move(n,a,d)
    elif n ==2:
        move(n-1,a,b)
        move(n,a,d)
        move(n-1,b,d)

     else:
        hano4(n-2, a, b, d,c)
        move(n-1,a,b)
        move(n,a,d)
        move(n-1,b,d)
        hano4(n-2, c, a, b,d)

def main():

    n = input("please input the number of the plate")
    han4(n,"A","B","C","D")


if __name__ == '__main__':
    main()







