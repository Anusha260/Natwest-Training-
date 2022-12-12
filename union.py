# union
a=[1,5,6,7]
b=[5,7,8,9]
c=a+b
print(c)

# intersection
new=[]
for i in a:
    if i in b:
        new.append(i)
print(new)
