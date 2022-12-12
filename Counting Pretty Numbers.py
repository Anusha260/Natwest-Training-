Pretty=[2,3,9]
T=int(input())
for i in range(T):
    L,R=list(map(int,input().split()))
    c=0
    for j in range(L,R+1):
        if j%10 in Pretty:
            c=c+1
    print(c)
