arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n=4
result=[]
top=0
side=0
columns=n
rows=n
while side<columns and top<rows:
    for i in range(side,columns):
        result.append(arr[rows-1][i])
    rows-=1
    for j in range(rows-1,top-1,-1):
        result.append(arr[j][rows])
    columns-=1
    for k in range(columns-1,side-1,-1):
        result.append(arr[top][k])
    top+=1
    for m in range(top,rows):
        result.append(arr[m][side])
    side+=1
print(*result,sep=" ")