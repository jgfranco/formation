
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
    def bfs(r,c):
        # discard out of bounds coordinates
        if r< 0 or r>= len(grid) or c< 0 or c>= len(grid[0]):
            return
        
        neighbourLand = [[0,1],[0,-1],[1,0],[-1,0]]

        # check if we are in land
        if grid[r][c] == 1:

            #flood this portion of the island
            grid[r][c] = 0

            #explore the island
            for dr,dc in neighbourLand:
                bfs(r+dr, c+dc)
        
        return
          

    islandCount = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                islandCount += 1
                bfs(r, c)
    return islandCount
    


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

grid3 = [
    [1,0,0,0,1],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,0,0,0,1]
]
print(numIslands(grid3), 4)