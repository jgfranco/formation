"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

114. Flatten Binary Tree to Linked List
Medium



11615

540

Add to List

Share
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
    def __str__(self) -> str:
        result = []
        from collections import deque
        q = deque([self])
        while q:
            curr = q.popleft()
            if curr is None: 
                result.append(None)
                continue
            result.append(curr.val)
            if not curr.left and not curr.right: continue # dont add "None" to leaf nodes
            if curr.left: q.append(curr.left)
            else: q.append(None)
            if curr.right: q.append(curr.right)
            else:
                q.append(None)
        
        
        return str(result)


    
def flatten(root: TreeNode):
    """
    Do not return anything, modify root in-place instead.
    """
    
    if root is None: return root

    """


                1
            2       5
          3  4        6

        1
            2
                3
                    4  
                        5
                            6
                                7
    """
    node = root
    while node:
    
        if node.left:
            rightMost = node.left
            while rightMost.right:
                rightMost = rightMost.right
            
            rightMost.right = node.right
            node.right = node.left
            node.left = None

        node = node.right


tree1 = TreeNode(1, 
                TreeNode(2, 
                        TreeNode(3),
                        TreeNode(4)),
                TreeNode(5,
                        None,
                        TreeNode(6)))

print(tree1)
flatten(tree1)

print(tree1)