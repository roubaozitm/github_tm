class Fib(object):

    def __init__(self,num):
	x = 0
	y = 1
	numi = 1
	self.l = [0,]
	self.num = num
	while numi <num:
	    x= x + y
	    y = x + y
	    self.l.append(x)    
	    self.l.append(y) 
	    numi = numi + 2  

    def __str__(self):
	self.printf = self.l[0:self.num]
	return str(self.printf)

    __repr__ = __str__

    def __len__(self):
	return self.num

f = Fib(10)
print f
print len(f) 
