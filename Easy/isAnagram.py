class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counter_s = collections.Counter(s)
        
        for c in t:
            if c not in counter_s:
                return False
            counter_s[c] -= 1
            
        for x in counter_s.values():
            if x!=0:
                return False
        
        return True
