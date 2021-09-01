## Not a fast approach - but might be useful during interviews

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [self.Node()]*10000
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = self.idx(key)
        
        if self.data[i]==None:
            self.data[i] = self.Node()
        node = self.find(self.data[i], key)
        if node.next==None:
            node.next = self.Node(key, value)
        else:
            node.next.val = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = self.idx(key)
        
        if self.data[i]==None:
            return -1
        
        node = self.find(self.data[i], key)
        return node.next.val if node.next else -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = self.idx(key)
        
        if self.data[i]==None:
            return
        prev = self.find(self.data[i], key)
        if prev.next==None:
            return
        prev.next = prev.next.next
        
    def find(self, bucket, key):
        node = bucket
        prev = None
        
        while (node!=None and node.key!=key):
            prev = node
            node = node.next
            
        return prev
    
    def idx(self, key):
        return key % len(self.data)        
        
    class Node:
        
        def __init__(self, key=-1, value=-1, next=None):
            self.key = key
            self.val = value
            self.next = next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
