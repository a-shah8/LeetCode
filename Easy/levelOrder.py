## Binary Tree Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []
        
        q = deque([root])
        result = []
        
        while q:
            
            cur_level = []
            for _ in range(len(q)):
                child = q.popleft()
                if child.left:
                    q.append(child.left)
                if child.right:
                    q.append(child.right)
                cur_level.append(child.val)
                
            result.append(cur_level)
            
        return result
