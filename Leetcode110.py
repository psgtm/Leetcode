# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to check height and balance status simultaneously
        def checkHeight(node: Optional[TreeNode]) -> int:
            # An empty subtree is balanced and has height -1
            if not node:
                return 0
            
            # Check left subtree
            leftHeight = checkHeight(node.left)
            if leftHeight == -1:
                return -1  # Left subtree is not balanced
            
            # Check right subtree
            rightHeight = checkHeight(node.right)
            if rightHeight == -1:
                return -1  # Right subtree is not balanced
            
            # If the current node is unbalanced, return -1
            if abs(leftHeight - rightHeight) > 1:
                return -1
            
            # Return the height of the current node
            return max(leftHeight, rightHeight) + 1
        
        # Use the helper function to determine if the tree is balanced
        return checkHeight(root) != -1
