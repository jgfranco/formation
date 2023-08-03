'''
Find Nodes Occurring K Times

Given a binary tree and an integer (k), find and return an array of unique nodes that occur **at least (k) times** in the tree.

For example, if Node(5) occurs 3 times in the tree, and (k) = 3, your result array would include the value of Node(5) (simply **5** in this case).
 

EXAMPLE(S)
    2
 2     3
7 3  14 9

k = 2, should return [2, 3]

   12
 3    3
1 _  6 _

k = 2, should return [3]

       12
    3      4
  1  _    6  _
9  _     _ _

k = 1, should return [12, 3, 4, 1, 6, 9]
 

FUNCTION SIGNATURE
function findNodesOccuringKTimes(head, k) {
'''

class TreeNode:
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

def findNodesOccurringKTimes(head, k):
  from collections import deque

  nodeMap = {}
  q = deque([head])

  while q:

    curr = q.popleft()
    nodeMap[curr.value] = nodeMap.get(curr.value, 0) + 1

    if curr.left: q.append(curr.left)
    if curr.right: q.append(curr.right)

  result = []

  for key,val in nodeMap.items():

    if val == k:
      result.append(key)

  return result


tree = TreeNode(1, 
                TreeNode(2, TreeNode(4), TreeNode(6)), 
                TreeNode(2, TreeNode(3), TreeNode(3)))


print(findNodesOccurringKTimes(tree, 2), 'expect [2, 3]')
print(findNodesOccurringKTimes(tree, 1), 'expect [1, 4, 6]')
print(findNodesOccurringKTimes(tree, 0), 'expect []')  