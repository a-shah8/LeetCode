## BFS - Using Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        
        if root is None: return True
        
        queue = deque([(root, root.val)])
        
        while queue:
            
            root, val = queue.popleft()
            if root:
                if root.left:
                    if root.left.val == val:
                        queue.append((root.left, val))
                    else:
                        return False
                if root.right:
                    if root.right.val == val:
                        queue.append((root.right, val))
                    else:
                        return False
                    
        return True
            
