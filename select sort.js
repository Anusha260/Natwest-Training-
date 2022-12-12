arr=[5,4,3,2,1]
for(i=0;i<arr.length;i++){
    min=i
    for (j=i+1;j<arr.length;j++){
        if(arr[min]>arr[j]){
            min=j
    // arr[min],arr[i]=arr[i],arr[min]
        }
    arr[min],arr[i]=arr[i],arr[min]
    }
}
console.log(arr)