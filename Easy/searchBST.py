class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        while root:
            if val==root.val: return root
            elif val<root.val: root = root.left
            else: root = root.right
                
        return root
