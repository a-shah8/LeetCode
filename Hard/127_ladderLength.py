## Use BFS with Queue

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        word_set = set(wordList)
        queue = deque([[beginWord, 1]])
        
        while queue:
            word, seq_len = queue.popleft()
                
            if word == endWord:
                return seq_len
                
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                        
                    if next_word in word_set:
                        word_set.remove(next_word)
                        queue.append([next_word, seq_len+1])
                        
        return 0
