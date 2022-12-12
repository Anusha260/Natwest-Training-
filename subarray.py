
# def SubArrays(arr, start, end):
#     if end == len(arr):
#         return
#     elif start > end:
#         return SubArrays(arr, 0, end + 1)
#     else:
#         print(arr[start:end + 1])
#         return SubArrays(arr, start + 1, end)
# arr = [1, 2, 3]
# SubArrays(arr, 0, 0)
arr=[3,2,1,5,4]
def rec(arr,start,end):
    if end==len(arr):
        return
    elif start>end:
        return rec(arr,0,end+1)
    else:
        print(arr[start:end+1])
        return rec(arr,start+1,end)
rec(arr,0,0)
