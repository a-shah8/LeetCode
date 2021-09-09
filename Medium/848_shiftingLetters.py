class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
       
        total_shifts = 0
        new_s = [0]*len(s)
        
        for i in range(len(s)-1, -1, -1):
            
            total_shifts += shifts[i]
            new_s[i] = chr(((ord(s[i])-97 + total_shifts) % 26) + 97)
            
        return ''.join(new_s)
