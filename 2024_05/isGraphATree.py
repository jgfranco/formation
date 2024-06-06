'''
Given an adjacency list of a directed graph, return "BINARY TREE" if it's a binary tree, "TREE" if it's any other type of tree, or "GRAPH" if it's neither.
 

EXAMPLE(S)
     1
   /   \ 
 2     3
/
4

input:
classify(
    {
        1: [2, 3],
        2: [4],
        3: [],
        4: []
    }
) -> BINARY TREE

--------------

     1        5
   /   \ 
 2     3
/
4

input:
classify(
    {
        1: [2, 3],
        2: [4],
        3: [],
        4: [],
        5: [],
    }
) -> GRAPH

--------------

     1       
   /   \ 
 2     3
   \  /
     4

input:
classify(
    {
        1: [2, 3],
        2: [4],
        3: [4],
        4: [],
    }
) -> GRAPH
 

FUNCTION SIGNATURE
function classify(adjList) {
'''
def classify(adjList):

  if len(adjList) == 0: return "BINARY TREE"
  potentialRoots = set()
  visited = set()
  moreThanTwoChildren = False
  
  for k in adjList:
  
    if k not in visited:
      potentialRoots.add(k)
      visited.add(k)
    if len(adjList[k])> 2:
      moreThanTwoChildren = True

    for child in adjList[k]:
      if child in potentialRoots:
        potentialRoots.remove(child)
      if child in visited:
        return "GRAPH"
      else:
        visited.add(child)
  


  if len(potentialRoots) ==1 and moreThanTwoChildren: 
    return "TREE"
  if len(potentialRoots) ==1:
    return "BINARY TREE"

  return "GRAPH"
  


multiTree = {
    1: [2, 3],
    2: [4],
    3: [5, 6, 7],
    4: [],
}
print(classify(multiTree) == 'TREE')

binaryTree = {
    1: [2, 3],
    2: [4],
    3: [],
    4: [],
}
print(classify(binaryTree) == 'BINARY TREE')

doubleRoot = {
    1: [2, 3],
    2: [4],
    3: [],
    4: [],
    5: [],
}
print(classify(doubleRoot) == 'GRAPH')

sharedParent = {
    1: [2, 3],
    2: [4],
    3: [4],
    4: [],
}
print(classify(sharedParent) == 'GRAPH')

oneNode = {
    1: [],
}
print(classify(oneNode) == 'BINARY TREE')

noNode = {}
print(classify(noNode) == 'BINARY TREE')

oneNodeCycle = {
    1: [1],
}
print(classify(oneNodeCycle) == 'GRAPH')

nestedCycle = {
    1: [2, 3],
    2: [],
    3: [3, 4],
    4: [],
}
print(classify(nestedCycle) == 'GRAPH')
