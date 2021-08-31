class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        area = 0
        left, right = 0, len(height)-1
        
        while left<right:
                
            if height[left]<height[right]:
                new_area = height[left]*(right-left)
                left += 1
            else:
                new_area = height[right]*(right-left)
                right -= 1
                
            area = max(area, new_area)
        return area
