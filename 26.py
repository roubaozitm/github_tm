def calc_prod(lst):
    def prod():
	a = 1
	for s in lst:
	    a *= s
	return a
    return prod

f = calc_prod([1, 2, 3, 4])
print f()
