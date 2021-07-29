class Solution:
    def compress(self, chars: List[str]) -> int:
        
        ans_index = 0
        index = 0
        
        while index < len(chars):
            current = chars[index]
            count = 0
            
            while index < len(chars) and chars[index] == current:
                count += 1
                index += 1
                
            chars[ans_index] = current
            ans_index += 1
            
            if count != 1:
                for c in list(str(count)):
                    chars[ans_index] = c
                    ans_index += 1
                    
        return ans_index
