# /*
# '''
# Today, you will be given the problem of the Brick Wall:

# Source: https://leetcode.com/problems/brick-wall/description/

# There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.
# The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.
# If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

# You want to return the least number of bricks that you'll need to cut through.
 

# EXAMPLE(S)
# [[1,2,2,1]
# [3,1,2],
# [1,3,2],
# [2,4],
# [3,1,2],
# [1,3,1,1]] => 2

"""

{
    1: 1
    3: 1
    5: 1
}

rows - edge with largest count
  
 _1_2_3_4_5_
 _ ___ ___ _ , 1: 1
 _____ _ ___
 _ _____ ___
 ___ _______
 _____ _ ___
 _ _____ _ _



 initialize a map of edges
 edgeWithlargestCount

 traverse the rows:
    for each row: 
        update map: increment the count for the current space. Space is defined as the sum of widths so far

        update the edge with largest count if larger


return len of our input - edge with largest count

 """


# FUNCTION SIGNATURE
# func minBricks(input: [[Int]]) -> Int
# '''
# */


def minBricks(wall):

    edges = {}
    leastBlockedEdge = float("-inf")

    for row in wall:
        edge = 0
        for i,w in enumerate(row):

            if i == len(row) - 1: continue
            edge += w 
            edges[edge] = edges.get(edge, 0) + 1

            leastBlockedEdge = max(leastBlockedEdge, edges[edge])

    print()
    return len(wall) - leastBlockedEdge


wall = [[1,2,2,1],
[3,1,2],
[1,3,2],
[2,4],
[3,1,2],
[1,3,1,1]]

print(minBricks(wall))

"""
formation solution
def leastBricks(self, wall: List[List[int]]) -> int:
	edges, maxEdges = defaultdict(int), 0
	for row in wall:
		for idx in accumulate(row[:-1]):
			edges[idx] += 1
			maxEdges = max(maxEdges, edges[idx])
	return len(wall) - maxEdges

"""
