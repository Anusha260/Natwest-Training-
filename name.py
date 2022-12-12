
# result=[]
# def name(arr,result):

#     if arr[0]=="anu":
#         return " "
#     else:
#         result.append(arr[0])
#         return name(arr[1:],result)

# arr=["sristi","bhavya","anu","sukku"]
# print(name(arr,result))
# print(result)

# T=int(input())
# for i in range(T):
    # N=int(input())
    # for j in range(N):
    #     S=input()
    #     x=S[N//2:]
    #     print(x)
    #     y=S[:N//2]
    #     print(y)
    #     if x==y:
    #         print("yes")
    #     else:
    #         print("NO")
T=int(input())
for i in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    a=A.sort()
    c=0
    for j in range(A):
        if A[i]==a:
            print(c)
