a=[3,3,5,4,1,6]
b=[4,3,2,1,3,7]
a.sort()
b.sort()
a.extend(b)
a.sort()
print(a)