## this function retruns the indexes of the first paired matched with target 
def two_pairs_sum_index(arr,target):
    seen={}
    for i,n in enumerate(arr):
        sub=target - n
        if sub in seen:
            return [seen[sub],i]
        
        seen[n]=i

print(two_pairs_sum_index([2,6,3,9,5],9))


## this function retruns the values of the first paired matched with target 
def two_pairs_sum_values(arr,target):
    seen=[]
    for i,n in enumerate(arr):
        sub=target - n
        if sub in seen:
            return [sub,n]
        seen.append(n)

print(two_pairs_sum_values([4,5,3,9,1],9))