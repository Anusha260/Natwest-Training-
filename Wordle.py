T=int(input())

for i in range(T):
    S=input()
    t=input()
    a=list(S)
    b=list(t)
    L=""
    for j in range(len(a)):
        if a[j]==b[j]:
            L=L+"G"
        else:
            L=L+"B"
    print(L)