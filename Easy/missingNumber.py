class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # Using Gauss' Formula
        n = len(nums)
        missing = n*(n+1)//2
        
        for i in nums:
            missing -= i
        return missing
        
#         # Using Bit-manipulation
#         missing = len(nums)
        
#         for i, num in enumerate(nums):
#             missing ^= i ^ num
#         return missing
