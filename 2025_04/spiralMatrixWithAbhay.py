'''
Given a matrix, return an array representing the traversal of the matrix in spiral order. Starting in the top left, move right, then down, then left, then up, and then progress inward.

Some problems are "tricky" ones where you have to notice something clever. Sometimes, however, problems are all about demonstrating mastery of your language and being able to manipulate basic data structures. This problem is all about mastering basic counting loops and strategically moving around a 2-dimensional matrix.
 

EXAMPLE(S)
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
// returns [1, 2, 3, 6, 9, 8, 7, 4, 5]
 

FUNCTION SIGNATURE
function spiralOrder(matrix) { // returns a 1D array
def spiralOrder(matrix: list[list[int]]) -> list[int]:

Explore:
- can be a non square matrix
- 

Brainstorm:
- define left, right top, bottom
left= 0
right = 2 len(row) -1
top = 0
bottom = 2

# go right          0, 1
     for i in range(left, right)
     reg for loop (left, right -1)

# go down

# go left

# go up


    shrink our edges
    left +=1
    right -=1
    top ++
    bottom --
    
   l./t   r
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9] 
   b
]

let matrix5 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16]
]

Plan:

'''


def spiralOrder(matrix):

    left = 0
    right = len(matrix[0]) -1
    top = 0
    bottom = len(matrix) - 1

    result = []
    
    while left < right and top < bottom:
        # go right
        for i in range(left, right):
            result.append(matrix[top][i])

        # go down
        for i in range(top, bottom):
            result.append(matrix[i][right])

        # go left
        for i in range(right, left, -1):
            result.append(matrix[bottom][i])

        # go up
        for i in range(bottom, top, -1):
            result.append(matrix[i][left])

        
        #shrink edges
        left += 1
        right -=1 
        top += 1
        bottom -=1
    
    if left == right and top == bottom: result.append(matrix[left][top])
    elif top == bottom:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
    elif left == right:
        for i in range(top, bottom + 1):
           result.append(matrix[i][left])

    
    
    return result


# matrix1 = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]



# matrix5 = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12],
#   [13,14,15,16]
# ]

# matrix2 = [
#   [1, 2, 3],
#   [5, 6, 7],
#   [9,10,11],
#   [13,14,15]
# ]

# matrix4 = [
#   [1, 2, 3]
# ]

# matrix6 = [
#   [1],
#   [2],
#   [3]
# ]

# matrix7 = [
#   [1]
# ]


# print(spiralOrder(matrix1))
# print(spiralOrder(matrix5))
# print(spiralOrder(matrix2))
# print(spiralOrder(matrix4))
# print(spiralOrder(matrix6))
# print(spiralOrder(matrix7))
#print(spiralOrder)

print(spiralOrder([[1]]) == [1])

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spiralOrder(matrix1) == [1, 2, 3, 6, 9, 8, 7, 4, 5])

matrix2 = [
    [1, 2],
    [3, 4]
]
print(spiralOrder(matrix2) == [1, 2, 4, 3])

matrix3 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]
print(spiralOrder(matrix3) == [1, 2, 3, 4, 8, 7, 6, 5])

matrix4 = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]
print(spiralOrder(matrix4) == [1, 2, 4, 6, 8, 7, 5, 3])

matrix5 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(spiralOrder(matrix5) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10])

matrix6 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print(spiralOrder(matrix6) == [1, 2, 3, 4, 5, 10, 15, 20, 25, 24, 23, 22, 21, 16, 11, 6, 7, 8, 9, 14, 19, 18, 17, 12, 13])

matrix7 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(spiralOrder(matrix7) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    output = []
    rmin = 0
    rmax = len(matrix) - 1
    cmin = 0
    cmax = len(matrix[0]) - 1

    direction = 0
    while rmin <= rmax and cmin <= cmax:
        if direction == 0:  # across
            for c in range(cmin, cmax + 1):
                output.append(matrix[rmin][c])
            rmin += 1
        elif direction == 1:  # down
            for r in range(rmin, rmax + 1):
                output.append(matrix[r][cmax])
            cmax -= 1
        elif direction == 2:  # across in reverse
            for c in range(cmax, cmin - 1, -1):
                output.append(matrix[rmax][c])
            rmax -= 1
        elif direction == 3:  # up
            for r in range(rmax, rmin - 1, -1):
                output.append(matrix[r][cmin])
            cmin += 1
        direction = (direction + 1) % 4

    return output


