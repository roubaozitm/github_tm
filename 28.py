class Student:
    def __init__(self,name,gender,score):
	self.name = name
	self.gender = gender
	self.score = score
    def __str__(self):
	return '(Student:%s,%s,%d)' %(self.name,self.gender,self.score)
    __repr__ = __str__


s = Student('Bob', 'male', 88)
print s
