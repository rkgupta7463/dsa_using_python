'''
write the program of find all pairs of integers whose sum is equal to a given number.
Eg:- [2,6,3,9,11], output :- [6,3] 
'''

## this function retruns the indexes of the first paired matched with target 
def two_pairs_sum_index(arr,target):
    seen={}
    for i,n in enumerate(arr):
        sub=target - n
        if sub in seen:
            return [seen[sub],i]
        
        seen[n]=i

print(two_pairs_sum_index([2,6,3,9,5],9))

'''
write the program of find all pairs of integers whose sum is equal to a given number.
Eg:- [2,6,3,9,11], output :- [1,2] -> indexes of those value whose sum of pairs is. 
'''

## this function retruns the values of the first paired matched with target 
def two_pairs_sum_values(arr,target):
    seen=[]
    for n in arr:
        sub=target - n
        if sub in seen:
            return [sub,n]
        seen.append(n)

print(two_pairs_sum_values([4,5,3,9,1],9))