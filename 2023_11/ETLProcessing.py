
'''
❓ PROMPT
You are working on a large-scale data ETL (Extract, Transform, Load) 
process where multiple data tables are processed. Some tables are 
dependent on the output of other tables' processing and therefore 
need to be processed after them. Your task is to determine a valid 
order to process the tables such that all dependencies are honored.

You are given a list of n tables, where each table i has a unique 
identifier from 0 to n - 1. You are also given a list of pairs 
where pairs[i] = [a, b] indicates that table b must be processed 
before table a can be processed.

Write a function process_order(n: int, 
dependencies: List[List[int]]) -> List[int] that returns the order 
in which the tables should be processed to satisfy all dependencies. 
If there are multiple orders, return any of them. If there is no 
valid processing order, return an empty list.

Example(s)
Let's assume we have 4 tables numbered from 0 to 3. If table 3 
depends on tables 2 and 0, and table 2 depends on tables 0 and 1, 
we can represent these dependencies as [[3, 2], [3, 0], [2, 0], 
[2, 1]]. A valid processing order would be [0, 1, 2, 3], so 
process_order(4, [[3, 2], [3, 0], [2, 0], [2, 1]]) should return 
[0, 1, 2, 3].

If we have a circular dependency, such as [[2, 1], [1, 2]] 
(table 2 depends on table 1 and table 1 depends on table 2), 
then process_order(2, [[2, 1], [1, 2]]) should return [], as 
there's no valid processing order.
 

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
def process_order(n: int, dependencies: List[List[int]]) -> List[int]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

from typing import List
from collections import deque, defaultdict

def process_order(n: int, dependencies: List[List[int]]) -> List[int]:
    # initialize graph and in-degree count
    graph = defaultdict(list)
    indegree = defaultdict(int)

    # construct graph and count in-degree for each node
    for pair in dependencies:
        a, b = pair
        graph[b].append(a)
        indegree[a] += 1
    print(indegree)
    
    print(graph)
    
    # find all nodes with in-degree 0
    queue = deque([i for i in range(n) if indegree[i] == 0])
    print(queue)
    # result list
    result = []
    
    # Kahn's algorithm for topological sorting
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    print(result)
    return result if len(result) == n else []

print(process_order(4, [[3, 2], [3, 0], [2, 0], 
[2, 1]]))

