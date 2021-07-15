# BFS Traversal with Queue


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        queue = deque([root])
        total = 0
        
        while queue:
            top = queue.popleft()
            
            if top.val >= low and top.val <= high:
                total += top.val

            if top.val > low and top.left:
                queue.append(top.left)

            if top.val < high and top.right:
                queue.append(top.right)
                    
        return total
