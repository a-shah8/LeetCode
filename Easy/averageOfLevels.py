## Using queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        result = []
        if root==None:
            return result
        
        queue = deque([root])
        
        while queue:
            size = len(queue)
            level_total = 0
            
            for i in range(size):
                current = queue.popleft()
                level_total += current.val
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                    
            result.append(level_total/size)
            
        return result
