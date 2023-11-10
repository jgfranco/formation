"""

Matrix horizontal flip
"""

def horizontalFlip(matrix):

  """
  turn:
  1,2,3
  4,5,6
  7,8,9

  into:
  7,8,9
  4,5,6
  1,2,3
  """

  if len(matrix) == 1: return matrix

  top = 0
  bottom = len(matrix)-1

  while top < bottom:
    matrix[top], matrix[bottom] = matrix[bottom], matrix[top]

    top +=1
    bottom -=1
  
  return matrix

print(horizontalFlip([[1,2,3],[4,5,6],[7,8,9]]))

def verticalFlip(matrix):

  """
  turn:
  1,2,3
  4,5,6
  7,8,9

  into:
  3,2,1
  6,5,4
  9,8,7
  """
  if len(matrix[0]) ==1: return matrix
  left = 0
  right = len(matrix[0])-1

  while left < right:
    for row in range(len(matrix)):
      matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
    left +=1
    right -=1
  return matrix

print(verticalFlip([[1,2,3],[4,5,6],[7,8,9]]))