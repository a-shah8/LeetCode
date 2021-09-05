class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        
        for j in range(1, len(nums)):
            # Copy only if elements are different
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
        return i+1
