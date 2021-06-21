class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            if nums[i] > result:
                result = nums[i]
        
        return result
