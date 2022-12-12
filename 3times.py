# T=int(input())
# for i in range (T):
#     N=list(map(int,input().split()))
#     l=set(N)
#     m=list(l)
#     n=m.sort()
#     # print(m)
    
#     if len(m)<3:
#         print("not possible")
#     else:
#         print(m[0:3])
#         print(m[-3:])
        






    

# l=[1, 3, 1, 3, 1, 2, 3]
# b={1:3,2:1,3:3,4:1}
# for i in b:
#     if b[i]==1:
#         print(i)


l=[1,2,3,4,5]
sub_array=[]
for i in range(0,len(l)):
    
    for j in range(i,len(l)):
        sub_array.append(l[i:j+1])
print(sub_array)
j=0
sum=0
c=0
while j<len(sub_array):
    if len(sub_array)>j and sum%3!=0:
        sum=sum+j


        print(sum)
        
    c=c+1
    j+=1
print(c)
c=0
for j in sub_array:
    if len(sub_array)==3:
       
        sum=sum(sub_array[j])
        if sum%3!=0:
             max=max(len[j])
        print(max)
        print(c)

        c=c+1




l=[1, 1, 1, 1 ,2, 3]
n=len(l)
c=1
for i in range(len(l)):
    if i==1:
        print(l[i])
    if n//2==0:
        c=c+1
        

    
print(c)










    
