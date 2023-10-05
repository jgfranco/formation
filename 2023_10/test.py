"""Q. Given a binary tree, return the the maximum sum of nodes from the root to any leaf.

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

the sum of the max path"""

#
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
     self.value = x
     self.left = None
     self.right = None

def solution(root):
    
    maxSum= float("-inf")
    
    def helper(currentSum, node):
        nonlocal maxSum
        if node is None:
            if currentSum > maxSum:
                maxSum = currentSum
            return 
        helper(currentSum+ node.value, node.left)
        helper(currentSum+ node.value, node.right)
        
    helper(0, root)
    return maxSum

Q. Given a binary tree, return the values of the nodes when facing the tree from the right side (from top to bottom).

Example:
Input:
   1              <---
 /   \
2     5         <---
 \  
  7               <---
Output: [1, 5, 7]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[output] array.integer


def solution(root):

    from collections import deque
    q = deque([root])
    rightSideNodes = []
    while q:
        size = len(q)
        
        curr = None
        for _ in range(size):
            curr = q.popleft()
            if curr.left:q.append(curr.left)
            if curr.right: q.append(curr.right)
        rightSideNodes.append(curr.value)
        
    return rightSideNodes

Q. Given a binary tree and a target k, count the number of nodes that has a value less than k.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[input] integer target

[output] integer

def solution(root, target):

    from collections import deque
    q = deque([root])
    count = 0
    while q:
        curr = q.popleft()
        
        if curr.value < target:
            count +=1
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
        
    return count

"""Q. Given a binary tree, sum all left leaf nodes.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

[output] integer"""

def solution(root):

    leftChildrenSum = 0
    def helper(isLeftChild, node):
        nonlocal leftChildrenSum
        if node is None: return
         
        if not node.left and not node.right and isLeftChild:
            leftChildrenSum += node.value
            
        helper(True, node.left)
        helper(False, node.right)
        
        return 
        
    helper(False, root)
    return leftChildrenSum

"""Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be solution(t) = true.

Here's what the tree in this example looks like:

    1
   / \
  2   2
 / \ / \
3  4 4  3
As you can see, it is symmetric.

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be solution(t) = false.

Here's what the tree in this example looks like:

    1
   / \
  2   2
   \   \
   3    3
As you can see, it is not symmetric.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer t

A binary tree of integers.

Guaranteed constraints:
0 ≤ tree size < 5 · 104,
-1000 ≤ node value ≤ 1000.

[output] boolean

Return true if t is symmetric and false otherwise."""

def solution(t):
    
    def helper(left, right):
    
        if left is None and right is None: return True
        if left is None or right is None: return False
        if left.value != right.value: return False
        
        return helper(left.left, right.right) and helper(left.right, right.left)
        
    if t is None: return True
    return helper(t.left, t.right)

    """Q. Flip a given binary tree.

Examples:

Given:
           1
          / \
         2   3

returns:
           1
          / \
         3   2
Given:
           1
          / \
         2   3
        / \
       4   5
          /
         6

returns:
           1 
          / \
         3   2
            / \
           5   4
            \
             6
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

[output] tree.integer"""

def solution(root):
  if root is None: return None
      new = Tree(root.value)
      def helper(original, new):

          if original is None: return
          
          if original.right:
              new.left = Tree(original.right.value)
          if original.left:
              new.right = Tree(original.left.value)
          
          helper(original.left, new.right)
          helper(original.right, new.left)
          
      helper(root, new)
      return new

