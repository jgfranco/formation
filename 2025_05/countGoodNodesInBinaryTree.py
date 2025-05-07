"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/1628091587/?envType=study-plan-v2&envId=leetcode-75
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        from collections import deque

        q = deque([(float("-inf"), root)])
        goodNodes = 0

        while q:
            maxValue, node = q.popleft()
            
            if node.val >= maxValue:
                maxValue = node.val
                goodNodes += 1
            
            if node.left:
                q.append((maxValue, node.left)) 

            if node.right:
                q.append((maxValue, node.right))

        
        return goodNodes