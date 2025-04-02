'''
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You want to return the least number of bricks that you'll need to cut through.


EXAMPLE(S)

[[1,2,2,1],   
[3,1,2],       
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]] => 2


 sum.  =     5 
        [1,2,2,1]

map[sum-1]

{
0:2
1:1
2:2
5:3
6:5
}

map = 
  0 1 2 3 4
 1_1_1_1_1_1

func minBricks(input: [[Int]]) -> Int
'''

def minBricks(wall):
    spaces = {}

    largestCount = 0

    for line in wall:
        # Skip the last brick in each row
        # to avoid counting the right edge of the wall
        # as a space.
        space = 0
        for bwidth in range(len(line)-1):
            space += line[bwidth]
            spaces[space] = current = spaces.get(space, 0) + 1
            
            if current > largestCount:
                largestCount = current

    
    return len(wall) -  largestCount

print(minBricks([[1,2,2,1],   
[3,1,2],       
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]] ))


'''

# Formation Solution 

def leastBricks(self, wall: List[List[int]]) -> int:
    edges, maxEdges = defaultdict(int), 0
    for row in wall:
        for idx in accumulate(row[:-1]):
            edges[idx] += 1
            maxEdges = max(maxEdges, edges[idx])
    return len(wall) - maxEdges
'''