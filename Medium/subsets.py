class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ## Cascading
        ## Time complexity - O(N x 2^N)
        
        output = [[]]
        
        for num in nums:
            
            output += [curr+[num] for curr in output]
            
        return output
