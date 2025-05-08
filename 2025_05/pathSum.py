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
        from collections import defaultdict
        
        def dfs(node, curr_sum):
            
            nonlocal num_paths
            if node is None:
                return 

            curr_sum += node.val
            if curr_sum == targetSum:
                num_paths += 1

            num_paths += h[curr_sum-targetSum]
            h[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            h[curr_sum] -= 1

        
        num_paths = 0
        h = defaultdict(int)
        dfs(root, 0)

        return num_paths


        