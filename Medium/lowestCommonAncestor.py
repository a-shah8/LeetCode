## Using recursion
## Time Complexity - O(N), Space Complexity - O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = None
        
        def recurse_tree(current_node):
            
            nonlocal ans
            
            if not current_node:
                return False
            
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            
            mid = current_node==p or current_node==q
            
            if mid+left+right >= 2:
                ans = current_node
                
            return mid or left or right
        
        recurse_tree(root)
        return ans
