'''
Duplicate Number

Write a function to remove the duplicate numbers on given integer array/list.

Example

    remove_duplicates([1, 1, 2, 2, 3, 4, 5])
    Output : [1, 2, 3, 4, 5]
'''
#### 1st way of removing duplicate

def remove_duplicates(arr):
    # TODO
    return list(set(arr))


#### 2nd way of removing duplicate
def remove_duplicates2(arr):
    seen=[]
    for i in arr:
        if i not in seen:
            seen.append(i)
    return seen

r1=remove_duplicates([1, 1, 2, 2, 3, 4, 5])
r2=remove_duplicates2([1, 1, 2, 2, 3, 4, 5])

print("1st, Result:- ",r1)
print("2nd, Result:- ",r2)