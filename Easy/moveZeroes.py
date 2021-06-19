# Move zeroes to end

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        length = len(nums)
        
        for i in range(length):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
                
        for x in range(j, length):
            nums[x] = 0
