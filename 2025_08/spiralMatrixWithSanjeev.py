

def spiralOrder(matrix: list[list[int]]) -> list[int]:

    result = []
    left = top = 0
    right = len(matrix[0]) - 1
    bottom = len(matrix) - 1

    dir = 0
    while left<=right and top<= bottom:

        if dir == 0: # go right
            for i in range(left, right +1):
                result.append(matrix[top][i])
            top +=1
        if dir == 1: # go down
            for i in range(top, bottom +1):
                result.append(matrix[i][right])
            right  -=1
        if dir == 2: # go left
            for i in range(right, left -1, -1):
                result.append(matrix[bottom][i])
            bottom  -=1
        if dir == 3: # go up
            for i in range(bottom, top -1, -1):
                result.append(matrix[i][left])
            left  += 1

        dir = (dir + 1) % 4

    return result


m = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

m2 = [
    [1,2],
    [3,4],
    [5,6]
]

m3= [
  [1, 2, 3],
  [4, 5, 6]
]

m4 = [
    [1],
    [3],
    [5]
]

m5= [
  [1, 2, 3]
]
print(spiralOrder(m), [1, 2, 3, 6, 9, 8, 7, 4, 5])
print(spiralOrder(m2), [1, 2, 4, 6, 5, 3])
print(spiralOrder(m3), [1, 2, 3, 6, 5, 4])
print(spiralOrder(m4), [1, 3, 5])
print(spiralOrder(m5), [1, 2, 3])
print(spiralOrder([[1]]), [1])

