class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        maximum = -inf
        s_max, t_max = -inf, -inf
        
        for i in range(len(nums)):
            
            if nums[i] > maximum:
                t_max = s_max
                s_max = maximum
                maximum = nums[i]
                
            elif nums[i] < maximum and nums[i] > s_max:
                t_max = s_max
                s_max = nums[i]
                
            elif nums[i] < s_max and nums[i] > t_max:
                t_max = nums[i]
            
        return t_max if t_max!=-inf else maximum
