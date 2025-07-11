
'''
Number Of Islands

Given a 2d grid map of `1`'s (land) and `0`'s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
 

EXAMPLE(S)
Input:
11110
11010
11000
00000

Output: 1

Input:
11000
11000
00100
00011

Output: 3

edge cases:

- all water
- one island

explore
- input array can be modified
- 

brainstorm:
intializeislandCount variable
iterate through the whole array
    once we hit a 1 (island)
    increment islandoCount
    explore the island recursively using bfs
        use a set to store explored coordinates
    
 "" - 

 cccccc
r000001
r000001
r000000
r100001
 

FUNCTION SIGNATURE
function numIslands(grid)
def numIslands(grid):
'''



def numIslands(grid):
    def bfs(grid,r,c):
         
        nonlocal visitedIsland
        # discard out of bounds coordinates
        if r < 0 or r == len(grid):
            return
        if c < 0 or c == len(grid[0]):
            return

        if (r,c) not in visitedIsland and grid[r][c]  == 1:
            visitedIsland.add((r,c))
            #left
            bfs(grid,r, c + 1)

            #up
            bfs(grid,r + 1,c)

            #right
            bfs(grid,r, c - 1)
    

            #down
            bfs(grid,r - 1,c)
        
        return 

    
    intializeislandCount  = 0
    visitedIsland = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            # check if current r and c is visited
            if (r,c) not in visitedIsland and grid[r][c] == 1:
                intializeislandCount += 1
                bfs(grid, r, c)

                

                
    
    return intializeislandCount
            #check left,right,up down using recursion
    


grid1 = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]
print(numIslands(grid1), 3)


grid2 = [
    [1,1,1,1,0],
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,0,0]
]
print(numIslands(grid2), 1)