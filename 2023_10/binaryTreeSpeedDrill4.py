"""Q. Given a binary tree and k, count the number of nodes that are divisible by k in tree.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[input] integer k

[output] integer"""


#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def solution(root, k):
    if not root: return 0
    from collections import deque
    
    q = deque([root])
    count= 0
    while q:
        node = q.popleft()
        if node.value %k ==0:
            count +=1
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    
    return count

"""Q. Given a binary tree and k, sum first k levels in tree, where the root node is at level 0. If k exceeds the maximum level of a given tree, return -1.

Example:
          1
            \
              2
                \
                 4

with k = 1 returns 3 (1+2) because the last 4 is below the level.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[input] integer k

[output] integer"""

def solution(root, k):
    
    if not root: return 0
    from collections import deque
    
    q = deque([root])
    levelSum = 0
    level = -1
    while q and level < k:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            levelSum +=node.value
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        level +=1
        
    if level != k: return -1
    return levelSum


"""Q. Given a binary search tree, return the value of the violating node. When there is a violation, return the lowest node. If there is no violating node, return -1.

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

the value of the violating node"""


def solution(root):

    
    def helper(node, leftMin, rightMax):
        if not node: return -1
        
        if node.value > rightMax or node.value < leftMin: return node.value
        
        return max(helper(node.left,leftMin, node.value), helper(node.right, node.value, rightMax))  
         
    return helper(root, float("-inf"), float("inf"))


"""Given a binary tree, return the most frequent value. If multiple most frequent exist, return any at random.

Function Description
solution has the following parameters:

root: the root of the tree

Returns:
The int value that is most frequent in the tree

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

The root of the tree

[output] integer"""


def solution(root):
    #if not root: return 0
    from collections import deque
    
    q = deque([root])
    nodeMap = {}
    while q:
        node = q.popleft()
        nodeMap[node.value] = nodeMap.get(node.value, 0) +1
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    
    sortedNodes = sorted(nodeMap.items(), key = lambda x: x[1], reverse=True)
    
    
    return sortedNodes[0][0]
    

"""Q. Given a binary tree, sum all leaf nodes' values.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[output] integer

"""

def solution(root):
    if not root: return 0
   
    if not root.left and not root.right:
        return root.value + solution(root.left) + solution(root.right)
        
    return solution(root.left) + solution(root.right)


"""Q. Given a binary tree, return the sum of the level whose values add up to the highest sum.

     5
   2   6
  1 3    8
        7
returns 12 because 1 + 3 + 8 is the largest sum of any level in the tree.

     51
   2   6
  1 3    8
       17
return 51.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[output] integer

"""

def solution(root):
    from collections import deque
    q = deque([root])
    levelSums = []

    while q:
        size = len(q)
        levelSum = 0
        for _ in range(size):
            node = q.popleft()
            levelSum += node.value
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        levelSums.append(levelSum)
    
    return max(levelSums)

