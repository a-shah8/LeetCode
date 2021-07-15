## Inorder Traversal - recursion
## Creating new in-order increasing BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        def inorder(node):
            if node:
                # traverse left subtree
                inorder(node.left)
                node.left = None
                # add node to right of new_tree
                self.cur.right = node
                self.cur = node
                # traverse left subtree
                inorder(node.right)
                
        new_tree = self.cur = TreeNode(None)
        inorder(root)
        
        return new_tree.right
