arr=[5,4,2,3,1]
# for i in range(0,len(arr)):
#     for j in range(0,len(arr)-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]

# print(arr)
# another way....

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)-1):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)

