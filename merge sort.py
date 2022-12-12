def merge(arr):

    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge(left)
        merge(right)
        left_index=0
        right_index=0
        position=0
        while left_index<len(left) and right_index<len(right):
            if left[left_index]<right[right_index]:
                arr[position]=left[left_index]
                left_index+=1
            else:
                arr[position]=right[right_index]
                right_index+=1
                # this is  0dd numbers 
            position+=1
        while left_index<len(left):
            arr[position]=left[left_index]
            position+=1
            left_index+=1
        
