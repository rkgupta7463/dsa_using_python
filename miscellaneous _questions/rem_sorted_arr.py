'''
'''


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j=0
        for i in range(len(nums)):
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]
        return j+1,nums
    
obj=Solution()
nums=[0,0,1,1,1,2,2,3,3,4]#[1,1,2]
print(obj.removeDuplicates(nums=nums))    
        
