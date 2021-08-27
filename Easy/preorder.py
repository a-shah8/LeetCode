## Using stack

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        result_list = []
        
        if root==None: return result_list
        
        stack = [root]
        
        while stack:
            root = stack.pop()
            result_list.append(root.val)
            
            for i in range(len(root.children)-1, -1, -1):
                stack.append(root.children[i])
                
        return result_list
