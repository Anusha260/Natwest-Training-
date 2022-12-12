# n=int(input("gjkh"))
# for i in range(n-4):
#     if n==2**i:
#         print("yes")
#         print(i)


# another way........
n=int(input("enter number"))
arr=[2]
while arr[-1]<n:
    if arr[-1]==n:
        print("yes")
        break
    else:
        arr.append(2*arr[-1])
print(arr)
    