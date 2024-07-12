
'''
You given a total number of dice, the number of faces on each 
dice and a total, write a function that determines the total 
number of ways to throw the dice to get the target sum.

If the number of faces on a dice is X, then numbers on each 
face will be 1, 2, ..., X. So a dice with 5 faces will have 
numbers 1, 2, 3, 4 and 5.
 

EXAMPLE(S)
n = 1, faces = 6, total = 3 returns 1 (must throw face 3)
n = 3, faces = 6, total = 7 returns 15
n = 3, faces = 6, total = 3 returns 1 (1,1,1)

Spoiler examples
n = 2, faces = 5, total = 8 returns  3 (4, 4 or 3, 5 or 5, 3)
 

FUNCTION SIGNATURE

what will be the recursive equation??



edge cases:
total <= 10^5
'''
# runtime: O(F^N)


# dynamic programming 

# store the value of the states which are already calculated
'''
total number of unique states = n*total

dp[n*total] = [-1]

'''

# runtime: O(total*n)
# space: O(total*n)

def number_ways(n, faces, total):

    dp = [[-1 for i in range(total + 1)] for j in range(n + 1)]

    def helper(n, total):
        
        numWays = 0
        if total<0:
            return 0
        
        if n==0 and total ==0:
            return 1
        elif n== 0 and total != 0:
            return 0

        if dp[n][total] !=-1:
            return dp[n][total]

        for f in range (1, faces+1):
            numWays += helper(n-1, total-f)
            
        dp[n][total] = numWays
        return numWays

    return helper(n, total)

print(number_ways(3,6,7), 'expect 15')
print(number_ways(3,6,3), 'expect 1')
print(number_ways(1,6,3), 'expect 1')