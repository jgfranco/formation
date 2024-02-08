
'''
Today, you will be finding the sum of all the left leaves in a binary tree. A left leaf is any leaf node that is the left child of its parent.

Source: https://leetcode.com/problems/sum-of-left-leaves/
 

EXAMPLE(S)
The following tree returns 5, which is the sum of 1 and 4.
     3
   /   \
1       5
       /
     4
 

bfs
iterative 
queue 
(node, isLeftChild: boolean)

initializing a queue
initializing a sum variable
appending the root and False

traverse the queue
    pop the node and boolean

    if the node is a leaf  and isLeftChild:
        add node's value to the sum
    
    check for left child:
        append to queue left child and True for isLeftChild

    check for right child:
        append to queue left child and False for isLeftChild

return the sum 

FUNCTION SIGNATURE
def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
'''

class TreeNode:
    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def sumOfLeftLeaves(root):
    from collections import deque
    q = deque()
    leftChildrenSum = 0
    q.append((root, False))

    while q:
        node, isLeftChild = q.popleft()

        if not node.left and not node.right and isLeftChild:
            leftChildrenSum += node.value
        
        if node.left:   
            q.append((node.left, True))
        if node.right:
            q.append((node.right, False))

    return leftChildrenSum

tree = TreeNode(3, 
            TreeNode(1), 
            TreeNode(5,
                TreeNode(4)))

root = TreeNode(2)

onlyRightTree = TreeNode(3, 
                    None, 
                    TreeNode(5,
                        None,
                        TreeNode(100)))
    
print(sumOfLeftLeaves(tree))
print(sumOfLeftLeaves(root))
print(sumOfLeftLeaves(onlyRightTree))


''' formation solution 

def sumOfLeftLeaves(root) -> int:
    if not root:
        return 0
    res = 0
    if root.left:
        if not root.left.left and not root.left.right:
            res += root.left.val
        else:
            res += sumOfLeftLeaves(root.left)
    res += sumOfLeftLeaves(root.right)
    return res
'''