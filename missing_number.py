def missing_number(arr, n):
    # TODO
    total_sum=n*(n+1)//2
    arr_sum=sum(arr)
    return total_sum - arr_sum

missing_number([1,2,3,4,6,7],6)