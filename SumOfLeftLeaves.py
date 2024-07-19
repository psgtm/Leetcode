# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dsum(root):
            s = 0
            if root is None:
                return 0
            if root.left and isLeaf(root.left):
                s += root.left.val
            return s + dsum(root.left) + dsum(root.right)


        def isLeaf(root):
            if root.left is None and root.right is None:
                return True
        
        return dsum(root)