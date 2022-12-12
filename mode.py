arr=[1,2,3,2,3,2
,2,3,4,5]
d={}
i=0
while i<len(arr):
    count=0
    j=0
    while j<len(arr):
        if arr[j]==arr[i]:
            count+=1
        j+=1
    if 1<count:
        d[count]=arr[i]
    i=i+1
max=0
for i in d:
    if max<i:
        max=i
print(d[max])
