## Using dictionary and heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        freq = collections.Counter(words)
        
        return heapq.nsmallest(k, 
            freq, key=lambda word:(~freq[word], word)
        )
