"""
99. Recover Binary Search Tree

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
 

Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
"""

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
    def recoverTree(self, root) -> None:
        
        def inorder(root):
            if not root: return []

            return inorder(root.left) + [root.val] + inorder(root.right)

        def findTwoSwapped(nums):
            n = len(nums)
            x = y = None
              # 1 
            for i in range(n-1):
                        #2: 1      #1: 2
                if nums[i+1] < nums[i]:
                    y = nums[i+1] # 1
                    
                    if x is None:
                        x = nums[i] #3
                    else:
                        break
            
            return x, y

        def recover(r, count):
            if r: 
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -=1
                    if count ==0:
                        return 
                recover(r.left, count)
                recover(r.right, count)

        valArray = inorder(root)
        x,y = findTwoSwapped(valArray)
        recover(root, 2)