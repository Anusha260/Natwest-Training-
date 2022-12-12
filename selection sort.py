arr=[5,4,2,3,1]
for i in range(len(arr)):
    min=i
    for j in range(i+1,len(arr)):
        
        if arr[min]>arr[j]:
            min=j
    arr[min],arr[i]=arr[i],arr[min]
    # temp=arr[i]
    # arr[i]=arr[min]
    # arr[min]=temp

  
print(arr)


