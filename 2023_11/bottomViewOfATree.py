'''
Given a binary tree where each node holds an integer, write a function that returns an array of integers representing the bottom view of the tree.

To calculate the bottom view of a tree, consider the horizontal distance of each node. The horizontal distance of a binary tree node describes how far left or right the node will be when the tree is printed out.

More rigorously, we can define it as follows:

The horizontal distance of the root is 0.  
The horizontal distance of a left child is hd(parent) - 1.  
The horizontal distance of a right child is hd(parent) + 1.
 

EXAMPLE(S)
For this tree, hd(1) = -2, and hd(6) = 0.


-3-2 -1    0    1   2 3 4       
           5
        /     \
      3         7
    /  \      /   \
  1     4    6     9
 /                /
0                8 (1)
map = {0: 5, 3: -1, 7: 1}
q = [(5, 0), (3, -1), (7, 1)]

The bottom view is either [0, 1, 3, 4, 8, 9] or [0, 1, 3, 4, 6, 8, 9]
     3  
   2    4 
1          5

FUNCTION SIGNATURE
func bottomView(root: Node) -> [Int]
'''

class TreeNode:
    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right



# O(w) = width of tree (space)
# TIme O(nlogn)

def bottomView(root):
    from collections import deque
    q = deque()
    q.append((root, 0))
    bottomViewMap = {}
    while q:
        node, hd = q.popleft()

        bottomViewMap[hd] = node.value

        if node.left:
            q.append((node.left, hd-1))
        if node.right:
            q.append((node.right, hd+1))

    sortedView = sorted(bottomViewMap.items(), key = lambda x:x[0])
  
    return [y for x,y in sortedView]

tree= TreeNode(5, 
        TreeNode(3, 
            TreeNode(1,
                TreeNode(0), 
                None), 
            TreeNode(4)),
        TreeNode(7, TreeNode(6), TreeNode(9, TreeNode(8))))


print(bottomView(tree))

  


#formation solution 

def tree_bottom_view(root):
    lowest_node_for_distance = {}

    def helper(root, distance, level):
        if not root:
            return
        if distance not in lowest_node_for_distance or level > lowest_node_for_distance[distance][1]:
            lowest_node_for_distance[distance] = (root.val, level)

        helper(root.left, distance - 1, level + 1)
        helper(root.right, distance + 1, level +1)

    helper(root, 0, 0)

    for key in sorted(lowest_node_for_distance.keys()):
        print(lowest_node_for_distance.get(key)[0], end=' ')
        

