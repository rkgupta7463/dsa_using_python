'''
Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

    Input: nums = [1,2,3,1]
    Output: true

Hint: Use sets
'''
def least_contains_duplicate(nums):
    # TODO
    seen=[]
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.append(nums[i])
    return False

nums = [1,1,2,3,9]
print(least_contains_duplicate(nums))

'''
Contains Duplicate

Given an integer array nums, return true if any value appears at last twice in the array, and return false if every element is distinct.

Example :

    Input: nums = [1,2,3,1]
    Output: true

Hint: Use sets
'''

def contains_duplicate_last(nums):
    # TODO
    seen=[]
    for i in range(len(nums)-1):
        if nums[i] == nums[-1]:
            return True
    return False


nums = [1,2,3,1]
print(contains_duplicate_last(nums))
