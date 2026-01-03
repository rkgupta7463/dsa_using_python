'''
21. Merge Two Sorted Lists
Easy
Topics
premium lock iconCompanies

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''
## solution.1
class Solution:
    def mergeTwoLists(self, list1, list2) -> list:
        new_lst=list1+list2
        return sorted(new_lst)

obj=Solution()
list1 = [1,2,4]
list2 = [1,3,4]
print(obj.mergeTwoLists(list1=list1,list2=list2))        

## solution.2
class Solution:
    def mergeTwoLists(self, list1, list2) -> list:
        i,j=0,0
        sorted_lst=[]

        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                sorted_lst.append(list1[i])
                i+=1
            else:
                sorted_lst.append(list2[j])
                j+=1 

        sorted_lst.extend(list1[i:]) 
        sorted_lst.extend(list2[j:]) 

        return sorted_lst

obj=Solution()
print(obj.mergeTwoLists(list1=list1,list2=list2))        

## solution.3
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            print("lst1: ",list1)
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach remaining nodes
        current.next = list1 if list1 else list2

        return dummy.next

obj=Solution()
list1 = [1,2,4]
list2 = [1,3,4]
print(obj.mergeTwoLists(list1=list1,list2=list2))        