from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        
        adjList = defaultdict(list)

        for a,b in connections:
            adjList[a].append((b, True))
            adjList[b].append((a, False))

        count = 0

        q = [0]
        visited = set()

        while q:
            node = q.pop()
            
            visited.add(node)
            for a,b  in adjList[node]:
                if a not in visited:
                    q.append(a)
                    if b: count += 1
                    
        return count 