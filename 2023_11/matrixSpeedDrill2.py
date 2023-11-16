"""
Q. Given a m x n matrix of integers, determine if it is a square matrix (i.e. m equals n).

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] boolean
"""

def solution(m):

    return len(m) == len(m[0])

"""
Q. Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in horizontal zigzag order (see examples below) starting from the top left element

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
    newMatrix = [[0 for i in range(len(m))] for j in range(len(m[0]))]
    
    for row in range(len(newMatrix)):
        for col in range(len(newMatrix[0])):
            
             newMatrix[row][col] = m[-col-1][row]

    return newMatrix

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
     
    if m == []:
        return m
    
    left = 0
    right = len(m[0]) -1
    top = 0
    bottom = len(m) -1
    result = []
    
    print(left, right, top, bottom )
    
    while left< right and top <bottom:
        
        #go down
        for i in range(top, bottom):
            result.append(m[i][left])
        #go right
        for i in range(left, right):
            result.append(m[bottom][i])
        
         # go up
        for i in range(bottom, top, -1):
            result.append(m[i][right])
        
        #go left 
        for i in range(right, left, -1):
            result.append(m[top][i])
        
       
            
        left += 1
        right -= 1
        top += 1
        bottom -= 1
        print(left, right, top, bottom )
        
    if left == right and bottom == top:
        result.append(m[left][bottom])
    elif left == right:
        for i in range(top, bottom + 1):
            result.append(m[i][left])
    elif top == bottom:
        for i in range(left, right + 1):
            result.append(m[top][i])
                            
    return result
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
    
    left = 0
    right = len(m[0]) -1
    top = 0
    bottom = len(m) -1
    result = 0
    
    for row in range(len(m)):
        for col in range(len(m)):
            if row == top or row == bottom or col == left or col == right:
                result += m[row][col]
                
    return result

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

"""
def solution(m):

    visited = []
    def setToZero(row,col):
        for i in range(len(m[0])):
            m[row][i]=0
            visited.append((row,i))
            
        for j in range(len(m)):
            m[j][col] = 0
            visited.append((j,col))
        
        
    for row in range(len(m)):
        for col in range(len(m[0])): 
            if (row,col) not in visited and m[row][col]==0:
                setToZero(row,col) 
                
    return m

    