class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        last_pos = {c:i for i,c in enumerate(s)}
        result = []
        j, start = 0, 0
        
        for i, c in enumerate(s):
            j = max(j, last_pos[c])
            
            if i==j:
                result.append(i-start+1)
                start = i+1
                
        return result
