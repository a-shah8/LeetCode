class Solution:
    def toLowerCase(self, s: str) -> str:
        
        # Map uppercase alphabet to lowecase alphabet
        hash_map = dict(zip(string.ascii_uppercase, string.ascii_lowercase))
        
        return ''.join(hash_map[c] if c in hash_map else c for c in s)
        
       # Hard-coding ascii values
#         new_string = ''
#         for c in s:
#             if ord(c) < 97 and ord(c) > 64:
#                 new_string += chr(ord(c)+32)
#             else:
#                 new_string += c
            
#         return new_string
