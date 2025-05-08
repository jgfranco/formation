


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        
        self.longestZigZag = 0
        def zigzaging(node, left, right):
            self.longestZigZag = max(self.longestZigZag, left, right)

            if node.left:
                zigzaging(node.left, right+1, 0)
            
            if node.right:
                zigzaging(node.right, 0, left +1)

        zigzaging(root, 0, 0)
        return self.longestZigZag