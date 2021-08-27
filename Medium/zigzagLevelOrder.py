# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result_list = []
        
        if root==None:
            return result_list
        
        queue = deque([root])
        zigzag = True
        
        while queue:
            size = len(queue)
            cur_level = [0]*size
            
            for i in range(size):
                root = queue.popleft()
                pos = i if zigzag else size-i-1
                
                cur_level[pos] = root.val
            
                if root.left:
                    queue.append(root.left)
                    
                if root.right:
                    queue.append(root.right)
                    
            zigzag = not zigzag
            result_list.append(cur_level)
            
        return result_list
