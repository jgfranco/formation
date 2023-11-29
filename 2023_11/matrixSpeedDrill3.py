"""
Q. Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in vertical zigzag order (see examples below) starting from the top left element

Examples:
Input1:
[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
Output1:
[1, 4, 7, 8, 5, 2, 3, 6, 9]
Input2:
[
[1, 2, 3],
[4, 5, 6]
]
Output2: [1, 4, 5, 2, 3, 6]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] array.integers
"""

def solution(m):
    if len(m) == 0: return m
    result = []
    down = True
    for col in range(len(m[0])):
        for row in range(len(m)):
            if down:
                result.append(m[row][col])
            else:
                result.append(m[-row-1][col])
        down = not down
            
    return result


"""Q. Given a square matrix of integers, return the sum except the numbers on the outer edges.

Example:
Input1:

[  [1,2,3],
   [4,5,6],
   [7,8,9]  ]
Output1: 5

Input2:

[   [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13,14, 15, 16]  ]
Output2: 34
Explanation: 6+7+10+11

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] integer"""


def solution(m):

    left = 0
    right = len(m[0]) -1
    top = 0
    bottom = len(m) -1
    result = 0
    for row in range(len(m)):
        for col in range(len(m[0])):
            if row != top and row != bottom and col != left and col != right:
                result += m[row][col]
    return result


"""Given a square matrix of integers, sort it in ascending order.

Example:

Given:
[  [6, 4, 7],
   [1, 3, 2],
   [8, 9, 5]  ]
returns:
[  [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]  ]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] array.array.integer

[Python 3] Syntax Tips"""

def solution(m):

    val = 1
    for row in range(len(m)):
        for col in range(len(m[0])):
            m[row][col] = val
            val +=1
    return m

"""Q. Given a square matrix with each row sorted and consist of either 0 or 1, find the first row from the top with the maximum number of 1s. If none, return -1. Return the ordinal of the row, so if the first row is the answer, return 1.

For example:

[
  [0, 0, 1],
  [0, 1, 1],
  [0, 1, 1]
]
Returns 2.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] integer

"""

def solution(m):
    
    max = -1
    maxSum = 0
    
    for row in range(len(m)):
        sum = 0
        for col in range(len(m[0])):
            sum += m[row][col]
        
        if sum > 0 and sum > maxSum:
            max = row
            maxSum = sum
    
    if maxSum == 0: return -1
    return max +1


"""Given a matrix of integers m, rotate it by 90 degrees counterclockwise.

Example

For

m = [[1, 2, 3, 4],
     [5, 6, 7, 8]]
the output should be

rotateMatrix180(m) = [[4, 8],
                      [3, 7],
                      [2, 6],
                      [1, 5]]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] array.array.integer

Return m rotated by 90 degrees."""
    

def solution(m):
    if len(m) == 0 or len(m[0]) == 0: return m
    newMatrix = [[0 for i in range(len(m))] for j in range(len(m[0]))]


    for row in range(len(newMatrix)):
        for col in range(len(newMatrix[0])):
            newMatrix[row][col] = m[col][-row-1]
            
    return newMatrix
            

"""Q. Given a m x n matrix of integers, determine if it is a square matrix (i.e. m equals n).

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] boolean

"""


def solution(m):

    return len(m) == len(m[0])
            