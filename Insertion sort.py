arr=[5,3,1,2,4]
arr=[3,1,2,4]
for i in range(len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and key<arr[j]:
        arr[i],arr[j]=arr[j],arr[i]
        # arr[j+1]=arr[j]
        # temp=arr[i]
        # arr[i]=arr[j]
        # arr[j]=temp
        j-=1
    arr[j+1]=key

print(arr)
