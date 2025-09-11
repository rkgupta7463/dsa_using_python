def max_product(arr):
    # TODO
    max1,max2=0,0
    
    for i in range(len(arr)):
        if arr[i] > max1:
            max2=max1
            max1=arr[i]
        elif arr[i] > max2:
            max2 = arr[i]
    return max1*max2

print((max_product([1, 7, 3, 4, 9, 5])))