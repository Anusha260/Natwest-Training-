T=int(input())
for i in range(T):
    N=int(input())
    L=input().split()
    c1=0
    c2=0
    for N in L:
        if N=="START38":
            c1=c1+1
        elif N=="LTIME108":
            c2=c2+1
    print(c1,c2)