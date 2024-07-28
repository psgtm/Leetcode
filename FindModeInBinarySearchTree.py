# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right) if root else []
        
        L = inorderTraversal(root)
        counter = Counter(L)
        max_count = max(counter.values())
        mode = [k for k, v in counter.items() if v == max_count]
        return mode