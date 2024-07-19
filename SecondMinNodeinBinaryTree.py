# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []
        
        L = inorderTraversal(root)
        M = []
        L = sorted(L)
        L_min = min(L)

        for i in L:
            if i!=L_min:
                M.append(i)
        return min(M) if M else -1