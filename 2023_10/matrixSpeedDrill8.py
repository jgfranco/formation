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
        for j in range(len(m[0])- counter):
            s += m[i][j]            
        counter +=1
    
    return s

"""
Q. Given a square matrix with each row sorted and consist of either 0 or 1, return the index of the first row from the top with the minimum positive number of 1s. If no rows have even a single 1, return -1.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] integer

[Python 3] Syntax Tips
"""
def solution(m):
    sumMap = {}
    
    for i in range(len(m)):
        sum = 0
        for j in range(len(m[0])):
            sum += m[i][j]
        #if sum ==0: continue
        if sum in sumMap:
            sumMap[sum].append(i)
        else:
            sumMap[sum] = [i]
    
    sortedMap = sorted(sumMap.items(), key= lambda x: x[0])
    print(sortedMap)
    if sortedMap[0][0] == 0:
        if len(sortedMap) ==1: return -1
        else: del sortedMap[0]
    return sortedMap[0][1][0]

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

    if r*c != len(m) * len(m[0]): return m
    
    newMatrix = [[0 for i in range(c)] for i in range(r)]
    
    row = 0
    col = 0
    for i in range(r):
        for j in range(c):
            newMatrix[i][j] = m[row][col]
            if col +1 < len(m[0]):
                col +=1
            else:
                row +=1
                col = 0
    
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

"""
def solution(m):

    middle = len(m)//2
    
    sum = 0
    for i in range(len(m)):
        sum += m[i][middle]
        sum += m[middle][i]

    return sum - m[middle][middle]

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
    if m == []: return []
    if len(m[0]) == 0: return m
    rows = len(m)
    cols = len(m[0])
    
    newMatrix = [[0 for i in range(rows)] for j in range(cols)]
    

    for i in range(len(newMatrix)):
        for j in range(len(newMatrix[0])):
            newMatrix[i][j] = m[j][-i-1]
       
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

"""
def solution(a, m, n):
    if m*n != len(a): return []
        
    array = [[0 for i in range(n)] for j in range(m)]
    pointer = 0
    for i in range(m):
        for j in range(n):
            array[i][j] = a[pointer]
            pointer +=1
            
    return array