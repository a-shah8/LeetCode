class Solution:
    def countPrimes(self, n: int) -> int:
        
        is_prime = [True]*n
        
        for i in range(2, int(n**0.5)+1):
            
            if not is_prime[i]:
                continue
            for j in range(i**2, n, i):
                is_prime[j] = False
                
        count = 0
        
        for i in range(2, n):
            if is_prime[i]:
                count += 1
                
        return count
