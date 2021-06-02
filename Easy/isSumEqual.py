class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        first, second, third = 0, 0, 0
        
        for i in firstWord:
            first = first*10 + (ord(i)-ord('a'))
            
        for j in secondWord:
            second = second*10 + (ord(j)-ord('a'))
            
        for k in targetWord:
            third = third*10 + (ord(k)-ord('a'))
            
        return first+second==third
