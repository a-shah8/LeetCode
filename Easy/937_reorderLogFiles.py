## Main part of the problem is the key to be used by sorted function

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        # Time complexity - O(M*N*logN)
        # Space complexity - O(M*N)
        
        def get_key(log):
            _id, rest = log.split(' ', maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )
        
        return sorted(logs, key=get_key)
