'''
14. Longest Common Prefix
Easy
Topics
premium lock iconCompanies

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix=strs[0]
        print("s prefix: ",prefix)
        for s in strs[1:]:
            print("s: ",s)
            while not s.startswith(prefix):
                print("prefix: ",prefix)
                prefix=prefix[:-1]
                if prefix=="":
                    return ""
        return prefix

strs =  ["dog","racecar","car"]
strs=["flower","flow","flight"]
obj=Solution()
print(obj.longestCommonPrefix(strs=strs))
