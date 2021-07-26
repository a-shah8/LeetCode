## Method 1: Iterative - stack
## Method 2: Recursive - in-built stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        
        ## Iteration
    
        nodeStack = []
        for num in nums:
            node = TreeNode(num)
            while nodeStack and num > nodeStack[-1].val:
                node.left = nodeStack.pop()
            if nodeStack:
                nodeStack[-1].right = node
            nodeStack.append(node)
        return nodeStack[0]
    
        
        ## Recursion
        
#         def max_index(nums, l, r) -> int:
#             max_i = l
#             for i in range(l, r):
#                 if nums[max_i] < nums[i]:
#                     max_i = i

#             return max_i
        
#         def construct(nums, l, r) -> TreeNode:

#             if l==r:
#                 return None

#             max_i = max_index(nums, l, r)
#             root = TreeNode(nums[max_i])
#             root.left = construct(nums, l, max_i)
#             root.right = construct(nums, max_i+1, r)

#             return root
        
#         return construct(nums, l=0, r=len(nums))
