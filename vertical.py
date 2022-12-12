arr=[[1,2,1],[2,1,2],[1,2,1]]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j]==arr[i][j-1]:
            print("horizonal")
        if arr[i][1]==arr[i][-1]:
            
            print("vertical")