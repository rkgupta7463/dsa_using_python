def second_largest(nums):
    unique_nums = list(set(nums))
    print(unique_nums)
    unique_nums.sort()
    return unique_nums[-2]

print(second_largest([5, 1, 3, 9, 9, 7]))
