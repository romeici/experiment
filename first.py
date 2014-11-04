#!/usr/bin/env python
# -*- coding: utf-8 -*-
print 'I\'m ok.'

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
		
print my_abs(-100)	
print my_abs(-100.01)	
# print my_abs('A')

# return NONE
def nop(age):
	if age >= 18:
		pass     
	else:
		print 'age: %d' % age
		
nop(20)
nop(15)

# return multiple value
 
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
	
x, y = move(100, 100, 60, math.pi / 6)
print x, y

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
	
print power(5) , ',', power(5,3)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

a=[1,2,3,6]
b=[1,3,5,9,8,7]
print calc(*a)
print calc(*b)

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

a=[1,2,3,6]
b=[1,3,5,9,8,7]
print calc(a)
print calc(b)

fread = open('for_read.txt', 'r')
res=fread.read()
print res
fread.close

f = open('for_read.txt', 'w+')
data=['adc ','adaa ','adafe ']
for data_in in data:
	f.write(data_in)
f.close

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(10)
print fact(5)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1
fib(10)

g = (x * x for x in range(10))
print g.next()
print g.next()
for n in g:
	print n
	
l = [x*x for x in range(10)]
for n in l:
	print n
	
def fib_1(max,beg1 = 0,beg2 = 1):
	n, a, b = 0,beg1,beg2
	while n < max:
		print b
		a, b = b, a + b
		n = n + 1
		
fib_1(5)		
fib_1(5, 0, 1)
fib_1(5, 0, 2)
# map(f,[])  高阶函数
map(fib_1, [1,2,3,4,5])

L = ['Hello', 'World', 'IBM', 'Apple']
for n in L:
	print [n.lower()]

print [s.lower() for s in L]

print sorted([36, 5, 12, 9, 21])

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
	
print sorted( [6,3,8,5,4,7,1], reversed_cmp)

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
	
print sorted(['about', 'bob', 'Zoo', 'Credit'], cmp_ignore_case)	

def now():
	print '2013-12-25'
	
f = now
f()
print f.__name__
print now.__name__

print int('12345', 10)
print int('12345', 16)
#偏函数
def int2(x, base=2):
    return int(x, base)
	
import urllib2
#encoding = utf-8
class Crawler:
    def main(self):
        #req = urllib2.Request('http://www.baidu.com/')
        #req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0)')
        #urllib2.socket.setdefaulttimeout(10) # 超时10秒
        #page = urllib2.urlopen(req)
        page = urllib2.urlopen('http://www.baidu.com', timeout=10)
        data = page.read()
        print data
        print len(data)  #计算字节长度
	
if __name__ == '__main__':
    me=Crawler()
    me.main()


import os, sys
os.system('curl ' + url)
os.system('curl -D baidu ' + url)	