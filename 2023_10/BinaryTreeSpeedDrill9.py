"""Q. Given a binary tree, count the number of elements with odd values in the tree.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[output] integer

the number of nodes with odd values in a tree"""

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
        curr =q.popleft()
        
        if curr.value %2 != 0: count +=1
        
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
        
    return count


"""Q. Given a binary tree and a target k, return any values in the tree that is repeated exactly k times. If multiple values are repeated k times, return the smaller value. If there isn't any value repeated k times, return -1.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[input] integer k

[output] integer"""

def solution(root, k):
    nodeMap = {}
    
    from collections import deque
    q = deque([root])

    while q:
        curr =q.popleft()
        
        nodeMap[curr.value] = nodeMap.get(curr.value, 0) +1
        
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
        
    smaller = float("inf")

    for key,v in nodeMap.items():
        if v == k:
            smaller = min(key, smaller)
    
    if smaller == float("inf"): return -1
    
    return smaller

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
    level = 0
    
    from collections import deque
    q = deque([root])
    levelSum = 0
    
    while q and level <= k:
        size = len(q)
        
        for _ in range(size):
            curr = q.popleft()
            levelSum += curr.value
            if curr.left: q.append(curr.left) 
            if curr.right: q.append(curr.right)
        level +=1

    if level <= k: return -1
    return levelSum

"""Q. Given a binary tree, sum all leaf nodes' values.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

root of the tree

[output] integer"""

def solution(root):
    from collections import deque
    q = deque([root])
    leafNodeSum = 0
    while q:
        curr =q.popleft()
        
        if not curr.left and not curr.right: 
            leafNodeSum +=curr.value
            continue
        
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
        
    return leafNodeSum

"""Q. Given a binary tree, update each node's value with its sum of child nodes. You must update the nodes by one level at a time starting from the top (root).

Example:
Given

          1
         / \
        2   3
       /
      4
returns

          5                    // 2+3
         / \
        4   3                  // 4
       /
      4
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

[output] tree.integer
"""


def solution(root):

    from collections import deque
    q = deque([root])
    
    while q:
        curr =q.popleft()
        
        if not curr.left and not curr.right:
            continue
        curr.value = 0
        
        if curr.left: 
            curr.value +=curr.left.value
            q.append(curr.left)
        if curr.right: 
            curr.value +=curr.right.value
            q.append(curr.right)
        
    return root



"""Q. Given an binary tree and a target subtree, determine if the original tree contains a target subtree. A subtree of a tree is a tree consisting of a node in the original tree and all of its descendants while maintaining the same structure.

Examples:

Given a tree:
            1
          /  \
        2      3
      /  \
    4     5
          /
        6

and a subtree:
        5 
      / 
    6

returns true
Given a tree:
            1
          /  \
        2      3
      /  \
    4     5
          /
        6
and a subtree:
        2 
      /  \
    4     5

returns false (6 is missing in a subtree)
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] tree.integer root

[input] tree.integer subRoot

[output] boolean
"""

def solution(root, subRoot):


    def isSubtree(original, subRoot):
        if not original and not subRoot: return True
        
        if not original or not subRoot: return False
        if original.value != subRoot.value: return False
    
        return isSubtree(original.left, subRoot.left) and isSubtree(original.right, subRoot.right)
        
    

    from collections import deque
    q = deque([root])
    
    while q:
        curr =q.popleft()
        
        if curr.value == subRoot.value:
            if isSubtree(curr, subRoot):
                return True
    
        if curr.left: 
            q.append(curr.left)
        if curr.right: 
            q.append(curr.right)
        
    return False
