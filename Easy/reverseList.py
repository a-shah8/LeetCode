# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        ## Iterative - O(1) space complexity
        prev = None
        cur = head
        
        while cur:
            tmp_ll = cur.next
            cur.next = prev
            prev = cur
            cur = tmp_ll
            
        return prev
    
        ## Iterative - O(n) space complexity
#         stack = []
        
#         while head:
#             stack.append(head.val)
#             head = head.next
        
#         if stack == []: return None
        
#         head = ListNode(stack.pop())
#         cur = head
#         while stack:
#             node = ListNode(stack.pop())
#             cur.next = node
#             cur = cur.next
            
#         return head
