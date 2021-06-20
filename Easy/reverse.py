class Solution:
    def reverse(self, x: int) -> int:
        
        result = 0
        num = abs(x)
        while num != 0:
            result = (result*10) + (num%10)
            num //= 10
        
        if x<0 and (result*-1 > -1*(2**31)):
            return -1*result
        if x>0 and result < (2**31 - 1):
            return result
            
        return 0
