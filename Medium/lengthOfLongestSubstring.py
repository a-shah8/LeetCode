## Using HashMap 2 pointers moving in forward direction

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_map = {}
        max_ = 0
        j = 0
        
        for i in range(len(s)):
            if s[i] in char_map:
                j = max(j, char_map.get(s[i])+1)
            char_map[s[i]] = i
            max_ = max(max_, i-j+1)
            
        return max_
