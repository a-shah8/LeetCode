## Inorder Traversal of Binary Tree
# 1. Iterative approach - Using stack
# 2. Recursive approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        # Using Iteration
        result = []
        stack = []
        cur = root
        
        while cur!=None or stack!=[]:
            
            while cur!=None:
                stack.append(cur)
                cur = cur.left
                
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
            
        return result
    
#     # Using Recursion
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         result = []
#         def helper(root):
#             nonlocal result
#             if root:
#                 helper(root.left)
#                 result.append(root.val)
#                 helper(root.right)
#         helper(root)
        
#         return result
