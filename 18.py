class Person(object):
    def __init__(self,name,gender,birth,job):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.job = job

p1 = Person('Xiao Ming', 'Male', '1990-1-1', 'Student')
p2 = Person('Xiao Hong', 'Female', '1991-10-1', 'Fucker')
p3 = Person('Xiao Qiang', 'Male', '1980-5-17', 'Worker')
p4 = Person('Xiao Zhang', 'Male', '1990-12-11', 'Student')
p5 = Person('Xiao Li', 'Male', '1990-1-10', 'Police')

print p2.name
print p5.job
