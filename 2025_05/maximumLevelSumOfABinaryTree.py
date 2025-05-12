"""
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        if not root: return None

        level = 1
        from collections import deque
        q = deque([root])
    
        maxLevelSum = float("-inf")
        maxLevel = 1

        while q:
            size = len(q)
            levelSum = 0

            for _ in range(size):
                node = q.popleft()
                levelSum += node.val

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            if levelSum > maxLevelSum:
                maxLevelSum = levelSum
                maxLevel = level

            level += 1
            
        return maxLevel
            
        