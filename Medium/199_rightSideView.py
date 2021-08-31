## Level Order Traversal - Using Queue
## Append only right node's value when on same level

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root==None:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                root = queue.popleft()
                
                if i==0:
                    result.append(root.val)
                if root.right:
                    queue.append(root.right)
                if root.left:
                    queue.append(root.left)
        
        return result
