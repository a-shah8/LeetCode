## Using recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_path = float("-inf")
        
        def get_max_path(node):
            nonlocal max_path
            
            if node==None:
                return 0
            
            left_gain = max(get_max_path(node.left), 0)
            right_gain = max(get_max_path(node.right), 0)
            
            cur_max_path = node.val + left_gain + right_gain
            max_path = max(max_path, cur_max_path)
            
            return node.val + max(left_gain, right_gain)
        
        get_max_path(root)

