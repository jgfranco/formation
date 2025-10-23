'''
Given a chess board with a set of bishops, return the number of pairs of bishops that are attacking each other. Bishops will be given as an array of tuples.
 

EXAMPLE(S)
Bishops: [(0, 0), (2, 2), (1, 2), (3, 0)]
This would look like this:



0  1 2 3 4
   x . . . .
-1 . . x . .
-2 . . x . .
-3 x . .  .
-2 . . . . .

0       0
0,0.    2,2

3        3
1,2 and 3,0 


0,0  2,2  3,3 -> 3 pairs attacking on this diag
0,0 1,1 2,2  3,3 -> 3 + 2 + 1 = 6 
1,2 3,0 -> 1 pair




Q. Can a bishop attack a bishop through another bishop?
A. Yes. bishops attack all bishops on its diagonal, no matter how many there are. For example, in this board, there are 3 pairs of bishops attacking each other since every pair of bishops are attacking each other:
x . .
. x .
. . x

total 4

In this case, there are 2 pairs of bishops attacking each other.

define 2 maps, positive and negative diagonals


iterate through the bishop x,y coordinates:
    
    increment postive diagonals of x+y
    increment negative diagonals of x-y

                  _
[(0, 0), (2, 2), (3,3)]

(x+y)
map1: {
0:1
4:1
6:1 
}

(x-y)
map2:{
0:3
}

pairsInConflict+= 3
    

FUNCTION SIGNATURE
def numberOfBishops(bishops): Int
function numberOfBishops(bishops)

'''

def numberOfBishops(bishops) -> int:

    positiveDiagonals = {}
    negativeDiagonals = {}

    pairsInConflict = 0
    for bishop in bishops:

        x,y = bishop[0], bishop[1]

        if x + y in positiveDiagonals:
            pairsInConflict += positiveDiagonals[x + y]
            positiveDiagonals[x + y] += 1
        else:
            positiveDiagonals[x + y] = 1

        if x - y in negativeDiagonals:
            pairsInConflict += negativeDiagonals[x - y]
            negativeDiagonals[x - y] += 1
        else:
            negativeDiagonals[x - y] = 1
    
    return pairsInConflict
          
    


# Test case: Bishops form two attacking pairs
bishops = [(0, 0), (2, 2), (1, 2), (3, 0)]
print(numberOfBishops(bishops) == 2)

# Test case: Bishops form no attacking pairs
bishops = [(0, 0), (1, 3), (3, 4), (9, 6)]
print(numberOfBishops(bishops) == 0) # should be 0

# Test case: Bishops form multiple attacking pairs
bishops = [(1, 1), (2, 2), (5, 3), (6, 2), (5, 0), (0, 5)]
print(numberOfBishops(bishops) == 3) ## should be 3

# Test case: Bishops form attacking pairs on both diagonals
bishops = [(0, 0), (3, 3), (6, 6), (0, 6), (6, 0)]
print(numberOfBishops(bishops) == 6) # should be 6

# Test case: Bishops form attacking pairs on a single diagonal
bishops = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
print(numberOfBishops(bishops) == 10) # should be 10

# Test case: Single bishop, no attacking pairs
bishops = [(0, 0)]
print(numberOfBishops(bishops) == 0) # Defaults to 0 

# Test case: Empty list, no attacking pairs
bishops = []
print(numberOfBishops(bishops) == 0) # Defaults to 0
