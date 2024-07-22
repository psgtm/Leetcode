# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        self.total_tilt = 0

        def tilt(node):
            if node is None:
                return 0
            
            left_sum = tilt(node.left)
            right_sum = tilt(node.right)

            current_tilt = abs(left_sum - right_sum)

            self.total_tilt += current_tilt

            return node.val + left_sum + right_sum
        
        tilt(root)
        return self.total_tilt