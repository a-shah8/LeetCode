class Solution:
    def maxDepth(self, s: str) -> int:
        
        max_depth = 0
        count = 0
        
        for c in s:
            if c=='(':
                count += 1
                max_depth = max(max_depth, count)
                
            elif c==')': 
                count -= 1
             
        return max_depth
