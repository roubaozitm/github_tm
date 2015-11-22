#!/usr/bin/env python
from __future__ import division
import math
def f(a,b,c):
    x1 = (math.sqrt(b**2-4*a*c)-b)/(2*a)
    x2 = -(math.sqrt(b**2-4*a*c)+b)/(2*a)
    return x1,x2
print f(1,-2,1)
