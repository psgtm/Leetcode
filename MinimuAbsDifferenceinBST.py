# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []

        L = inorderTraversal(root)
        diff = 0
        min_diff = float('inf')

        for i in range(len(L)-1):
            diff = abs(L[i+1] - L[i])
            
            if diff <= min_diff:
                min_diff = diff
        
        return min_diff             