#!/usr/bin/env python
def f(n):
    if n > 0:
        s = n * f(n - 1)
    if n == 0:
        s = 1
    return s



print f(5)
