class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        unique_nums = {}
        total = 0
        
        for n in nums:
            if n not in unique_nums:
                unique_nums[n] = True
                total += n
            elif unique_nums[n]:
                total -= n
                unique_nums[n] = False
                
        return total
