class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix==None or len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        
        m, n = 0, len(matrix[0])-1
        
        while n>=0 and m<=len(matrix)-1:
            cur = matrix[m][n]
            if target == cur:
                return True
            elif target < cur:
                n -= 1
            elif target > cur:
                m += 1
                
        return False
