arr=[1,4,3,2,3,2,1,7]
new_list=[]
for i in arr:
    if i not in new_list:
        new_list.append(i)
print(new_list)
