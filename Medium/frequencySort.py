## Using Bucket Sort with Dictionary

class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq_dict = {}
        
        for c in s:
            freq_dict[c] = freq_dict.get(c, 0) + 1
            
        bucket = [None]*(len(s)+1)
        
        for key in freq_dict.keys():
            freq = freq_dict[key]
            
            if bucket[freq] == None:
                bucket[freq] = []
            
            bucket[freq].append(key)
        
        new_string = ''
        for pos in range(len(bucket)-1, -1, -1):
            
            if bucket[pos] != None:
                for c in bucket[pos]:
                    for i in range(pos):
                        new_string += c
                        
        return new_string
