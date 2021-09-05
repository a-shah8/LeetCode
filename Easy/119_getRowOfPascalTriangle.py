## Optimized by storing only recent row of Pascal's Triangle

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        pascal_tri = [[1]]
        
        if rowIndex == 0:
            return pascal_tri[0]
        
        while True:
            cur_level = []
            last_level_len = len(pascal_tri)
            
            for i in range(last_level_len+1):
                if i==0 or i==last_level_len:
                    cur_level.append(1)
                else:
                    cur_level.append(pascal_tri[i-1] + pascal_tri[i])
                    
            pascal_tri = cur_level
            rowIndex -= 1

            if rowIndex == 0:
                return pascal_tri
