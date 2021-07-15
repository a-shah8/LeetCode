# Iterative approach using stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        if root1 == None:
            return root2
        
        stack = []
        stack.append([root1, root2])
        
        while stack:
            node = stack.pop()
            
            # possible when tree2 node was None
            if node[0]==None or node[1]==None:
                continue
                
            node[0].val += node[1].val
            
            # merging tree2's left subtree with tree1's left subtree
            if node[0].left == None:
                node[0].left = node[1].left
                
            else:
                stack.append([node[0].left, node[1].left])
            
            # merging tree2's right subtree with tree1's right subtree
            if node[0].right == None:
                node[0].right = node[1].right
                
            else:
                stack.append([node[0].right, node[1].right])
                
        return root1
