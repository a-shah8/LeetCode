# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None:
            return None
        
        cur = point = head
        
        while point:
            
            while point.next != None and point.val == point.next.val:
                point = point.next
            point = point.next
            cur.next = point
            cur = cur.next
            
        return head
