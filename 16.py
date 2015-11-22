from math import sqrt
def sqrt_is_odd(num):
    if sqrt(num) % 2 == 0 or sqrt(num) % 2 == 1:
        return 1 
    else :
        return 0


print filter(sqrt_is_odd,range(1,101))  
