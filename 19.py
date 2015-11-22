class Person(object):
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count += 1
	print Person.count

p1 = Person('Bob')

p2 = Person('Alice')

p3 = Person('Tim')
