'''
In a binary tree, find the length of the longest consecutive sequence path.

A path is any route that only goes from parent to child (and never back up!)
 

EXAMPLE(S)
  1  
   \  
    2 
   / \  
  2   3   incCount, decCount
       \   
        2
         \
          1
           \
            0

        return 4

In this tree, the longest path would be 3 -> 4 -> 5. 1 is not included because 3 is not consecutive with 1. 2 is not included because it would need to travel back up to a parent to continue the path.
 
    1 
   / \
  2   3

  return 2



DFS approach

paths 
    increasing sequences
    decreasing sequences



main function 

    define a loongestPath counter

    helper function(node, parentsValue, incCount, decCount):

        base case ( node is NOne):
         updating the max of incCount and decCount, longestPath

        if the node's value is parentsValue +1: 
            incCount +1 
        elif the node's value is parentsValue -1: 
            decCount +1 
        else:
            save max between incCOunt and decCOunt on longespaht
            restart counts to 1

        recursive call on left child
        recursive call on right child

FUNCTION SIGNATURE
function longestPath(root) // returns a number
'''

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def longestPath(root):
    if not root: return 0

    longestPathCount = 0

    def dfs(node, parentsValue, incCount, decCount):
        nonlocal longestPathCount
        if not node:
            longestPathCount = max(longestPathCount, incCount, decCount)
            return 

        if node.value == parentsValue +1:
            incCount +=1
        elif node.value == parentsValue -1:
            decCount +=1
        else:
            longestPathCount = max(longestPathCount, incCount, decCount)
            incCount = 1
            decCOunt = 1
        
        dfs(node.left, node.value, incCount, decCount)
        dfs(node.right, node.value, incCount, decCount)

    dfs(root.left, root.value, 1, 1)
    dfs(root.right, root.value, 1, 1)

    return longestPathCount


# Test empty tree
root = None
print( longestPath(root) == 0)

# Test tree with only one node
root = Node(1)
print( longestPath(root) , 1)

# Test tree with two nodes
root = Node(1, left=Node(2))
print( longestPath(root) , 2)

# Test tree with multiple nodes
root = Node(1, left=Node(2), right=Node(3))
print( longestPath(root) , 2)
    

    
'''
EXAMPLE(S)
  1  
   \  
    2 
   / \  
  2   3   increasingCount, decCount
       \   
        2
         \
          1
           \
            0

        return 4
'''
root = Node(1, 
        None, 
        Node(2, Node(2), Node(3, None, Node(2, None, Node(1, None, Node(0))))))

print(longestPath(root)) # 4