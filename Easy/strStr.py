# Find needle in haystack
# If needle=='' return 0; like C's strstr()
# If needle not in haystack return -1
# Else return starting index of needle in haystack

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        i, j = 0, len(haystack)
        l = len(needle)
        
        if needle == "":
            return 0
        
        while i<j:
            if haystack[i] != needle[0]:
                i += 1
            elif i+l-1 < j and haystack[i:i+l] == needle:
                return i
            else:
                i += 1
                
        return -1
