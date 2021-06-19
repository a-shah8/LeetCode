class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
#         for i in range(len(nums)):
#             nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
            
#         return [i+1 for i in range(len(nums)) if nums[i]>0]

        return set(range(1,len(nums)+1)) - set(nums)    # faster approach
