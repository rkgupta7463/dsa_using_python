'''
9. Palindrome Number
Given an integer x, return true if x is a

, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num=x
        rev=0
        while  num > 0:
            rem=num%10
            rev=rev*10+rem
            num=num//10

        if rev==x:
            return True
        else:
            return False

print(Solution().isPalindrome(-121))