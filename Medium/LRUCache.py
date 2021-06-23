## LRU cache using OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.lru_dict = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        
        if key not in self.lru_dict:
            return -1
        value = self.lru_dict.pop(key)
        self.lru_dict[key] = value
        
        return value

    def put(self, key: int, value: int) -> None:
        
        if key in self.lru_dict:
            self.lru_dict.pop(key)
        else:
            if len(self.lru_dict) == self.capacity:
                self.lru_dict.popitem(last=False)
                
        self.lru_dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
