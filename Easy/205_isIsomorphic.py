## Using 2 dictionaries
## 1 to map from s to t
## another to map from t to s

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map_s_t = {}
        map_t_s = {}
        
        for c1, c2 in zip(s, t):
            
            if c1 not in map_s_t and c2 not in map_t_s:
                map_s_t[c1] = c2
                map_t_s[c2] = c1
                
            elif map_s_t.get(c1) != c2 or map_t_s.get(c2) != c1:
                return False
        
        return True

        # Easier approach - maybe not be accepted during interviews
        # return len(set(zip(s, t))) == len(set(s)) == len(set(t))
