class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        b_dict = {')':'(', '}':'{', ']':'['}
        
        for b in s:
            if b not in b_dict:
                stack.append(b)
            
            elif stack == [] or stack.pop() != b_dict[b]:
                    return False
                    
        return stack==[]
