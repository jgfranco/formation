"""
Given a matrix of integers m, rotate it by 90 degrees counterclockwise.

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

Return m rotated by 90 degrees.
"""

def solution(m):
    if len(m) == 0 or len(m[0]) ==0: return m
    
    newMatrix = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    print(newMatrix)


    for row in range(len(newMatrix)):
        for col in range(len(newMatrix[0])):
            newMatrix[row][col] = m[col][-row-1]
            
    return newMatrix


"""
Q. Given a zero-indexed array a and integers m and n, construct a mxn matrix with array a's elements in the order they appear, filling the top rows first. If a matrix cannot be generated, return an empty matrix [].
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

    if m*n != len(a): return []
        
    newMatrix = [[0 for _ in range(n)] for _ in range(m)]
    p = 0
    for row in range(len(newMatrix)):
        for col in range(len(newMatrix[0])):
            newMatrix[row][col] = a[p]
            p +=1
    return newMatrix



"""
Q. Given a square matrix with a minimum length of 2 on each side, sum top left triangular portion.

Example 1:

Given:
[  [6, 4, 7],
   [1, 3, 2],
   [8, 9, 5]  ]
returns: 29 (6+4+7+1+3+8)

Explanation: The top left triangular portion is:

[  [6, 4, 7],
   [1, 3   ],
   [8      ]  ]
Example 2:

Given:
[  [6, 4, 7, 1],
   [1, 3, 2, 2],
   [0, 0, 5, 2],
   [8, 9, 5, 3]  ]
returns: 32

Explanation: The top left triangular portion is:

[  [6, 4, 7, 1],
   [1, 3, 2   ],
   [0, 0      ],
   [8         ]  ]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] integer
"""


def solution(m):

    portion = len(m[0])
    sum = 0
    for row in range(len(m)):
        for col in range(portion):
            sum  += m[row][col]
        portion -=1
        
    return sum

"""
Q. Given a square matrix with each row sorted and consist of either 0 or 1, return the index of the first row from the top with the minimum positive number of 1s. If no rows have even a single 1, return -1.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] integer

[Python 3] Syntax Tips
"""


def solution(m):
    
    result = (-1, float("inf"))
    for i, row in enumerate(m):
        sumRow = sum(row)
        if sumRow > 0 and sumRow < result[1]:
            result = (i, sumRow)
    
    return result[0]


"""
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
    if r * c != len(m) * len(m[0]): return m
    
    newMatrix = [[0 for _ in range(c)] for _ in range(r)]
    
    R = C = 0
    
    for row in range(r):
        for col in range(c):
            newMatrix[row][col] = m[R][C]
            
            C+=1
            if C >= len(m[0]):
                C = 0
                R +=1
    
    return newMatrix

"""
Q. Given a square matrix with a minimum odd length of 3 on each side, sum numbers in cross positions.

Example:

Given:
[  [6, 4, 7],
   [1, 3, 2],
   [8, 9, 5]  ]
returns: 19 (4+3+9+1+2)

Explanation: The cross potion is:

[  [   4   ],
   [1, 3, 2],
   [   9   ]  ]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] integer

[Python 3] Syntax Tips
"""

def solution(m):

    mid = len(m) //2
    sum =0
    for row in range(len(m)):
        for col in range(len(m[0])):
            if row == mid or col == mid:
                sum += m[row][col]
                
    return sum
