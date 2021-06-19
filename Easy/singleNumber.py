# All numbers in nums are repeated, expect for one.
# Find the single number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        a = 0
        for i in nums:
            a ^= i
        return a
