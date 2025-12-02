def second_largest(nums):
    unique_nums = list(set(nums))
    # print(unique_nums)
    unique_nums.sort()
    return unique_nums[-2]

print(second_largest([5, 1, 3, 9, 9, 7]))

def second_largest_2n(nums):
    nums = list(set(nums))   
    if len(nums) < 2:
        return None          

    first = second = float('-inf')

    for n in nums:
        if n > first:
            second = first
            first = n
        elif n > second and n != first:
            second = n

    return second

print(second_largest_2n([5, 1, 3, 9, 9, 7,8]))

