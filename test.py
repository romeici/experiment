#!/usr/bin/env python3
# -*-encoding:utf-8 -*-

__author__ = 'mxu2'

L=[2,8,3,50]
L.sort()
print(L)

a="123kljkoi908jkfdd"
print(a[::-1])

string = ''
#string1 = raw_input('Enter a string:')
string1 = 'this is a test'

list1 = string1.split(' ')
list2 = list1[::-1]
for x in range(0,len(list2)):
    string += list2[x] + " "
print(list1,list2,string)

a={1:1,2:2,3:3,9:8,7:9,5:4}

keys=list(a.keys())
st=''
for i in range(len(keys)):
    st+=str(keys[i])
    if i<len(keys)-1:
        st+=','
#st="".join(str(keys))
print(st)

#输出倒序奇数位置字符
a='123afe'
print(a[::-2])

l=[2];
for i in range(3,100):
    if not[i for t in l if i%t==0]:
        l.append(i);
print(' '.join(str(k) for k in l))

import re
address="romeici@163.com"

bt='print("fdfadfadf")'
eval(bt)

# 最小公倍数
def min_mult(x,y):
    for i in range(max(x,y),x*y+1):
        if ((i%x) == 0) & ((i%y) == 0):
            return i
#        print(i)

print(min_mult(15,25))
print(min_mult(6,8))

#矩阵面积和周长
a=3;b=4
print('area:' + str(a*b) + ' '+ "circumference:" +str(2*(a+b)))

#结尾0的个数
L=[200,8,30,500,0,50000000000000]
sum=0;a=0;b=0;
for i in L:
    if i is not 0:
        while i%2==0:
            i=i/2
            a+=1
        while i%5==0:
            i=i/5
            b+=1
    else:
        a=b=1;
    sum+=min(a,b)
    a=0;b=0
print("sum:%d" % sum)


#信息加密
alphabet = "abcdefghijklmnopqrstuvwxyz";
a="adfadfecekljkifoafe";b=3
n = list(map(lambda x : alphabet[(alphabet.index(x)+b)%26],a))
print("".join(n))

str1='adfaloVeladkjfoel ljadafe'
def flove(s):
    if  s.lower().find('love') >= 0:
        return 'love'
    else:
        return 'single'

print(flove(str1))

import sys
import os
import re

f=os.popen('dir')
str=f.read()
print(str)
deb='08/31/2015  03:46 PM             2,206 test.py'
sa='.*(\.py)+'
ra=re.match(sa, deb)
if ra is not None:
    print(ra.group())
else:
    print(None)
f.close



patt='(\w+\s\w+)+\@\w+[a-zA-Z0-9\-\~]{1,20}\.+(com|cn|bat|txt|py)$'
str='windriver d@windriver~wind~-.py'
m=re.match(patt,str)
if m is not None:
    rs=m.group()
    print(m.group())
else:
    print(None)

patt='(bat|bit|but|hat|hit|hut)'
#patt='^(bat|bit|but|hat|hit|hut)$'
str='hut but but bat hut hit hat'
m=re.findall(patt,str)
print(m)
if m is not None:
    print(m[0])
else:
    print(None)

t=re.search(patt,str)
print(t)