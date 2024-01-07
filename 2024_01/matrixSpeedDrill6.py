"""Q. Given a zero-indexed array a and integers m and n, construct a mxn matrix with array a's elements in the order they appear, filling the top rows first. If a matrix cannot be generated, return an empty matrix [].
**
Examples:
**

Input: a = [1, 2, 3, 4], m = 2, n=2
Output:
[
    [1, 2],
    [3, 4]
]
Input: a = [1, 2, 3, 4], m = 3, n=2
Output:
[
]
Input: a = [1, 2, 3, 4], m = 4, n=1
Output:
[
    [1],
    [2],
    [3],
    [4]
]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer a

[input] integer m

[input] integer n

[output] array.array.integer
"""
def solution(a, m, n):
    if m *n != len(a): return []
    
    newMatrix = [[0 for _ in range(n)] for _ in range(m)]
    
    row = col = 0
    print(newMatrix)
    pointer = 0
    while pointer < len(a):
        print(pointer, row, col)
        newMatrix[row][col] = a[pointer]
        col +=1
        if col == len(newMatrix[0]):
            row += 1
            col = 0
        pointer +=1
        
    return newMatrix


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
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] array.array.integer

Return m rotated by 90 degrees.

"""


def solution(m):
    if len(m) == 0 or len(m[0]) == 0: return m

    newMatrix = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    
    for row in range(len(newMatrix)):
        for col in range(len(newMatrix[0])):
            newMatrix[row][col] = m[-col-1][row]
            
    return newMatrix


"""
You are given a rectangular matrix m. Your goal is to write a program that, if an element of m is equal to 0, sets that element's entire row and column to 0.

Example

For

m = [[1, 0, 2, 3],
     [4, 5, 6, 7],
     [8, 9, 10, 0]]
the output should be

solution(m) = [[0, 0, 0, 0],
                    [4, 0, 6, 0],
                    [0, 0, 0, 0]]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

Guaranteed constraints:
1 ≤ m.length ≤ 100,
1 ≤ m[i].length ≤ 100,
-1000 ≤ m[i][j] ≤ 1000.

[output] array.array.integer
"""

def solution(m):

    visited = set()
    
    def setToZeroes(r, c):
        
        for row in range(len(m)):
            for col in range(len(m[0])):
                if row == r or col == c:
                  
                    m[row][col] = 0
                    visited.add((row, col))
    
            
    for row in range(len(m)):
        for col in range(len(m[0])):
            if m[row][col] ==0 and (row, col) not in visited:
                setToZeroes(row,col)
                
    return m

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

    position = len(m[0]) - 1
    sum = 0
    
    for row in range(len(m)):
        for col in range(position, len(m[0])):
            sum += m[row][col]
        position -=1
        
    return sum

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

    maxIdx = -1
    maxSum = 0
    for row in range(len(m)):
        rowSum  = sum(m[row])
        if rowSum > maxSum:
            maxSum = rowSum
            maxIdx = row+1
        
    return maxIdx

"""
Q. Given two matrices, multiply them using the dot product (under "Multiplying a Matrix by Another Matrix") of rows and columns.

Example

For

matrix1 = [[1, 1, 1],
           [0, 0, 0]]
and

matrix2 = [[2, 1],
           [1, 2],
           [2, 1]]
the output should be

matrixMultiplication(matrix1, matrix2) = [[5, 4],
                                          [0, 0]]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer matrix1

2-dimensional array of integers representing a matrix.

Guaranteed constraints:
1 ≤ matrix1.length ≤ 100,
1 ≤ matrix1[0].length ≤ 100,
matrix1[0].length = matrix1[i].length,
0 ≤ matrix1[i][j] ≤ 10.

[input] array.array.integer matrix2

2-dimensional array of integers representing a matrix. Number of columns in matrix1 is equal to the number of rows in matrix2.

Guaranteed constraints:
matrix2.length = matrix1[0].length,
1 ≤ matrix2[0].length ≤ 100,
matrix2[0].length = matrix2[i].length,
0 ≤ matrix2[i][j] ≤ 10.

[output] array.array.integer

2-dimensional array of integers representing the product of matrix1 and matrix2."""



def solution(matrix1, matrix2):
    
    newMatrix = [[0 for _ in range(len(matrix2[0]))] for _ in range( len(matrix1))]

    for i in range(len(newMatrix)):
        for j in range(len(newMatrix[0])):
            for x in range(len(matrix1[0])):
  
                newMatrix[i][j] += matrix1[i][x] * matrix2[x][j]
                
            
    return newMatrix
            


