
def Median(arr, n):
    sorted(arr)
    if n % 2 != 0:
        return arr[(n/2)]
 
    return (arr[int((n-1)/2)] +
                  arr[int(n/2)])/2.0
arr = [1, 3, 4, 2, 7, 5, 8, 6]
n = len(arr)
print(Median(arr, n))
