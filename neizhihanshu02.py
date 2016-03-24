#!/usr/bin/python
#-*- coding:utf-8

'''
def run(arg):
    print arg

apply(run,('t'))
# 等同于 run('t')
'''

'''
def foo(arg):
    return arg + 100

lis = [11,22,33]
temp = []
for item in lis:
    temp.append(item + 100)

print temp

# [111, 122, 133]
# 这里生成了一个新的列表
'''

'''
def foo(arg):
    return arg + 100

lis = [11,22,33]
temp = map(foo,lis)
temp = map(lambda x:x+100,lis)

print temp
# map 遍历列表后生成新的列表
'''

'''
lis = [11,22,33]
def foo(arg):
    if arg<22:
        return True
    else:
        return False
temp = filter(foo,lis)
# 一种过滤方法,只有当lis 中的数值在function foo 中为true 的才会有返回,
#如果是字符串或者元祖则返回字符串或元祖,除此之外返回列表
print temp
'''


'''
lis = [11,22,33]
print reduce(lambda x,y:x+y,lis)

# reduce 表示的为累加
'''
'''
help(reduce)
reduce(...)
    reduce(function, sequence[, initial]) -> value
    
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
'''


