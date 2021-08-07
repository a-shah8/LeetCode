## Write stoi function


class Solution:
    
    def stoi(self, num: str) -> int:
        
        res = 0
        digits = {"0" : 0, "1" : 1, "2" : 2, "3" : 3,
                  "4" : 4, "5" : 5, "6" : 6, "7" : 7,
                  "8" : 8, "9" : 9}
        base = 10
        exp = 0
        
        for i in range(len(num)-1, -1, -1):
            
            digit = digits[num[i]]
            res += digit * (base ** exp)
            exp += 1
        
        return res
    
    def multiply(self, num1: str, num2: str) -> str:
    
        return str(self.stoi(num1) * self.stoi(num2))
        
        
        
#         m, n = len(num1), len(num2)
#         res = [0]*(m+n)
        
#         for i in range(m-1, -1, -1):
#             for j in range(n-1, -1, -1):
#                 mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
#                 p1, p2 = i+j, i+j+1
#                 total = mul + res[p2]
                
#                 res[p1] += total//10
#                 res[p2] = total%10
                
#         ans = ''
#         for digit in res:
            
#             if not (len(ans)==0 and digit==0):
#                 ans += str(digit)
        
#         if len(res)>0 and len(ans)==0:
#             return '0'
        
#         return '0' if len(res)==0 else ans
