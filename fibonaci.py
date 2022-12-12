arr=[0,1]
for i in range(2,11):
    arr.append(arr[-1]+arr[-2])
print(arr)

# ...........another way
a=0
b=1
i=0
while i<10:
    print(a)
    sum=a+b
    a=b
    b=sum
    i=i+1

