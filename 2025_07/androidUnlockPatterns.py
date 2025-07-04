'''
Given a 3x3 lock screen in the following arrangement:

1 2 3
4 5 6
7 8 9

count the total number of unlock patterns that use N numbers.

A pattern is valid if the following criteria are met:
- no number is used more than once
- a path from one number to another does not directly pass through an unused number. eg:
  - 2 -> 1 -> 3 is valid, but 1 -> 3 is not valid because it directly passes through the unused number 2

NOTE: It is possible to go from 2 to 9 (or 3 to 4) because the pattern may move between rows and colunns on diagonals.
 

 9PN = 9! (9-N!) / N!

 9CN

EXAMPLE(S)
1 2 3
4 5 6
7 8 9

4 -> 1 -> 3 -> 6 is invalid because 1 -> 3 passes through the unused 2

2 -> 4 -> 1 -> 3 -> 6 is valid
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 is valid
3 -> 4 is valid
1's neighbors are 2,4,5,6,8
2's are 1,3,4,5,6,7,9
3's are 2,5,8,6,4
4's are 1,2,3,5,7,8,9
5's are 1,2,3,4,6,7,8,9
6's are 1,2,3,5,7,8,9
7's are 4,2,5,8,6

use a set to account for visited numbers

notNeighborMap = {1: [3,]}

path: currently visited numbers
base case:
    once numberOfKeys match length of path, then we copy path into the result array
in each iteration, we choose from 1-9, use blocks and visited to prune nonvalid nodes

FUNCTION SIGNATURE
function countPatterns(numberOfKeys) {
def countPatterns(numberOfKeys: int) -> int:
'''

blocks = [
        [],
        [0, 0, 0, 2, 0, 0, 0, 4, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 2, 0, 0, 0, 0, 0, 5, 0, 6],
        [0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 4, 0, 5, 0, 0, 0, 0, 0, 8],
        [0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 6, 0, 0, 0, 8, 0, 0],
]

def countPatterns(numberOfKeys: int) -> int:
    solutions = 0
    solArray = []
    path = []
    visited = set()

    def helper(start):
        nonlocal solutions

        if len(path) == numberOfKeys:
            solutions +=1
            solArray.append(path.copy())
            return solutions
      
        for i, option in enumerate(blocks[start]):
            if i == 0: continue
            if option == 0 or option in visited:
                path.append(option)
                visited.add(option)
                helper(option)
                path.pop(-1)
                visited.discard(option)
        
        return solutions
            


    corner = helper(1)
    center = helper(2)
    middle = helper(5)
    total = (4 * corner) + (4 * center) + middle
    print(solArray)
    return total

print(countPatterns(1))