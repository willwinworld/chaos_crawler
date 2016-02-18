# -*- coding: utf-8 -*-
''' L = [x*x for x in range(101)]
 print sum(L)

l = []
x = range(101)
for i in x:
    l.append(i*i)
print sum(l)

def square_of_sum(L):
    sum = 0
    for i in L:
        sum = sum + i*i
    return sum
print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])

import math

def quadratic_equation(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    return x1, x2
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)

def move(n,a,b,c): 

     if n==1:

            print a,'-->',c #这其实是只有一个圆盘需要从A到C的情况。所有递归，最终都是走到这一步。

            return #这是结束递归，省略了None。没有这句的话，递归没办法结束。

     move(n-1,a,c,b) #将A柱的n-1个盘移到B柱，这里毫无争议。注意形参顺序变化了。

     print a,'-->',c #这句话才是第一个柱子的第n个圆盘移动到目标柱子。

     move(n-1,b,a,c))#过渡柱子B上（n-1）个圆盘B递归移动到目标柱子C

def move(n, a, b, c):
    if n == 1:
        print a, '-->', c
        return
    move(n-1, a, c, b)
    print a, '-->', c
    move(n-1, b, a, c)
move(4, 'A', 'B', 'C')


def a():
    print 'aa'
    return  'gggg'
 
def b():
    a()
    print 'bb'

b()
'''



def move(n, a, b, c):
    if n ==1:
        print a, '-->', c
        return
    move(n-1, a, c, b)
    print a, '-->', c
    move(n-1, b, a, c)
move(3, 'A', 'B', 'C')


move(3, a, b, c)
    move(2, a, c, b)
        move(1, a, b, c)
            a -- c
        a -- b
        move(1, c, a, b)
            c -- b
    a -- c
    move(2, b, a, c)
        move(1, b, c, a)
            b -- a
        b -- c
        move(1, a, b, c)
            a -- c
            
            
#-*- coding:utf-8 -*-
# move(n, a, b, c)表示的是有n个盘子在a柱子上，将要移到c柱子上面去
def move(n, a, b, c):
# 如果a柱子上面只有一个盘子，则直接移到c柱子上面去并输出路径，结束递归
    if n == 1:  
        print a, '-->', c
        return
# 表示的是将n-1的盘子从a柱子上面移到b柱子上面去
    move(n-1, a, c, b)
# 输出最下面个盘子移从a移到c的路径
    print a, '-->', c
# 将b柱子上面的n-1个盘子移动到c柱子上面
    move(n-1, b, a, c)

move(4, 'A', 'B', 'C')









