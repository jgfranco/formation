"""Q. Given a matrix, row r, and column c, generate a new matrix of a new size rxc, filling it with the original elements in the same row-traversing order. If the new matrix does not have the same total capacity, then return the original matrix.

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
    R = len(m)
    C = len(m[0])
    if r*c != R*C: return m
    
    newMatrix = [[0 for i in range(c)] for j in range(r)]
    
    R = 0
    C = 0
    for row in range(r):
        for col in range(c):
            newMatrix[row][col] = m[R][C]
            if C+1 >= len(m[0]):
                R +=1
                C = 0
                continue
            C+=1
        
    return newMatrix

"""Note: Your solution should only use O(1) additional memory, since that's what you'll be asked to do during an interview.

Given a matrix of integers m, rotate it by 180 degrees.

Example

For

m = [[1, 2, 3, 4],
     [5, 6, 7, 8]]
the output should be

solution(m) = [[8, 7, 6, 5],
                      [4, 3, 2, 1]]
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

Guaranteed constraints:
0 ≤ m.length ≤ 1000,
0 ≤ m[i].length ≤ 1000,
m[i].length = m[j].length,
-1000 ≤ m[i][j] ≤ 1000.

[output] array.array.integer

Return m rotated by 180 degrees.

"""

def solution(m):
    for row in range(len(m)):
        m[row] = m[row][::-1]
    
    return m[::-1]

"""Q. Given a matrix, flip it horizontally.

Examples:

Given:

[
    [1, 2],
    [3, 4]
]
returns:

[
    [3, 4],
    [1, 2]
]
Given:

[
    [1, 2]
]
returns:

[
    [1, 2]
]
Given:

[
    [1, 2],
    [3, 4],
    [5, 6]
]
returns:

[
    [5, 6],
    [3, 4],
    [1, 2]
]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer matrix

[output] array.array.integer
"""

def solution(matrix):  
    return matrix[::-1]

"""Q. Given a square matrix of integers, return the sum of all edges. Do not count the same element more than once.

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

[output] integer"""


def solution(m):

    left = 0
    right = len(m[0])-1
    top = 0
    bottom = len(m) -1
    sum = 0
    for row in range(len(m)):
        for col in range(len(m[0])):
            if row == top or row == bottom or col == left or col == right:
                sum += m[row][col]
                
    return sum

"""Q. Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in horizontal zigzag order (see examples below) starting from the top left element

Examples:
Input1:
[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
Output1:
[1, 2, 3, 6, 5, 4, 7, 8, 9]
Input2:
[
[1, 2, 3],
[4, 5, 6]
]
Output2: [1, 2, 3, 6, 5, 4]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] array.integer


"""

def solution(m):

    forward = True
    result = []
    for row in range(len(m)):
        for col in range(len(m[0])):
            if forward:
                result.append(m[row][col])
            else:
                result.append(m[row][-col-1])
        forward = not forward
    return result

"""Q. Given a matrix, determine if it is a Toeplitz Matrix (a matrix where all elements from the top-left to bottom-right are the same for each diagonal line).

Examples:
Given:

[
    [1, 2],
    [3, 1]
]
returns true

Given:
[
   [1, 2, 3, 4],
   [5, 1, 2, 3],
   [9, 5, 1, 2]
]

returns true

Given:

[
   [1, 2, 3, 4],
   [5, 1, 5, 3],
   [9, 5, 1, 2]
]
returns false

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] boolean


"""

def solution(m):
    rows = len(m)
    cols = len(m[0])
    
    for i in range(rows-1):
        for j in range(cols -1):
            if m[i][j] != m[i+1][j+1]:
                return False
    
    return True

