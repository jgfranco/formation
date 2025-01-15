


def pairsOfAttackingBishops(bishops):

    left = {}  # 0:2, -2:0
    right = {} # 0:0, 2:1, 4:0
    count  = 0 # 0, 1, 3, 4

    for x,y in bishops: # 0, 0 
        minus = x - y
        plus = x + y

        left[minus] = left.get(minus, -1) + 1
        right[plus] = right.get(plus, -1) + 1

        count += left[minus] + right[plus]

    return count

#print(numberOfBishops([(0, 0), (2, 2), (1, 2), (3, 0)])) # expect 2
#print(numberOfBishops([(0,0),(1,1),(2,2)])) # expect 3
#print(numberOfBishops([(0,0),(1,1),(2,2), (0,2)])) # expect 4





# Test case: Bishops form two attacking pairs
bishops = [(0, 0), (2, 2), (1, 2), (3, 0)]
print(pairsOfAttackingBishops(bishops) == 2)

# Test case: Bishops form no attacking pairs
bishops = [(0, 0), (1, 3), (3, 4), (9, 6)]
print(pairsOfAttackingBishops(bishops) == 0) # should be 0

# Test case: Bishops form multiple attacking pairs
bishops = [(1, 1), (2, 2), (5, 3), (6, 2), (5, 0), (0, 5)]
print(pairsOfAttackingBishops(bishops) == 3) ## should be 3

# Test case: Bishops form attacking pairs on both diagonals
bishops = [(0, 0), (3, 3), (6, 6), (0, 6), (6, 0)]
print(pairsOfAttackingBishops(bishops) == 6) # should be 6

# Test case: Bishops form attacking pairs on a single diagonal
bishops = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
print(pairsOfAttackingBishops(bishops) == 10) # should be 10

# Test case: Single bishop, no attacking pairs
bishops = [(0, 0)]
print(pairsOfAttackingBishops(bishops) == 0) # Defaults to 0 

# Test case: Empty list, no attacking pairs
bishops = []
print(pairsOfAttackingBishops(bishops) == 0) # Defaults to 0
  
