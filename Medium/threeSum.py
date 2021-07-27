## Two pointer approach

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]: continue
            lo, hi = i+1, len(nums)-1
            
            while lo<hi:
                total = nums[i] + nums[lo] + nums[hi]
                
                if total == 0:
                    result.append([nums[i], nums[lo], nums[hi]])
                    while lo<hi and nums[lo]==nums[lo+1]:
                        lo += 1
                    while lo<hi and nums[hi]==nums[hi-1]:
                        hi -= 1
                        
                    lo += 1
                    hi -= 1
                    
                elif total < 0:
                    lo += 1
                else:
                    hi -= 1
                    
        return result
