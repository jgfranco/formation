
'''
Given a binary search tree, write a function that returns the kth value in the in order traversal. 
 

EXAMPLE(S)
   3
 2  4
1    5

inorder list of values [1,2,3,4,5]

k=2
Output: 3

        3
  2          4
1 2.5    3.5  5

 
[1,2,2.5,3,3.5,4, 5]


   4
 2  10
1  8 

k=3
Output: 8
 

FUNCTION SIGNATURE
function findKth(root, k) // returns the integer value at the node

explore:
return None if the kth node does not exist

brainstorm:




    4
 2   5
1 3    6

output = 4


recursive approach:


    findKth(root, k) # k = 3

        initialize a counter with -1

        recursive function(node) # 4
        
            base case: current Node is none

            recursive call process left subtree
            
            current node:
                increment the counter # 3
                check if counter equals k: 
                    return value # return 4
            
            recursive call process right subtree

            return 

'''

class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# Time O(N) where N is the number of nodes 
# Space O(H) where H is the height of the tree
def findKth(root, k):

    counter = -1

    def inOrderTraversal(node):

        nonlocal counter
        if not node: return None

        left = inOrderTraversal(node.left)
        
        counter += 1
        if counter == k: return node.value

        right = inOrderTraversal(node.right)

        if left != None: return left
        if right != None: return right

        return None


    return inOrderTraversal(root)

"""
   3
 2  4
1    5

"""

tree = TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4, None, TreeNode(5)))

print(findKth(tree, 2)) # 3
print(findKth(tree, 0)) # 1
print(findKth(tree, 1)) # 2
print(findKth(tree, 100)) # None

'''
        3
    1       4
      2
t = new Node(3, new Node(1, null, new Node(2)), new Node(4));

'''
tree2 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(findKth(tree2, 0), 1)
print(findKth(tree2, 1), 2)
print(findKth(tree2, 2), 3)
print(findKth(tree2, 3), 4)
print(findKth(tree2, 27), None)


'''

Formation's solution

class Node {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}

function findKth(root, k) {
  function helper(root, k) {
    if (!root) return [0, null];

    let consumed = 0, result = null;

    if (root.left) {
      [consumed, result] = helper(root.left, k);
      if (result !== null) return [consumed, result];
    }

    if (consumed === k) {
      return [consumed, root.value];
    }
    consumed++;

    const [rconsumed, rresult] = helper(root.right, k - consumed);
    return [consumed + rconsumed, rresult];
  }

  const [consumed, result] = helper(root, k);
  return result;
}

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_kth(root, k):
    # Helper function returns (count_of_nodes_visited, kth_value_if_found)
    def helper(node, k):
        # Base case: no node → visited 0 nodes and found nothing
        if not node:
            return 0, None

        consumed = 0  # how many nodes we've counted so far
        result = None

        # --- Traverse left subtree first (in-order) ---
        if node.left:
            consumed, result = helper(node.left, k)
            # If the kth node was already found in the left subtree, bubble it up immediately
            if result is not None:
                return consumed, result

        # --- Visit current node ---
        # After visiting left subtree, 'consumed' tells how many nodes we've already seen.
        # If we've already consumed k nodes, the current node is the kth.
        if consumed == k:
            return consumed, node.value

        # Otherwise, include the current node in our count
        consumed += 1

        # --- Traverse right subtree ---
        # We pass k - consumed because we've already visited 'consumed' nodes.
        rconsumed, rresult = helper(node.right, k - consumed)

        # Total nodes visited = left + current + right
        return consumed + rconsumed, rresult

    # Kick off the recursion
    consumed, result = helper(root, k)
    return result

'''