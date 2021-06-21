## Count number of 1's in input n

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        return str(bin(n)).count('1')
        
        ## Using Bit-manipulation
        # total = 0
        # while n!=0:
        #     n &= (n-1)
        #     total += 1
        # return total
