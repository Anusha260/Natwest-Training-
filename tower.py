# a=[100,80,70,60,50,80]
# l=[]
# for k in range(len(a)-1,0,-1):
#     c=1
#     for j in range(k,-1,-1):
#         if a[k]>a[j]:
#             c+=1
#         elif a[j]>a[k]:
            

def rec(a):
    
    if a>=1:
        return a
    else:
        return rec(a-1)
print(rec(6))


