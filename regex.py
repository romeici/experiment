#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import re

def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return True
    return False

addr='romeici@a1.com'
print(validateEmail('romeici@163.com'))
print(validateEmail(addr))

