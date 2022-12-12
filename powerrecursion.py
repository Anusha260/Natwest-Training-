def rec(x,n):
    if(n==0):
        return 1
    else:
        return x*rec(x,n-1)
print(rec(2,6))