# def sum(a):
#     if a==1:
#         return 1
#     else:
#         return a+sum(a-1)
        
# print(sum(5))

# ..............

def rec(arr):
    if len(arr)==0:
        return 0
    else:
        return arr[0]+rec(arr[1:len(arr)])
arr=[1,2,3,4,5]
print(rec(arr))

