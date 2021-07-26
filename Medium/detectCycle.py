## Modify Linked List
## Or Use Floyd's algorithm

## Approach - modified LinkedList and modified again to original list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        cur = head
        tmp = head
        
        if head == None or head.next == None:
            return None
        
        while cur != None:
            
            if type(cur.val) == float:
                return cur
            cur.val = float(cur.val)
            cur = cur.next
            
        while tmp != None:
            
            tmp.val = int(tmp.val)
            tmp = tmp.next
            
        return None
