"""
https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=leetcode-75
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        
        if not root: return []
        
        from collections import deque

        q = deque([root])
        values = []

        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            values.append(node.val)

        return values
        
        
        