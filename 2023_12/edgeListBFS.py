
'''
❓ PROMPT
Given a vertex and edge list of nodes and a start node for an undirected graph return the sum of all the nodes IDs accessible from the start node. For practice's sake, do this in BFS order.

Example(s)
vertexList: [1, 2, 3, 4, 5]
edgeList: [(1, 2), (2, 3), (1, 3)]

1--2
| /
3      4    5

sumNodes(vertexList, edgeList, 1) -> 6

Node 1 has access to 2 and 3. The sum of all these nodes is 6. Nodes 4 and 5 aren't accessible.
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function sumNodes(vertexList, edgeList, startNode) {
def sumNodes(vertexList: list, edgeList: list, startNode: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def getAdjecencyList(vertexList, edgeList):
  adjList = {}

  for vertex in vertexList:
    adjList[vertex] = []
  for node1, node2 in edgeList:
    adjList[node1].append(node2)
    adjList[node2].append(node1)

  return adjList

def sumNodes(vertexList, edgeList, startNode):
  if startNode not in vertexList: return 0

  result = 0 
  adjList = getAdjecencyList(vertexList, edgeList)

  from collections import deque
  q = deque([startNode])
  visited = set()
  visited.add(startNode)

  while q:

    curr = q.popleft()
    result  += curr
    for neighbour in adjList[curr]:
      if neighbour not in visited:
        visited.add(neighbour)
        q.append(neighbour)
  

  return result

vertexList= [1, 2, 3, 4, 5]
edgeList= [(2, 1), (3, 2), (3, 1)]

print(sumNodes(vertexList, edgeList, 1), "expect 6")
print(sumNodes(vertexList, edgeList, 10000), "expect 0")
print(sumNodes(vertexList, edgeList, 4), "expect 4")