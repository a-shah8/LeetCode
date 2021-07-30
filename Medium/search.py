## Find start element index using binary search (minor change in binary search)
## After that find the new start and end
## And then apply binary search again

class Solution:
    
    def find_min_index(self, nums):
        start = 0
        end = len(nums)-1
        
        while start<end:
            mid = start + (end-start) // 2
            if nums[mid] > nums[end]:
                start = mid+1
            else:
                end = mid

        return start
        
    def search(self, nums: List[int], target: int) -> int:
        
        min_index = self.find_min_index(nums)
        
        if target == nums[min_index]:
            return min_index
        
        m = len(nums)
        start = min_index if (target <= nums[m-1]) else 0
        end = min_index if (target > nums[m-1]) else m-1
        
        while start<=end:
            mid = start + (end-start) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid+1
            else:
                end = mid-1
                
        return -1
