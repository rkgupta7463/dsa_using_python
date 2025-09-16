'''
1. Trapping Rain Water

Question: Given n non-negative integers representing elevation map, compute how much water it can trap after raining.

Input: [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6

Hint: Use two pointers tracking left_max and right_max. Water = min(left_max, right_max) - height[i].
'''

def solution(height:list[int]):
    ...