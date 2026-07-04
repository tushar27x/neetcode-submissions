# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None or (root.left == None and root.right == None):
            return root
        
        left_leaf = self.helper(root.left)
        right_leaf = self.helper(root.right)
        
        root.left, root.right = right_leaf, left_leaf
        
        return root
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.helper(root)
        return root        