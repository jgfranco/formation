'''
❓ PROMPT
Given a vertex and edge list of users of a social network and two user IDs, return whether they are friends of friends.

Example(s)
users = ["Jeff", "Susan", "Ed", "Fred", "Jason", "Zach"]
friends = [("Jeff", "Susan"), ("Jeff", "Fred"), ("Susan", "Ed"), ("Ed", "Fred"), ("Jason", "Zach")]

Jeff---|
 |     |
Susan  |   Jason - Zach
 |     |
 Ed - Fred

isFOF(users, friends, "Jeff", "Ed") -> True
isFOF(users, friends, "Jeff", "Susan") -> False
isFOF(users, friends, "Jeff", "Jeff") -> False

 

🔎 EXPLORE
List your assumptions & discoveries:
adjecencyList = {
  "Jeff": ["Susan, Fred"],
  "Susan": ["Jeff", "Ed"],
  "fred": ["Jeff", "Ed"],
  "Ed": ["Susan", "Fred"],
  "Jason": ["Zach"]
  "Zach": ["Jason"]
}

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function isFOF(vertex_list, edge_list, user1, user2) {
def isFOF(vertex_list: list[str], edge_list: list, user1: str, user2: str) -> bool:
'''

def generateAdjecencyList(vertexList, edgeList):
  adjList = {}

  for vertex in vertexList:
    adjList[vertex] = []

  for friend1, friend2 in edgeList:
    adjList[friend1].append(friend2)
    adjList[friend2].append(friend1)
  
  return adjList
  
def isFOF(vertexList, edgeList, user1, user2):
  if user1 not in vertexList or user2 not in vertexList: return False
  
  from collections import deque
  adjecencyList = generateAdjecencyList(vertexList, edgeList)
  
  q = deque()
  q.append((user1, 0))
  visited = set()
  visited.add(user1)
  
  while q:
    user, degree = q.popleft()

    if degree > 2: return False
    if degree == 2: 
      return user == user2

    for friend in adjecencyList[user]:
      if friend not in visited:
        q.append((friend, degree+1))
        visited.add(friend)
  
  return False



'''
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

users = ["Jeff", "Susan", "Ed", "Fred", "Jason", "Zach"]
friends = [("Jeff", "Susan"), ("Jeff", "Fred"), ("Susan", "Ed"), ("Ed", "Fred"), ("Jason", "Zach")]

# Jeff---|
#  |     |
# Susan  |   Jason - Zach
#  |     |
#  Ed - Fred

print(isFOF(users, friends, "Jeff", "Ed") == True)
print(isFOF(users, friends, "Jeff", "Susan") == False)
print(isFOF(users, friends, "Jeff", "Jeff") == False)
print(isFOF(users, friends, "Foo", "Bar") == False)
