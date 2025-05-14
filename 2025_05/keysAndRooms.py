"""
https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        from collections import deque

        q = deque([0])

        while q:

            key = q.popleft()
            visited.add(key)
            for k in rooms[key]:
                if k not in visited:
                    q.append(k)
        
        return len(rooms) == len(visited)
            