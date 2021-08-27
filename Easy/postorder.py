## Using stack - reverse result list

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        result_list = []
        
        if root==None:
            return result_list
        
        stack = [root]
        
        while stack:
            root = stack.pop()
            result_list.append(root.val)
            
            for node in root.children:
                stack.append(node)
        
        return result_list[::-1]
