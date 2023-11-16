"""
Q. Given a matrix, flip it horizontally.

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

    if len(matrix) == 1: return matrix
    
    top = 0
    bottom = len(matrix) -1
    
    while top < bottom:
        
        matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
        top +=1
        bottom -=1
        
    return matrix



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
    if len(m) == 0: return m
    if len(m[0]) ==0: return m
    newMatrix = [[0 for i in range(len(m))] for j in range(len(m[0])) ]
    

    for i in range(len(newMatrix)):
        for j in range(len(newMatrix[0])):
            
            newMatrix[i][j] = m[j][-i-1]
            
    return newMatrix

"""
Q. Given a m x n matrix of integers, determine if it is a square matrix (i.e. m equals n).

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] boolean

def solution(m):
    rows = len(m)
    cols = len(m[0])

    return rows == cols

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
    
    matrix = [[0 for i in range(n)] for j in range(m)]
    
    p = 0
    for i in range(m):
        for j in range(n):
            matrix[i][j] = a[p]
            p +=1
            
        
    return matrix


"""
Q. Given two square matrices m and target, determine if m can become target by rotating it in either direction (clockwise or counter-clockwise).

Examples:
Given:
m:

[
    [1, 1],
    [0, 1]
]
target:

[
    [1, 1],
    [1, 0]
]
returns true

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[input] array.array.integer target

[output] boolean
"""
def solution(m, target):
    if m == target: return True
    
    cw = True
    ccw = True
    full = True
    for i in range(len(m)):
        for j in range(len(m[0])):

            if m[i][j] != target[j][-i-1]: cw = False

            if m[i][j] != target[-j-1][i]: ccw =  False
            
            if m[i][j] != target[-j-1][-i-1]: full =  False
             
    print(cw, ccw, full)
    return cw or ccw or full

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
    counter = 0
    
    s = 0
    for i in range(len(m)):
        for j in range(len(m[0]) - counter):
            s += m[i][j]
        
        counter +=1
        
    return s
