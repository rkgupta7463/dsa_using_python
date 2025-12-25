class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0

        for i in range(left,right):
            ##with
            w=right-left

            ## height 
            h=min(height[left],height[right])

            area=w*h

            ## update the max area
            max_area=max(max_area,area)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1

        return max_area


print(Solution().maxArea(height=[1,2,1]))