



'''
Given a binary search tree, write a function that returns the kth value in the in order traversal. 

inorder traversal: left node -> root -> right node
 

EXAMPLE(S)
   3
 2  4
1    5

k=2
Output: 3

   4
 2   10
1   8 


[1, 2, 4, 8, 10]


k=3tt
Output: 8
 

k can be larger than the total nodes in the tree
we are returning the value


FUNCTION SIGNATURE
def findKth(root, k) // returns the integer value at the node

pseudo code


initialize an array for the values
recursive function (node)

    no node: return 

    call on left recursively
    process current node -> add value to the array
    call on right node recursively
  
return array at k
'''

class TreeNode:
  def __init__(self, val, left = None, right = None):
    self.val = val
    self.left = left
    self.right = right

# def findKth(root, k):
#   values = []

#   def dfs(node):
#     if not node: return

#     dfs(node.left)
#     values.append(node.val)
#     dfs(node.right)
  
#   dfs(root)
#   if k >= len(values): return None
#   return values[k]

def findKth(root, k):
    if not root: return 

    
    findKth(root.left, k)
    if k == 0: return root.val
    k -= 1
    findKth(root.right, k)


    return None

#t = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4, None, TreeNode(5)))

"""
   3
 2  4
1    5
"""

# print(findKth(t, 2)) # 3
# print(findKth(t, 0)) # 1
# print(findKth(t, 4)) # 5
# print(findKth(t, 7)) # None\



print("Set EMPTY")
print(findKth(None, 0), None)
print(findKth(None, 1), None)

print("\nSet 1")
t = TreeNode(1)
print(findKth(t, 0), 1)
print(findKth(t, 1), None)
print(findKth(t, 27), None)

print("\nSet 2")
t = TreeNode(2, TreeNode(1))
print(findKth(t, 0), 1)
print(findKth(t, 1), 2)
print(findKth(t, 2), None)
print(findKth(t, 27), None)

print("\nSet 3")
t = TreeNode(1, None, TreeNode(2))
print(findKth(t, 0), 1)
print(findKth(t, 1), 2)
print(findKth(t, 2), None)
print(findKth(t, 27), None)

print("\nSet 4")
t = TreeNode(2, TreeNode(1), TreeNode(3))
print(findKth(t, 0), 1)
print(findKth(t, 1), 2)
print(findKth(t, 2), 3)
print(findKth(t, 3), None)
print(findKth(t, 27), None)

print("\nSet 5")
t = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(findKth(t, 0), 1)
print(findKth(t, 1), 2)
print(findKth(t, 2), 3)
print(findKth(t, 3), 4)
print(findKth(t, 27), None)


# Time: O(n) Space: O(n + h) 

