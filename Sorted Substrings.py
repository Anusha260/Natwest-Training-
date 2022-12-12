
T=int(input())
for j in range(T):
    N=int(input())
    S=input()
    a=0
    for i in range(1,N):
        if S[i]=="0" and S[i-1]=="1":
            a=a+1
    print(a)
            