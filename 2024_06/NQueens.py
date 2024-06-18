'''
Given an NxN board, find the number of positions that allow N queens to be placed on the board where no queen can attack another queen.

Queens attack along their row, column, and diagonal. eg, *x* means the square can be attacked by a queen.

x . x . x
. x x x .
x x Q x x
. x x x .
x . x . x

we are looking for those places where a new queen can be placed safely

EXAMPLE(S)
Submit examples to #feedback-content!


FUNCTION SIGNATURE
function nQueens(n) => number
 
'''