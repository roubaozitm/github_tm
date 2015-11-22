#!/usr/bin/env python
def square_of_sum(L):
    a = []
    for l in L:
        s = l * l
        a.append(s)
    return sum(a)


print square_of_sum([1,2,3])
