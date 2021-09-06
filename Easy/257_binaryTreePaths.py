## Recursive solution
## Iterative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        # Recursive solution
        
        result = []
        self.dfs(root, [], result)
        return result
    
    def dfs(self, root, path, result):
        
        if root==None: return
        path.append(str(root.val))
        
        if not root.left and not root.right:
            result.append('->'.join(path))
        else:
            self.dfs(root.left, path, result)
            self.dfs(root.right, path, result)
        
        path.pop()
        
#         # Iterative solution

#         result, queue = [], deque([(root, "")])
        
#         if root==None:
#             return result
        
#         while queue:
#             root, path = queue.popleft()
            
#             if root.left:
#                 queue.append((root.left, path+str(root.val)+'->'))
#             if root.right:
#                 queue.append((root.right, path+str(root.val)+'->'))
#             if not root.left and not root.right:
#                 result.append(path+str(root.val))
                
#         return result
