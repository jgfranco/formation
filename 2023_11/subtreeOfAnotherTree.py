"""
572. Subtree of Another Tree
Easy

7848

457

Add to List

Share
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        
        def compareTrees(rootSubRoot, subRoot):
            if not rootSubRoot and not subRoot: return True
            elif not rootSubRoot or not subRoot: return False
            
            if rootSubRoot.val != subRoot.val: return False
            
            return compareTrees(rootSubRoot.left, subRoot.left) and compareTrees(rootSubRoot.right, subRoot.right)
        
        
        if root is None: return False
        if root.val == subRoot.val:
            if compareTrees(root, subRoot): return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
