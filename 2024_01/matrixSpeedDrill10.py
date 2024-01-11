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
"""

def solution(m):
    if len(m) ==0 or len(m[0]) == 0: return m

    newMatrix = [[0 for _ in range(len(m))] for _ in range(len(m[0]))]
    print(newMatrix)
    for row in range(len(newMatrix)):
        for col in range(len(newMatrix[0])):
            newMatrix[row][col] = m[col][-row-1]
            
    return newMatrix


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

[output] array.array.integer"""

def solution(a, m, n):

    if m*n != len(a): return []
    
    newMatrix = [[0 for _ in range(n)] for _ in range(m)]
    
    pointer = 0
    print(newMatrix)
    for row in range(len(newMatrix)):
        for col in range(len(newMatrix[0])):
            newMatrix[row][col] = a[pointer]
            pointer +=1
            
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

[Python 3] Syntax Tips
"""


def solution(m):

    counter =0
    sum = 0
    for row in range(len(m)):
        for col in range(len(m[0])- counter):
           sum += m[row][col]
        counter +=1
    return sum 
            