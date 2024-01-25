"""
Q. Given a matrix, check if it is a binary matrix. A binary matrix is a matrix in which all the elements are either 0 or 1.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] boolean


"""

def solution(m):
    
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col] >1 or m[row][col] < 0: return False
    
    return True

"""
Given a matrix of integers m, rotate it by 90 degrees clockwise.

Example

For

m = [[1, 2, 3, 4],
     [5, 6, 7, 8]]
the output should be

rotateMatrix180(m) = [[5, 1],
                      [6, 2],
                      [7, 3],
                      [8, 4]]
                      
"""


def solution(m):
    if len(m) == 0 or len(m[0]) == 0: return m

    newMatrix = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    
    for row in range(len(newMatrix)):
        for col in range(len(newMatrix[0])):
            newMatrix[row][col] = m[-col-1][row]
            
    return newMatrix


"""
Q. Given a square matrix of integers, return the sum of all edges. Do not count the same element more than once.

Example:
Input:
[[1,2,3],
[4,5,6],
[7,8,9]]

Output: 40
Explanation: 1 + 2 + 3 + 7+ 8 + 9 + 4+ 6

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] integer
"""

def solution(m):

    top = 0
    bottom = len(m) - 1
    left  = 0
    right = len(m[0]) -1
    edgeSum = 0
    for row in range(len(m)):
        for col in range(len(m[0])):
            if row == top or row == bottom or col == left or col == right:
                edgeSum += m[row][col]
                
                
    return edgeSum

"""
Q. Given a matrix, flip it vertically.

Examples:

Given:

[
    [1, 2],
    [3, 4]
]
returns:

[
    [2, 1],
    [4, 3]
]
Given:

[
    [1, 2]
]
returns:

[
    [2, 1]
]
Given:

[
    [1, 2],
    [3, 4],
    [5, 6]
]
returns:

[
    [2, 1],
    [4, 3],
    [6, 5]
]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer matrix

[output] array.array.integer

"""

def solution(matrix):

    for row in range(len(matrix)):
        matrix[row] = matrix[row][::-1]
        
    return matrix


"""Q. Given a square matrix with a minimum length of 2 on each side, sum bottom right triangular portion.

Example 1:

Given:
[  [6, 4, 7],
   [1, 3, 2],
   [8, 9, 5]  ]
returns: 34 (7 + 3 + 2 + 8 + 9 + 5)

Explanation: The bottom right triangular portion is:

[  [      7],
   [   3, 2],
   [8, 9, 5]  ]
Example 2:

Given:
[  [6, 4, 7, 1],
   [1, 3, 2, 2],
   [0, 0, 5, 2],
   [8, 9, 5, 3]  ]
returns: 37

Explanation: The bottom right triangular portion is:

[  [         1],
   [      2, 2],
   [   0, 5, 2],
   [8, 9, 5, 3]  ]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] integer
"""

def solution(m):

    start = len(m[0]) -1
    sum = 0
    for row in range(len(m)):
        for col in range(start, len(m[0])):
            sum += m[row][col]
        start -=1
    return sum
    
"""

Question 6 of 6
1:39:46

Q. Given a matrix, row r, and column c, generate a new matrix of a new size rxc, filling it with the original elements in the same row-traversing order. If the new matrix does not have the same total capacity, then return the original matrix.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[input] integer r

the number of rows of a new matrix

[input] integer c

the number of columns of a new matrix

[output] array.array.integer
"""

def solution(m, r, c):
    if len(m) * len(m[0]) != r*c: return m
    newMatrix = [[0 for i in range(c)] for _ in range(r)]
    ROW = COL = 0
    print(newMatrix)
    for row in range(r):
        
        for col in range(c):
            print(row,col, ROW,COL)
            newMatrix[row][col] = m[ROW][COL]
            COL +=1
            if COL == len(m[0]):
                COL = 0
                ROW +=1
    return newMatrix

    