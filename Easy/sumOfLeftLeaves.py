## Iterative - BFS using queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        if root==None: return 0
        
        ans = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left != None:
                if node.left.left==None and node.left.right==None:
                    ans += node.left.val
                else:
                    queue.append(node.left)
                    
            if node.right != None:
                if node.right.left!=None or node.right.right!=None:
                    queue.append(node.right)
                    
        return ans
