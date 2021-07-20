## Iterative preorder traversal (DFS preorder) - Using stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        # ITERATIVE PREORDER USING STACK
        total = 0
        stack = [(root, 0)]
        
        while stack:
            root, cur_total = stack.pop()
            if root is not None:
                cur_total = (cur_total << 1) | root.val
                
                if root.left is None and root.right is None:
                    total += cur_total
                    
                else:
                    stack.append((root.right, cur_total))
                    stack.append((root.left, cur_total))
                    
        return total
