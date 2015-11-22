#!/usr/bin/env python
#coding:utf-8

from __future__ import division

def jia(x,y):
    return x + y

def jian(x,y):
    return x - y

def cheng(x,y):
    return x * y

def chu(x,y):
    return x / y

hello = {'+':jia,'-':jian,'*':cheng,'/':chu}

def f(x,o,y):
    print hello.get(o)(x,y)



f(3,'-',2)

 

