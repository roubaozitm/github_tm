#!/usr/bin/env python
def move(n,a,b,c):
    if n == 1:
        print a,'-->',c
    elif n == 2:
        print a,'-->',b
        print a,'-->',c
        print b,'-->',c
    else:
        print a,'-->',b
        move(n-1,a,b,c)


s = int(raw_input('Please input num:'))
move(s , 'A', 'B', 'C')
