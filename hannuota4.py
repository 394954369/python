#!/usr/bin/python
#_*_ coding=utf-8


'''
def min(n,k):
    min_num = 0
    if n ==1:
        return min_num = 1
    elif n ==2:
        return min_num = 3

    else:
        for i in n:
            for k in i:
                min(i,k)
            f = 2min(n) + (2**(n-k) -1)
'''
def min_move(n):
    min_num = {}
    if n == 1:
        min_num[1] = 1
    if n == 2:
        min_num[n] = 3
    for i in range(3,n):



        min_move(n)
    #    min_i = []
        min_move(n-i)
        #min_num[i-1] = min_move(n-i)
          #  temp = 2*(min_move(n-i))+2**(i)-1
        min_i.append(temp)



min_move(5)



'''
def f3(n,a,b,c):
    if n ==1:
        print a, '-->', c
        return
    move(n-1, a, c, b)
    print a, '-->', c
    move(n-1, b, a, c)

def f4(n,a,b,c,d,k):
    if n ==1:
        print "move",a,'--->',d
    elif n ==2:
        print "move",a,'---->',b
        print "move",a,'---->',d
        print "move",b,'---->',d
    else:
        f4(n-k,a,c,d,b,k)
        f3(k,a,c,d)
        f4(n-k,b,a,c,d,k)

f4(4,"A","B","C","D",1)
'''