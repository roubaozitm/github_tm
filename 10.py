d = {'Adam':95,'Lisa':85,'Bart':59,'Paul':64}
a = 0.0
for sorce in d.itervalues():
    a += sorce
print a / len(d)
