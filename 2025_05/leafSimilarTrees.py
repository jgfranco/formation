


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def getLeaves(self, root):
        leaves = []

        def helper(node):
            if not node: return
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return leaves

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        tree1Leaves = self.getLeaves(root1)
        tree2Leaves = self.getLeaves(root2)

        print(tree1Leaves, tree2Leaves)
        return tree1Leaves == tree2Leaves