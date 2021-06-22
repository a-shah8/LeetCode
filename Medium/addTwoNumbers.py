## Inputs are given as LinkedList
## Result is returned as a LinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = ListNode()
        head = result
        carry = 0
        
        while l1 != None or l2 != None:
            
            x = l1.val if l1!=None else 0
            y = l2.val if l2!=None else 0
            
            total = carry + x + y
            carry = total//10
            head.next = ListNode(total%10)
            head = head.next
            
            if l1!=None: l1 = l1.next
            if l2!=None: l2 = l2.next
                
        if carry>0:
            head.next = ListNode(carry)
            
        return result.next
