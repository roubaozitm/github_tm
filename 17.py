import re
f = open('a.t','r')
s = f.readlines()
f.close()
re_x = r'hahaha'
re_x_o = re.compile(re_x)
lall = []
for x in s:
    l = re.sub(re_x_o,'reh',x)
    lall.append(l)
f = open('a.t','w')
f.writelines(lall)
f.close()

