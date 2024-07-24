# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []

        L = inorderTraversal(root)

        return all(x == L[0] for x in L)