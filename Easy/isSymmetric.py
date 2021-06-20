## Check if given Binary Tree is symmetric
## i.e. left subtree on one side should be same as,
## right subtree on other
## and vice versa


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        # Using iteration
        q = deque([root, root])
        
        while q:
            t1 = q.popleft()
            t2 = q.popleft()
            
            if t1==None and t2==None: continue
            if t1==None or t2==None: return False
            if t1.val != t2.val: return False
            
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
            
        return True
    
#         # Using recursion
#         return self.isMirror(root, root)
    
#     def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
#         if t1==None and t2==None: return True
#         if t1==None or t2==None: return False
#         return (t1.val==t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)
