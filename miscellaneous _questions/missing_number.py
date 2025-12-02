'''
Missing Number

Write a function to find the missing number in a given integer array of 1 to 100. The function takes to parameter the array and the number of elements that needs to be in array.  For example if we want to find missing number from 1 to 6 the second parameter will be 6.

Example

    missing_number([1, 2, 3, 4, 6,7], 6) # 5
'''
def missing_number(arr, n):
    # TODO
    m=n+1
    total_sum=m*(m+1)//2
    arr_sum=sum(arr)
    return total_sum - arr_sum

print(missing_number([1, 2, 3,4, 6],5))