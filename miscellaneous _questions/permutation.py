'''
“Given two lists, L1 and L2, how can we check if L2 is a permutation of L1?
'''
## 1st way using sort inbuilt function
def check_permutation_two(l1,l2):
    if len(l1) != len(l2):
        return False
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False
    
'''
Time Complexity:

len(l1) != len(l2) → O(1)

l1.sort() → Python’s .sort() uses Timsort, which is O(n log n)

l2.sort() → also O(n log n)

l1 == l2 comparison → O(n)

✅ Total = O(n log n) + O(n log n) + O(n) = O(n log n)
'''

print(check_permutation_two(l1=[1,2,3],l2=[1,3,2]))

## 2nd way using loops inbuilt function
def check_permutation_two2(l1,l2):
    if len(l1) != len(l2):
        return False
    
    for i in range(len(l1)):
        for j in range(0, len(l1) - i - 1):
            if l1[j] > l1[j + 1]:
                temp = l1[j]
                l1[j] = l1[j + 1]
                l1[j + 1] = temp


    for i in range(len(l2)):
        for j in range(0, len(l2) - i - 1):
            if l2[j] > l2[j + 1]:
                temp = l2[j]
                l2[j] = l2[j + 1]
                l2[j + 1] = temp

    if l1 == l2:
        return True

    
'''
Time Complexity:

len(l1) != len(l2) → O(1)

Bubble sort l1 → O(n²)

Bubble sort l2 → O(n²)

l1 == l2 comparison → O(n)

✅ Total = O(n² + n² + n) = O(n²)
'''

print(check_permutation_two2(l1=['a','b','c'],l2=['c','a','b']))
