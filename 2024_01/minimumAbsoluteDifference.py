"""
530. Minimum Absolute Difference in BST
Easy

4244

213

Add to List

Share
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1

"""


class Solution:
    def getMinimumDifference(self, root) -> int:
        
        minDiff = float("inf")
        prev = None
        
        def inorder(node):
            nonlocal minDiff, prev
            if not node:
                return
            inorder(node.left)
            if prev:
                minDiff = min(minDiff, node.val - prev.val)
            prev = node
            inorder(node.right)
        inorder(root)
        return minDiff