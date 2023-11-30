"""Given a square matrix of integers, return the sum of the elements along the two major diagonals, top left to bottom right and top right to bottom left. Do not count the same index more than once.

Example:
Input:
[[1,2,3],
[4,5,6],
[7,8,9]]

Output: 25
Explanation: 1 + 5 + 9 + 3 + 7 = 25 (note that 5 is not counted twice).

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] integer

"""
def solution(m):
    if len(m) == 0: return 0
    
    sum = 0
    
    for i in range(len(m)):
        sum += m[i][i] + m[i][-i-1]

    mid = len(m)//2 
    if len(m) %2 != 0:
        return sum - m[mid][mid]
        
    return sum


"""
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

    start =0 
    sum =0
    
    for row in range(len(m)):
        for col in range(start, len(m[0])):
            sum += m[row][col]
        
        start +=1
        
    return sum


"""Q. Given a square matrix with each row sorted and consist of either 0 or 1, return the index of the first row from the top with the minimum positive number of 1s. If no rows have even a single 1, return -1.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[output] integer"""


def solution(m):
    if len(m) == 0: return -1
    if len(m[0]) == 0: return -1
    map = {}
    
    for row in range(len(m)):
        for col in range(len(m[0])):
            map[row] = map.get(row, 0) + m[row][col]
                
                
                
    idx = -1
    count = float("inf")
    for k,v in map.items():
        if v ==0:
            continue
        if v < count:
            count = v
            idx = k
            
            
    return idx


"""You are given a rectangular matrix m. Your goal is to write a program that, if an element of m is equal to 0, sets that element's entire row and column to 0.

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

[output] array.array.integer"""


def solution(m):

    
    visited = set()
    
    def setToZeroes(row,col):
        
        for r in range(len(m)):
            for c in range(len(m[0])):
                if r == row or c == col:
                    m[r][c] = 0
                    visited.add((r,c))
                

    for row in range(len(m)):
        for col in range(len(m[0])):
            
            if (row,col) not in visited and m[row][col] ==0:
                setToZeroes(row,col)
                
    return m
                
           

"""Q. Given a square matrix with a minimum odd length of 3 on each side, sum numbers in cross positions.

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

[output] integer"""


def solution(m):
    mid = len(m)//2

    sum = 0
    for row in range(len(m)):
        for col in range(len(m[0])):
            
            if row == mid or col == mid:
                sum += m[row][col]
                
    
    return sum
          
 
           
