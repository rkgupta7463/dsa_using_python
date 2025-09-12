'''
Max Product of Two Integers

Find the maximum product of two integers in an array where all elements are positive.

Example

    arr = [1, 7, 3, 4, 9, 5] 
    max_product(arr) # Output: 63 (9*7)
'''
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