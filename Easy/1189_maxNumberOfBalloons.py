class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        freq_in_text = [0]*26
        freq_in_pattern = [0]*26
        answer = math.inf
        
        for c in text:
            freq_in_text[ord(c)-ord('a')] += 1
        
        # replace 'balloon' with pattern
        # for more generalized solution
        for c in 'balloon':
            freq_in_pattern[ord(c)-ord('a')] += 1
            
        print(freq_in_text, freq_in_pattern)
        for i in range(26):
            
            if freq_in_pattern[i] > 0:
                answer = min(answer, freq_in_text[i]//freq_in_pattern[i])
                
        return answer
