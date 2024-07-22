# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []
        range_sum = 0
        L = inorderTraversal(root)

        for i in L:
            if i >= low and i<= high:
                range_sum+=i
        return range_sum