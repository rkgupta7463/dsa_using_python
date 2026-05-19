'''
3. Separate even and odd numbers

Input: [1,2,3,4,5,6]

Hint:
Use two pointers:

left searches odd
right searches even
Swap when needed.
'''
def sep_odd_even(arr):
    left=0
    right=len(arr)-1
    while left < right:
        while arr[left] % 2==0:
            left+=1
        while arr[right] % 2 != 0:
            right-=1

        if left < right:
            arr[left],arr[right]=arr[right],arr[left]
            left +=1
            right-=1
    return arr


arr = [1,2,3,4,5,6]
print(sep_odd_even(arr=arr))