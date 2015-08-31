#!/usr/bin/env python3
# -*-encoding:utf-8 -*-

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