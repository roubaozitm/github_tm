#!/usr/bin/python
def fuck(l):
    new = []
    for s in l:
        if isinstance(s,str):
            x = s.upper()
#        else:
#            x = s
            new.append(x)
    return new

print fuck(['Hello','world',101])
