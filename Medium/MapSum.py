## Using Trie

class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta
        

    def sum(self, prefix: str) -> int:
        cur = self.root
        
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
            
        return cur.score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
