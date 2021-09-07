class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]
        
        nums.sort()
        size = 0
        for i in range(len(nums)):
            j = size if i > 0 and (nums[i] == nums[i-1]) else 0
            size = len(output)
            while j < size:
                temp = copy.copy(output[j])
                temp.append(nums[i])
                output.append(temp)
                j += 1  
                
        return output
