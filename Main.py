# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 10:59:45 2018

@author: s-siraki
"""

import sys

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

a = int(input('Inuput 1st Number.\n'))
b = int(input('Inuput 2nd Number.\n'))

op = int(input('Choice operation. Plus:1, Minus:2\n'))

if op == 1:
    x = plus(a,b)
elif op ==2:
    x= minus(a,b)
else:
    print('Error:Invalid　Operator.')
    sys.exit(1)

print('The answer is ' + str(x) + '.')

