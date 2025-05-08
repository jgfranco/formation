"""
https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        
        """
        pseudocode
        
        Recursive function that takes into consideration a path up until the current node
        and also start a new path from the current node
        rec call -> sumSoFar path
        rec call -> new Path from current node
        """

        self.targetSumPaths = 0
        from collections import deque

        def count(node, currentSum = 0):

            if not node: return 0

            currentSum += node.val

            if currentSum == targetSum:
                self.targetSumPaths += 1

            count(node.left, currentSum)
            count(node.right, currentSum)

        q = deque([root])

        while q:
            node = q.popleft()
            count(node)
            if node:
                q.append(node.left)
                q.append(node.right)

        return self.targetSumPaths


        