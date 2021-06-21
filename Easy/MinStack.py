## Designing MinStack
## 1. Using Linked List
## 2. Using Arrays/Lists
class MinStack:

    head = None
    
    def __init__(self):
        """
        initialize your data structure here.
        """

    def push(self, x: int) -> None:
        if self.head==None:
            self.head = self.Node(x, x, None)
        else:
            self.head = self.Node(x, min(self.head.min_val, x), self.head)

    def pop(self) -> None:
        self.head = self.head.next_node

    def top(self) -> int:
        return self.head.value

    def getMin(self) -> int:
        return self.head.min_val
    
    class Node:
        
        value = None
        min_val = None
        next_node = None
        
        def __init__(self, value, min_val, next_node):
            self.value = value
            self.min_val = min_val
            self.next_node = next_node
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
