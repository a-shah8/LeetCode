def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merged = ''
        for i in range(min(len(word1), len(word2))):
            merged += word1[i] + word2[i]
            
        return merged+word1[len(word2):] if len(word1)>len(word2) else merged+word2[len(word1):]
