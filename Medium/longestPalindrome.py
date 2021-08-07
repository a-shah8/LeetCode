class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s==None or len(s)<1: return ''
        
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s,i,i)
            len2 = self.expandAroundCenter(s,i,i+1)
            max_len = max(len1, len2)
            
            if max_len > (end-start):
                start = i - (max_len-1)//2
                end = i + max_len//2
                
        return s[start:end+1]
    
    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        l, r = left, right
        
        while (l>=0 and r<len(s) and s[l]==s[r]):
            l -= 1
            r += 1
            
        return r - l - 1
