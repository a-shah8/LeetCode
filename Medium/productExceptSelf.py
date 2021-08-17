class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [0]*len(nums)
        result[0] = 1
        
        for i in range(1, len(nums)):
            result[i] = result[i-1]*nums[i-1]
            
        reverse = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= reverse
            reverse *= nums[i]
            
        return result
