"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0

        from collections import deque

        q = deque([(1, root)])
        maxDepth = 0
        while q:
            depth, node= q.popleft()
            if node.left:
                q.append((depth+1, node.left))
            if node.right:
                q.append((depth+1, node.right))
            
            if not node.left and not node.right:
                maxDepth = max(maxDepth, depth)
        return maxDepth
        