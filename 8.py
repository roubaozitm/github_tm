#!/usr/bin/python
def Upper(string):
    init = string[0]
    tail = string[1:]
    Init = init.upper()
    return Init + tail

print Upper('fuck')
