'''

In a binary tree, find the length of the longest consecutive sequence path.

A path is any route that only goes from parent to child (and never back up!)
 

EXAMPLE(S)
 
 
  1         1  
   \   
    2         # asceding = 2, descending = 1     
   / \  
       3      # asceding = 3, descending = 1  
     /  \   
         4    # asceding = 3, descending = 1 
            3 => 
        
 

1 2 3 2 1 not valid
boolean descending 



[1,(2),3,4,5] invaild
[2,3,4,5] # invaild -> travel back

keep a variable longestpathSoFar = 2
[1, 3] # discard 
[3, 2] # valid 
[3, 4, 5] #discar
[4, 3.2] # valid
[4, 5] =  valid


In this tree, the longest path would be 3 -> 4 -> 5. 1 is not included because 3 is not consecutive with 1. 2 is not included because it would need to travel back up to a parent to continue the path.
 

FUNCTION SIGNATURE
function longestPath(root) // returns a number

'''


class TreeNode:
    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right
def longestPath(root):


    longestPathSoFar = 0

    def recursiveLongestPath(node, asc, desc ):
        nonlocal longestPathSoFar

        #print(asc, desc)
        if not node: 

            longestPathSoFar = max(longestPathSoFar, asc, desc)
            #print(longestPathSoFar)
            return 

        if node.left:
            if node.left.value == node.value +1:
                recursiveLongestPath(node.left, asc, desc+1)
            elif node.left.value == node.value -1:
                recursiveLongestPath(node.left, asc +1, desc)
            else:
                longestPathSoFar = max(longestPathSoFar, asc, desc)
                recursiveLongestPath(node.left, 1, 1)

            
        if node.right:
            if node.right.value == node.value +1:
                recursiveLongestPath(node.right, asc, desc+1)
            elif node.right.value == node.value -1:
                recursiveLongestPath(node.right, asc +1, desc)
            else:
                longestPathSoFar = max(longestPathSoFar, asc, desc)
                recursiveLongestPath(node.right, 1, 1)
        
        recursiveLongestPath(node.left, asc, desc)

    

    recursiveLongestPath(root, 1, 1)
        
    return longestPathSoFar



    '''
    #JS
const t = new Node(1, None, new Node(3, new Node(2), new Node(4, null, new Node(5))));
const t2 = new Node(4, null, new Node(3, new Node(2, new Node(1)), new Node(4, null, new Node(5))));

console.log(longestPath(t), 3);
console.log(longestPath(t2), 4);
    
'''
t = TreeNode(1, 
        None,  
        TreeNode(3, 
            TreeNode(2),  
            TreeNode(4, 
                None,  
                TreeNode(5))))

print(longestPath(t),3)


t2 =  TreeNode(4, 
            None,  
            TreeNode(3,  
                TreeNode(2,  
                    TreeNode(1)),  
                TreeNode(4, 
                    None,  
                    TreeNode(5))));

print(longestPath(t2), 4)
    
'''
    #python
# Test empty tree
root = None
assert longestPath(root) == 0

# Test tree with only one node
root = Node(1)
assert longestPath(root) == 1

# Test tree with two nodes
root = Node(1, left=Node(2))
assert longestPath(root) == 2

# Test tree with multiple nodes
root = Node(1, left=Node(2), right=Node(3))
assert longestPath(root) == 2
    '''
    


    '''
class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def longestPath(root):
  maxLength = 1 if root else 0

  def helper(root, parentVal, currentIncreasingLength, currentDecreasingLength):
    nonlocal maxLength

    if not root:
      return

    if root.value == parentVal + 1:
      currentIncreasingLength += 1
      maxLength = max(currentIncreasingLength, maxLength)
    if root.value == parentVal - 1:
      currentDecreasingLength += 1
      maxLength = max(currentDecreasingLength, maxLength)

    helper(root.left, root.value, currentIncreasingLength, currentDecreasingLength)
    helper(root.right, root.value, currentIncreasingLength, currentDecreasingLength)

  helper(root.left, root.value, 1, 1)
  helper(root.right, root.value, 1, 1)

  return maxLength
  
    '''