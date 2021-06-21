class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        prev1, prev2 = 0, 0
        for n in nums:
            prev1, prev2 = max(prev2+n, prev1), prev1
            
        return prev1
