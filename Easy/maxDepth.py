## Maximum Depth of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        # Using iterative approach - BFS
        
        if not root: return 0
        
        nodes_in_current_level = 1
        nodes_in_next_level = 0
        ans = 0
        q = deque([root])
        
        while q:
            top = q.popleft()
            if top.left: 
                q.append(top.left)
                nodes_in_next_level += 1
            if top.right: 
                q.append(top.right)
                nodes_in_next_level += 1
            nodes_in_current_level -= 1
            if nodes_in_current_level == 0:
                nodes_in_current_level = nodes_in_next_level
                nodes_in_next_level = 0
                ans += 1
        return ans
    
#        # Using Recursion - DFS
#         if root == None:
#             return 0
        
#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)
        
#         return max(left, right) + 1        
