"""
Q. Given a matrix, determine if it is a Toeplitz Matrix (a matrix where all elements from the top-left to bottom-right are the same for each diagonal line).

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
"""

def solution(m):

    for row in range(len(m)-1):
        for col in range(len(m[0])-1):
            if m[row][col] != m[row+1][col+1]:
                return False
            
    return True
  

"""
Q. Given a square matrix of integers, return the sum except the numbers on the outer edges.

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

[output] integer
"""

def solution(m):

    left = 0
    right = len(m[0]) -1
    top = 0
    bottom = len(m) -1
    s = 0
    for row in range(len(m)):
        for col in range(len(m[0])):
            if row == top or row == bottom or col == left or col == right: continue
            s += m[row][col]
        
        
    return s

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


"""
Q. Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order (counter-clockwise) starting from the top left element

Examples:
Input1:
[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
Output1:
[1, 4, 7, 8, 9, 6, 3, 2, 5]
Input2:
[
[1, 2, 3],
[4, 5, 6]
]
Output2: [1, 4, 5, 6, 3, 2]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] array.integer
"""


def solution(m):
    if m == []: return []

    left = 0
    right = len(m[0])-1
    top= 0
    bottom = len(m) -1
    result = []
    
    while left < right and top < bottom: 
        # go down
        for i in range(top, bottom):
            result.append(m[i][left ])
        # go right
        for i in range(left, right):
            result.append(m[bottom][i])
        # go up
        for i in range(bottom, top, -1):
            result.append(m[i][right])
        # go left    
        for i in range(right, left, -1):
            result.append(m[top][i])
            
        left +=1
        right -=1
        top +=1
        bottom -=1
        
    if left == right and top == bottom:
        result.append(m[left][bottom])
    elif left == right:
        for i in range(top, bottom+1):
            result.append(m[i][left])
    elif top == bottom:
        for i in range(left, right+1):
            result.append(m[top][i])
    return result

"""Q. Given two square matrices m and target, determine if m can become target by rotating it in either direction (clockwise or counter-clockwise).

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
    full = True
    ccw = True
    for row in range(len(m)): # 0
        for col in range(len(m[0])): # 0,1
            if m[row][col] != target[col][-row-1]:
                cw = False
            if m[row][col] != target[-row-1][-col-1]:
                full = False
            if m[row][col] != target[-col-1][row]:
                ccw = False
            
    return cw or full or ccw


"""
Question 6 of 6
1:21:59

Q. Given a square matrix with a minimum length of 2 on each side, sum top right triangular portion.

Example 1:

Given:
[  [6, 4, 7],
   [1, 3, 2],
   [8, 9, 5]  ]
returns: 27 (6+4+7+3+2+5)

Explanation: The top right triangular portion is:

[  [6, 4, 7],
   [   3, 2],
   [      5]  ]
Example 2:

Given:
[  [6, 4, 7, 1],
   [1, 3, 2, 2],
   [0, 0, 5, 2],
   [8, 9, 5, 3]  ]
returns: 35

Explanation: The top right triangular portion is:

[  [6, 4, 7, 1],
   [   3, 2, 2],
   [      5, 2],
   [         3]  ]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] integer
""" 

def solution(m):

    s = 0
    column = 0
    for row in range(len(m)):
        for col in range(column, len(m[0])):
            s += m[row][col]
        column +=1
        
    return s