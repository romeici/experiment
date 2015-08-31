#!/usr/bin/env python3
# -*-encoding:utf-8 -*-
__author__ = 'mxu2'

import this
s=this.s
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)
print(s)
print('--'*100)
print('python 之禅')
re=''.join([d.get(c,c) for c in s])
print(list(d.get(c,c) for c in s))
print(re)

