# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if root==None:
            return 0
        
        # Using level-order traversal
        queue = [root]
        min_depth = 0
        
        while queue:
            
            cur_level = []
            
            for i in range(len(queue)):
                node = queue.pop()
                
                if not (node.left or node.right):
                    min_depth += 1
                    return min_depth
                
                if node.left:
                    cur_level.append(node.left)
                
                if node.right:
                    cur_level.append(node.right)
                
            min_depth += 1
            queue = cur_level
