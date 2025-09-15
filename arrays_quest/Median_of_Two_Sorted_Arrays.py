'''
4. Median of Two Sorted Arrays
Hard
Topics
premium lock iconCompanies

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_lst=nums1 + nums2
        merged_lst.sort()
        if len(merged_lst) % 2 == 1:
            return merged_lst[len(merged_lst)//2]
        else:
            return (merged_lst[len(merged_lst)//2 - 1] + merged_lst[len(merged_lst)//2])/2
 
a1=[1,3]
a2=[5,4,7,9]
print(Solution().findMedianSortedArrays(a1,a2))