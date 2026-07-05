# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        self.max_dia = max(self.max_dia, left + right)

        return max(left, right) + 1

        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0
        self.helper(root)
        return self.max_dia
        