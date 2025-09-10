'''
Reversi (https://en.wikipedia.org/wiki/Reversi), also called Othello, is a game where each piece has two sides, black and white, and after being placed, further moves cause other pieces to flip tiles. Specifically, a line of pieces of one color gets flipped when they become surrounded by pieces of the opposite color on both ends.

In this problem, we will be given a 2-dimensional array representing the board. Each position will contain a value of “B”, “W”, or “*” representing empty. Additionally, we get a position that is currently empty. Update the board to the new state after that play, including any flips if it is black’s turn to play. 

You can modify the existing array, but either way, return the board (2d array) with the new state.



EXAMPLE(S)
For example, consider the row:

1 2 3 4 5 6 7 8
* B W W W W * *

If black places a piece at position 7, the white pieces in between get flipped, so the result is:

1 2 3 4 5 6 7 8
* B B B B B B *

This can happen on a row, column, or diagonal and even at the same time. In the following example, if white place on position (5, 5), then all of the black pieces flip to white!
          4
  1 2 3 4 5 6 7 8
1 * * * * * * * *
2 * W * * * * * *
3 * * B * * * * *
4 * * * B * * * *
5 W B B B ! * * *
6 * * * * B * * *
7 * * * * B * * *
8 * * * * W * * *
 

 direction of left =(0, -1)  --> traverse(x, y-1) or while in bounds: ....


Space Complexity: Recursive: O(N)  Iterative O(1)

FUNCTION SIGNATURE
function reversi(board, x, y)
def reversi(board, x, y):



'''

def reversi(board, x, y, color):
  #              N        NW      W     SW     S     SE     E      NE 
  directions = [(0,-1),(-1,-1),(-1,0),(1,-1),(1,0),(-1,1),(0,1), (1,1)]
  dic = {
    'W': 'B',
    'B': 'W'
  }

  board[x][y] = color

  for dx, dy in directions:
    flip = False
    temp_x, temp_y = x+dx, y+dy
    while board[temp_x][temp_y] == dic[color] and temp_x in range(8) and temp_y in range(8):
      temp_x += dx 
      temp_y += dy
    flip = board[temp_x][temp_y] == color

    temp_x, temp_y = x+dx, y+dy 
    while flip and board[temp_x][temp_y] == dic[color] and temp_x in range(8) and temp_y in range(8):
      board[temp_x][temp_y] = color
      temp_x += dx 
      temp_y += dy

  for r in board:
    print(r)

  return board
  
board = [
  ["*", "*", "*", "*", "*", "*", "*", "*"],
  ["*", "W", "*", "*", "*", "*", "*", "*"],
  ["*", "*", "B", "*", "*", "*", "*", "*"],
  ["*", "*", "*", "B", "*", "*", "*", "*"],
  ["B", "W", "W", "W", "W", "*", "*", "*"],
  ["*", "*", "*", "*", "B", "*", "*", "*"],
  ["*", "*", "*", "*", "B", "*", "*", "*"],
  ["*", "*", "*", "*", "W", "*", "*", "*"]
]





# reversi(board, 4, 4, "W")
reversi(board, 4, 4, "B")