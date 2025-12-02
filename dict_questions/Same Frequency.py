'''
Same Frequency

Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:

    list1 = [1, 2, 3, 2, 1]
    list2 = [3, 1, 2, 1, 3]
    check_same_frequency(list1, list2)

Output:

False 
'''

### 1st way
def check_same_frequency(list1, list2):
    # TODO
    seen=set(list1)
    for l in list2:
        if l in seen:
            return False



list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 2]
# print(check_same_frequency(list1, list2))

### 2nd way with decorator
def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
    
    return count_elements(list1) == count_elements(list2)

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 2]
print(check_same_frequency(list1, list2))