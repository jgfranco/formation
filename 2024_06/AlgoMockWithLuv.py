# There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

# In each step, you will choose any 3 piles of coins (not necessarily consecutive).
# Of your choice, Alice will pick the pile with the maximum number of coins.
# You will pick the next pile with the maximum number of coins.
# Your friend Bob will pick the last pile.
# Repeat until there are no more piles of coins.
# Given an array of integers piles where piles[i] is the number of coins in the ith pile.

# Return the maximum number of coins that you can have.

 

# Example 1:

# Input: piles = [2,4,1,2,7,8]
# Output: 9
# Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with 7 coins and Bob the last one.
# Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
# The maximum number of coins which you can have are: 7 + 2 = 9.
# On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only get 2 + 4 = 6 coins which is not optimal.
# Example 2:

# Input: piles = [2,4,5]
# Output: 4
# Example 3:

# Input: piles = [9,8,7,6,5,1,2,3,4]
# Output: 18
"""
sort = 
nlogn
[9,8,7,6,5,1,2,3,4]

1,2,3,   4,5,6,7,8,9 

if there are n piles of coins
initial n/3 piles of coins will be always given to bob


[2,4,1,2,7,8]
sorted
 b   m,a
[1,2,2,4,7,8]


sum = 7+2

"""
# Constraints:

# 3 <= piles.length <= 105
# piles.length % 3 == 0
# 1 <= piles[i] <= 104

# 9,8,7,6,5,1,2,3,4
# Alice: 9, 7,5 
# You: 8, 6, 4
# Bob: 1, 2, 3

# Triplet: A,Y,B

def myPiles(pile):
    pile = sorted(pile)
    pileLength = len(pile)
    pointer = pileLength // 3
    mySum = 0
    while pointer < pileLength:
        mySum += pile[pointer]
        pointer += 2
    
    return mySum

print(myPiles([2,4,1,2,7,8]))
print(myPiles([9,8,7,6,5,1,2,3,4]))
print(myPiles([2,4,5]))
# Tc: nlogn
# Sc: constant

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Input: grid = [
#   ["0","0","0","0","0"],
#   ["0","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# copy
#   ["0","0","0","0","0"],
#   ["0","0","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
"""
 deque((1,0), (0,1))


 helpe visited((0,0), )r method explore()
        

 traverse bfs start at 0,0
 once i hit land do bfs to explore ( island
    visited set (keep track of what is part of the islad)
    increment my island count
    

bfs(i+1)
bfs(i-1)
bfs(j+1)
bfs(j-1)



"""

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.