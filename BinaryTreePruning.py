# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Helper function to prune the tree
        def prune(node: TreeNode) -> Optional[TreeNode]:
            if not node:
                return None
            
            # Recursively prune the left and right subtrees
            node.left = prune(node.left)
            node.right = prune(node.right)
            
            # If the current node is a leaf node and its value is 0, prune it
            if node.val == 0 and not node.left and not node.right:
                return None
            
            return node
        
        # Start pruning from the root
        return prune(root)

        