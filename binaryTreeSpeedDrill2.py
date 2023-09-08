"""
Q. Given a binary tree, count the number of elements with odd values in the tree.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[output] integer

the number of nodes with odd values in a tree
"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(root):
    from collections import deque
    q = deque([root])
    count = 0
    while q:
        curr = q.popleft()
        if curr.value % 2 != 0:
            count +=1
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return count
"""

Q. Given a binary tree, count the number of elements with negative values in the tree.

0 is a non-negative integer.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[output] integer

the number of the elements with negative value
"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(root):
    from collections import deque
    q = deque([root])
    count = 0
    while q:
        curr = q.popleft()
        if curr.value < 0:
            count +=1
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    return count
"""

Q. Given a binary tree, return the the maximum sum of nodes from the root to any leaf.

For example, in this tree:
1
2 3
4 5 6 7

There are 4 leaves, and thus 4 paths from root to leaf:
1 -> 2 -> 4, 1 -> 2 -> 5, 1 -> 3 -> 6, 1 -> 3 -> 7

The one with the maximum sum is 1 -> 3 -> 7, so return 11.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

roof of the tree

[output] integer

the sum of the max path
"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(root):

    maxSum = float("-inf")
    def dfs(pathSum, node):
        nonlocal maxSum
        if node is None: return 
        
        pathSum += node.value
        maxSum  = max(pathSum, maxSum)
        if node.left:
            dfs(pathSum, node.left)
        if node.right:
            dfs(pathSum, node.right)
        
    dfs(0, root)
    return maxSum
        
"""
Q. Given a binary tree, count the number of distinct elements in the tree.

     1
   9   5
  1     3
returns 4.

     6
   6   5
  1   6
returns 3.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[output] integer

the number of unique elements


"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(root):
    elements = set()

    from collections import deque
    q = deque([root])
    
    while q:
        curr = q.popleft()
        
        if curr.value not in elements:
            elements.add(curr.value)
        
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    
    return len(elements)
        
"""
Q. Given a binary tree, count the number of leaf nodes.

Leaf node is a node that does not have any child nodes.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

roof of the tree

[output] integer

the number of leaf nodes
"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(root):

    from collections import deque
    q = deque([root])
    count =0
    while q:
        curr = q.popleft()
        
        if not curr.left and not curr.right:
            count +=1
            
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    
    return count
        
"""
Q. Given a binary search tree, return the value of the violating node. When there is a violation, return the lowest node. If there is no violating node, return -1.

The properties of a binary search tree are that:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A violating node occurs when one of these properties is not met.

For example, in this tree:

      5
    /  \
  2    10
   \
    8
We have a violation between 5 and 8 because 8 is not less than 5. Because 8 is the lower node, return 8.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

roof of the tree

[output] integer

the value of the violating node

"""
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(root):
    
    def helper(lowest, highest, node):
        
        if not node: return -1
        
        if node.value < lowest or node.value > highest:
            return node.value
        
        return max(helper(lowest, node.value, node.left), helper(node.value, highest, node.right))
         
    return helper(float("-inf"), float("inf"), root)