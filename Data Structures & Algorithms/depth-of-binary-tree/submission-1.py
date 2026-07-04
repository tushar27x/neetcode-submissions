# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode], depth: int) -> int :
        if root == None: 
            return 0
        
        left_depth = self.helper(root.left, depth) + 1
        right_depth = self.helper(root.right, depth) + 1



        return max(left_depth, right_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)        