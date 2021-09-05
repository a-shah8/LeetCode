## Approach 1: Merge with Divide and Conquer
## Approach 2: Compare 1 by 1 using Priority Queue
## Approach 3: Brute Force - using O(N) extra space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# from queue import PriorityQueue

# class Wrapper:
#     def __init__(self, first, second):
#         self._first, self._second = first, second
        
#     def __lt__(self, other):
#         return self._first < other._first

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Approach 1: Merge with Divide and Conquer
        # Time Complexity - O(Nlogk)
        # Space Complexity - O(1)
        
        num_lists = len(lists)
        skip = 1
        
        while skip < num_lists:
            for i in range(0, num_lists-skip, skip*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+skip])
            skip *= 2
                
        return lists[0] if num_lists else None
        
    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
            
        if not l1:
            point.next = l2
        else:
            point.next = l1
            
        return head.next
        
        # Approach 2: Compare 1 by 1 using Priority Queue
#         # Time Complexity - O(Nlogk)
#         # Space Complexity - O(N)
        
#         head = point = ListNode(0)
#         q = PriorityQueue()
        
#         for l in lists:
#             if l:
#                 q.put(Wrapper(l.val, l))
                
#         while not q.empty():
#             wrapper_obj = q.get()
#             val, node = wrapper_obj._first, wrapper_obj._second
#             point.next = ListNode(val)
#             point = point.next
#             node = node.next
            
#             if node:
#                 q.put(Wrapper(node.val, node))
                
#         return head.next
        
        # Approach 3: Brute Force - using O(N) extra space
#        # Time Complexity - O(NlogN) because of sorting
#        # Space Complexity - O(N), to store values in a list
        
#         self.nodes = []
#         head = point = ListNode(0)
        
#         for l in lists:
#             while l:
#                 self.nodes.append(l.val)
#                 l = l.next
                
#         for x in sorted(self.nodes):
#             point.next = ListNode(x)
#             point = point.next
            
#         return head.next
