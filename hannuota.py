#!/usr/bin/python
#_*_coding:utf-8
'''
def hanoi(disc, src, aux, dst):
    if (disc > 0):
        hanoi(disc - 1, src, dst, aux)
        print('Move disc %d from %s to %s'%(disc,src,dst))
        hanoi(disc - 1, aux, src, dst)


hanoi(3,'Src','Aux','Dst')
'''
'''
def move(n, a, b, c):
    if n ==1:
        print a, '-->', c
        return
    move(n-1, a, c, b)
    print a, '-->', c
    move(n-1, b, a, c)
move(3, 'A', 'B', 'C')

'''
def fourHanoi(a, b, c, d, n):
	global i
	i=0
	if n == 1:
		print("please move the number is ", n,"plate from the base", a, "to the base", d)

	elif n == 2:
		print("please move the number is ", n-1,"plate from the base", a, "to the base", b)
		print("please move the number is ", n,"plate from the base", a, "to the base", d)
		print("please move the number is ", n-1,"plate from the base", b, "to the base", d)
	else:
		fourHanoi(a, b, d, c, n - 2)
		print("please move the number is ", n-1,"plate from the base", a, "to the base", b)
		print("please move the number is ", n,"plate from the base", a, "to the base", d)
		print("please move the number is ", n-1,"plate from the base", b, "to the base", d)
		fourHanoi(c, a, b, d, n - 2)
n = input("please input the number of plate: ")
fourHanoi("a", "b", "c", "d", n)

'''

def hannota(a,b,c,n):
	if n == 1:
		print ("move",n,"from",a,"to", d)
	if n == 2:
		print ("move",n,"from",a,"to", c)
		print ("move",n-1,"from",a,"to", d)
	if n == 3:
		print ("move",n,"from",a,"to", d)
'''

'''
def move(n, a, b, c):
    if n ==1:
        print "move", a, '-->', c
    elif n ==2:
        print n,"move",a,'--->',b
        print n-1,"move",a,'--->',c
        return
    move(n-1,a,c,b)
    print "move",a,'--->',c
        #move(n-1,b,a,c)
    if n%2 ==0:
        move(n-1,b,a,c)
    else:
        move(n-1,a,c,b)
        print "move",a,'-->',c

        move(n-1,a,c,b)


        #move(n-1,a,c,b)
        #print n,"move",a,'--->',c
        #move(n-2,b,a,c)
        #print n,"move",c,'---->',b

move(3, 'A', 'B', 'C')
'''

'''
from time import sleep
import sys
def disp_sym(num, sym):

        print sym*num,
#recusion
def hanoi(a, b, c, n, tray_num):
 if n == 1:
  move_tray(a, c)
  disp(tray_num)
  sleep(0.7)
 else:
  hanoi(a, c, b, n-1, tray_num)
  move_tray(a, c)
  disp(tray_num)
  sleep(0.7)
  hanoi(b, a, c, n-1, tray_num)
def move_tray(a, b):
 for i in a:
  if i != 0:
   for j in b:
    if j != 0:
     b[b.index(j) - 1] = i
     a[a.index(i)] = 0
     return
   b.append(i)
   b.pop(0)
   a[a.index(i)] = 0
   return

def disp(tray_num):
 global a, b, c
 for i in range(tray_num):
  for j in ['a', 'b', 'c']:
   disp_sym(5, ' ')
   eval('disp_sym(tray_num - ' + j + "[i], ' ')")
   eval('disp_sym(' + j + "[i], '=')")
   disp_sym(1, '|')
   eval('disp_sym(' + j + "[i], '=')")
   eval('disp_sym(tray_num - ' + j + "[i], ' ')")
  print()
 print('---------------------------------------------------------------------------')
tray_num=int(input("Please input the number of trays:"))
tray=[]
for i in range(tray_num):
 tray.append(i + 1)
a=[0]*tray_num
b=a[:]
c=a[:]
a = tray[:]
disp(tray_num)
hanoi(a, b, c, tray_num, tray_num)
'''