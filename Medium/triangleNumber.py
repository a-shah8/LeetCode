## Approach 1: Linear
## Approach 2: Binary Search

class Solution:
    
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        count = 0
        
        for i in range(len(nums)-1, 1, -1):
            side = nums[i]
            start, end = 0, i-1
            
            while start<end:
                if nums[start]+nums[end] > side:
                    count += (end-start)
                    end -= 1
                else:
                    start += 1
            
        return count
    
    
    ## Using Binary Search - O(n*nlogn) time complexity
    
#     def binary_search(self, nums, l, r, x):

#         while l<=r and r<len(nums):
#             mid = (l+r)//2
#             if nums[mid] >= x:
#                 r = mid-1
#             else:
#                 l = mid+1
                
#         return l
    
#     def triangleNumber(self, nums: List[int]) -> int:
#         count = 0
#         nums.sort()
        
#         for i in range(len(nums)-2):
#             k = i + 2
            
#             if nums[i] != 0:
#                 for j in range(i+1, len(nums)-1):
#                     k = self.binary_search(nums, k, len(nums)-1, nums[i]+nums[j])
#                     count += (k-j-1)
                    
#         return count
