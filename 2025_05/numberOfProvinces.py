"""
https://leetcode.com/problems/number-of-provinces/description/
"""

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:

        n = len(isConnected)

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] and not visited[j]: # if there is a connection between cities 
                    visited[j] = True
                    dfs(j)

        visited = [False] * n
        provinces = 0
        for i in range(n):
            if not visited[i]:
                provinces += 1
                visited[i] = True
                dfs(i)
        
        return provinces
