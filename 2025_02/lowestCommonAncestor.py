

class TreeNode:
  def __init__(self, value, left= None, right = None):
    self.value = value
    self.left = left
    self.right = right
def lca(root: TreeNode, node1: TreeNode, node2: TreeNode) -> (TreeNode, int):

  if not root:
    return None

  if root == node1 or root == node2:
    return root

  left = lca(root.left, node1, node2)
  right = lca(root.right, node1,node2)

  if left and right:
    return root
  
  return left if left else right

def lca_3(root, node1, node2, node3):
  return lca(root, node3, lca(root, node1, node2))


from collections import deque
def lca_n(root, nodes: list[TreeNode]):
  node_queue = deque(nodes)

  while len(node_queue) > 1:
    node_queue.appendleft(lca(root, node_queue.pop(), node_queue.pop()))
  
  return node_queue.pop()





"""
This solution works like this:

* The TreeNode is the actual LCA, not one of the found nodes
  * The int is the number of nodes found so far.
* Call recursively on root.left and root.right.
* Base case: return (null, 0) if root is null.
* If left’s found is 1 and right’s found is 1, return (root, 2)
  * If left’s found is 2, it must also have the lca, return the lca
    * If right’s found is 2, it must also have the lca, return the lca
  * Otherwise, return (nil, left’s found + right’s found)


//               30
//       15              45
//   10     17       35      55
// 4  11  16  19   32  37  50  70


      """


n1 = TreeNode(4)
n3 = TreeNode(19)
n2 = TreeNode(17, TreeNode(16), n3)
n4 = TreeNode(32)

tree = TreeNode(30,  TreeNode(15, TreeNode(10,  n1, TreeNode(11)), n2), TreeNode(45, TreeNode(35, n4, TreeNode(37)),  TreeNode(55, TreeNode(50), TreeNode(70))))


print(lca(tree, tree.left, tree.right).value) # 30
print(lca(tree, tree.left.right.left, tree.left.right.right).value) # 17
print(lca_3(tree, tree.left.right.left, tree.left.right.right, tree.right).value) # 30
print(lca_n(tree, [n1, n2, n3,n4]).value) # 30