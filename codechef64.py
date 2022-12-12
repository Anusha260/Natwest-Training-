# Mario and the Broken String

T=int(input())
for i in range(T):
    N=int(input())
    for j in range(N):
        S=input()
        x=S[N//2:]
        print(x)
        y=S[:N//2]
        print(y)
        if x==y:
            print("yes")
        else:
            print("NO")
# Water Consumption

T=int(input())
for i in range(T):
    X=int(input())
    if X>=2000:
        print("YES")
    else:
        print("NO")

# Distinct Colors
T=int(input())
for i in range(T):
    N=int(input())
    A=map(int,input().split())
    a=max(A)
    print(a)

# Luigi and Uniformity

T=int(input())
while T>0:
    N=int(input())
    A=list(map(int,input().split()))
    a=min(A)
    count1=0
    for k in A:
        if k%a!=0:
            count1=1
            break
    if count1==1:
        print(N)
    else:
        print(N-A.count(a))
    T-=1
            
# 