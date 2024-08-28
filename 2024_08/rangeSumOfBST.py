"""
https://leetcode.com/problems/range-sum-of-bst/
Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
"""
class Solution:
    def rangeSumBST(self, root, low, high):
        
        from collections import deque
        
        q = deque([root])
            
        result = 0
        while q:
            node = q.popleft()
            value= node.val
            if value >= low and value <= high:
                result += value

            if node.left and value > low:
                q.append(node.left)
            if node.right and value < high:
                q.append(node.right)
 
        return result