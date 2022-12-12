# l=[39,27,11,4,24,32,32,1]
# arr=[-1]
# for i in range(1,len(l)):
#     if l[i]<l[i-1]:
#         arr.append("-1")
#     else:
#         arr.append(l[i-1])
# print(arr)
# ...........another mehod........
# T=int(input())
# for i in range(T):
#     N=int(input())
#     for j in range(N):
#         arr=[]
#         A=list(map(int,input().split()))
#         for k in range(len(A)):
#             if A[i]=="5":
#                 A[i].remove("5")
#         print(arr)

T=int(input())
for i in range(T):
    N=int(input())
    for j in range(N):
        arr=[]
        A=list(map(int,input().split()))
        for k in range(len(A)):
            if A[i]=="5":
                arr.remove(A[i])
            elif A[i]=="3":
                arr.remove(A[i])
        print(arr)
            
                

