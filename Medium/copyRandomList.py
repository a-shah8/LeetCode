## Editing same list and then separating at the end

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if head==None: return head
        
        # Add new nodes in old list
        c = head
        while (c!=None):
            _next = c.next
            c.next = Node(c.val)
            c.next.next = _next
            c = _next
            
        # Assign random pointers to new nodes
        c = head
        while (c!=None):
            if c.random!=None:
                c.next.random = c.random.next
            
            c = c.next.next
            
            
        # Separate both linked lists
        c = head
        copyHead = head.next
        copy = copyHead
        while (copy.next!=None):
            c.next = c.next.next
            c = c.next
            
            copy.next = copy.next.next
            copy = copy.next
            
        c.next = c.next.next
        
        return copyHead
