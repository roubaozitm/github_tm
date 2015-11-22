#!/usr/bin/env python
from __future__ import division
def average(*args):
    lenth = len(args)
    sums = 0
    for num in args:
        sums += num
    return sums / lenth

print average(1,2)
print average(1,2,4)

