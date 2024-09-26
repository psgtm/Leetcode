# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # Helper function to calculate the height of the binary tree
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        # Helper function to fill the matrix
        def fill(res, node, r, c, height):
            if not node:
                return
            res[r][c] = str(node.val)
            # Calculate the position of the left and right children
            if node.left:
                fill(res, node.left, r + 1, c - 2**(height - r - 2), height)
            if node.right:
                fill(res, node.right, r + 1, c + 2**(height - r - 2), height)
        
        # Calculate the height of the tree
        height = getHeight(root)
        # Create the result matrix with dimensions height x (2^height - 1)
        m = height
        n = (2 ** height) - 1
        res = [["" for _ in range(n)] for _ in range(m)]
        
        # Start filling the matrix, beginning with the root in the middle of the top row
        fill(res, root, 0, (n - 1) // 2, height)
        
        return res
