class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
                
#         counter = collections.Counter(nums)
        
#         for x in counter.values():
#             if x > 1:
#                 return True
            
#         return False

        return len(nums) != len(set(nums))
