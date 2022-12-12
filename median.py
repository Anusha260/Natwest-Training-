# a=[2,6,5,5,7,6,1,6]
# a.sort()
# print(a)
# num=len(a)
# # print(num)
# # c=(num)//2
# for i in a:
#     c=(num+1)//2
#     print(c)
#     if c%2==0:
#         d=(a[c]+a[c+1])/2
#         print(a[c])
      

#     else:
#         e=a[c]
#         print(e)


def Median(a, n):
    sorted(a)
    if n % 2 != 0:
        return a[(n/2)]
 
    return (a[int((n-1)/2)] +
                  a[int(n/2)])/2.0
a = [1, 3, 4, 2, 7, 5, 8, 6]
n = len(a)
print(Median(a, n))


