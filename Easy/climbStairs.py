class Solution:
    def climbStairs(self, n: int) -> int:
       
        ## Fibonacci series - space efficient
        if n==1:
            return 1
        
        first, second = 1, 2
        for i in range(3,n+1):
            third = first+second
            first, second = second, third
            
        return second
        
#         ## Dynamic Programming   
#         if n==1:
#             return 1
        
#         # dp[0]=0 is not needed,
#         # but for correct indexing it is there
#         dp = [0, 1, 2]
        
#         for i in range(3,n+1):
#             dp.append(dp[i-1]+dp[i-2])
            
#         return dp[n]
