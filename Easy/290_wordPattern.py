class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        ## Similar problem to Isomorphic Strings problem
        ## Approach similar to isomorphic strings - concise
        
        words = s.split()
        p_len, s_len = len(pattern), len(words)
        
        if p_len != s_len: return False
        
        map_c_w, map_w_c = {}, {}
        
        for c1, c2 in zip(pattern, words):
            
            if c1 not in map_c_w and c2 not in map_w_c:
                map_c_w[c1] = c2
                map_w_c[c2] = c1
                
            elif map_c_w.get(c1) != c2 or map_w_c.get(c2) != c1:
                return False
        
        return True
        
        ## Approach using number assignment
        
#         for i in range(p_len):
#             p = pattern[i]
#             w = words[i]
            
#             if p not in map_c_w:
#                 map_c_w[p] = i
                
#             if w not in map_w_c:
#                 map_w_c[w] = i
                
#             if map_c_w[p] != map_w_c[w]:
#                 return False
        
#         return True
    
        ## Approach similar to isomorphic strings - not concise
        
#         for i in range(p_len):
            
#             if pattern[i] not in map_c_w and words[i] not in map_w_c:
#                 map_c_w[pattern[i]] = words[i]
#                 map_w_c[words[i]] = pattern[i]
                
#             else:
#                 if map_c_w.get(pattern[i]) != words[i] or map_w_c[words[i]] != pattern[i]:
#                     return False
                
#         return True
