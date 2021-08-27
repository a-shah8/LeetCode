## Using queue - Iterative

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root==None:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                current = queue.popleft()
                for child in current.children:
                    queue.append(child)
                    
            depth += 1
            
        return depth
