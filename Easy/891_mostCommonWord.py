## Solution 1: One-pass approach
## Solution 2: Multi-pass approach - String Manipulation

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # Time and Space Complexity - O(N + M)
        
        # One-pass approach
        answer = ''
        max_count = 0
        word_buffer = []
        word_count = defaultdict(int)
        banned_words = set(banned)
        
        for p, char in enumerate(paragraph):
            
            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph)-1:
                    continue
                    
            if len(word_buffer) > 0:
                word = ''.join(word_buffer)
                if word not in banned_words:
                    word_count[word] += 1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        answer = word
                
                word_buffer = []
                
        return answer
        
        
#         # Time and Space Complexity - O(N + M)
        
#         new_para = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        
#         words = new_para.split()
        
#         word_count = defaultdict(int)
#         banned_words = set(banned)
        
#         for word in words:
#             if word not in banned_words:
#                 word_count[word] += 1
                
#         return max(word_count.items(), key=operator.itemgetter(1))[0]
