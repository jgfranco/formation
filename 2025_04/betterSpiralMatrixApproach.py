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
'''

def spiralOrder(matrix: list[list[int]]) -> list[int]:
    result = []
    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1

    direction = 0

    while left <= right and top <= bottom:
        if direction == 0: # right
            for i in range(left, right +1):
                result.append(matrix[top][i])
            top += 1
        if direction == 1: #down
            for i in range(top, bottom +1):
                result.append(matrix[i][right])
            right -= 1
        if direction == 2: # left
            for i in range(right, left -1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if direction == 3: # up
            for i in range(bottom, top -1, -1):
                result.append(matrix[i][left])
            left += 1

        direction = (direction + 1) % 4

    return result


# tests

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