class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Divide and Conquer approach
        left, right = 0, len(nums)-1
        index = 0
        
        while left<right:
            mid = left + (right-left)//2
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
                index = mid
            else:
                left = mid+1
                index = mid+1
                
        if target <= nums[index]:
            return index
        else:
            return index+1
        
        # index = 0
        # for i in range(len(nums)):
        #     if(target <= nums[i]):
        #         index = i
        #         break
        #     else:
        #         if(i == len(nums) - 1):
        #             index = i + 1
        # return index
