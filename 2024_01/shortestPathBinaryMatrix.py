"""
1091. Shortest Path in Binary Matrix

Add to List

Share
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

"""
def shortestPathBinaryMatrix(grid) -> int:
  if grid[0][0] == 1: return -1
  from collections import deque
  q = deque()
  q.append([0,0])
  grid[0][0] = 1 # mark the starting node as visited with the amount of nodes visited so far (1, aka current one)
  n  = len(grid)
  goal = (n-1, n-1)
  
  directions = [(1,0),(0,1),(-1,1),(1,-1),(-1,0),(0,-1),(-1,-1),(1,1)]
  
  def inBounds(x,y):
    if x <0 or x >= n or y <0 or y >= n: return False
    return True
  
  while q:
    x,y = q.popleft()
    if (x,y) == goal: return grid[x][y]
      
    for dx, dy in directions:
      nx = x + dx
      ny = y + dy

      if inBounds(nx,ny) and grid[nx][ny] == 0:
        grid[nx][ny] = grid[x][y] +1
        q.append([nx,ny])
  return -1

print(shortestPathBinaryMatrix([[0,0,1,1,0,0], 
                                [0,0,0,0,1,1], 
                                [1,0,1,1,0,0], 
                                [0,0,1,1,0,0], 
                                [0,0,0,0,0,0], 
                                [0,0,1,0,0,0]]))