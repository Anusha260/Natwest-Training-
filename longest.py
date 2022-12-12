l=[1,2,1,3,4,5]

# sub_array=[]
# for i in range(0,len(l)):
    
#     for j in range(i,len(l)):
#         sub_array.append(l[i:j+1])
        

# print(sub_array)
# d={}
# for k in range(len(0,sub_array)):
#     for m in range(len(1,sub_array)):
#         d[k]=sub_array[m]
# print(d)
arr=[1,2,3,4,5,6]
n=6
max_length=0
obj={}
for i in range(1,n+1):
    obj[(str(i))]=[]
for i in range(0,n):
    for j in range(i,n):
        a=arr[i:j+1]
        obj[str(len(a))].append(a)
print(obj)
