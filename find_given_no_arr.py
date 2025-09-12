'''
Write a program, to return the that number which is euqal to given number
Eg. [1,2,3,4,5,6] , n=5 , output:- 4 (index) 
'''

import array as arr

def find_number(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return f"Number present at {i} index"

print(find_number(arr.array('i',[1,2,4,5,7,8,9,12]),4) )
