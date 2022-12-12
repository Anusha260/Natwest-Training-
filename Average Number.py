T=int(input())
for i in range(T):
    N,K,V=map(int,input().split())
    A=list(map(int,input().split()))
    l=len(A)
    n=((V*(l+K)-sum(A))/K)
    if n>0 and n%1==0:
        print(int(n))
    else:
        print("-1")