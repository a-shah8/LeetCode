## Generate Pascal's Triangle upto numRows rows

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows==0:
            return 0
        
        pascal_tri = [[1]]
        
        for i in range(2,numRows+1):
            cur_level_nums = []
            last_level_len = len(pascal_tri[-1])
            for j in range(last_level_len+1):
                if j==0 or j==last_level_len:
                    cur_level_nums.append(1)
                else:
                    cur_level_nums.append(pascal_tri[-1][j-1]+pascal_tri[-1][j])
            pascal_tri.append(cur_level_nums)
                    
        return pascal_tri
