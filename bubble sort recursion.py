arr=[5,4,2,1,3]
n=5
def rec(arr,n):
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    if n>0:
        rec(arr,n-1)
rec(arr,n)
print(arr)
# n=5
# def rec(arr,n):
#     if n==0:
#         return arr
#     else:
#         for i in range(0, n-1):
#             if arr[i]>arr[i+1]:
#                 arr[i],arr[i+1]=a[i+1],a[i]
#         return rec(arr,n-1)
# print(arr)

def bubble(arr,n):
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    if n==0:
        return 
    bubble(arr,n)
    print(arr)

