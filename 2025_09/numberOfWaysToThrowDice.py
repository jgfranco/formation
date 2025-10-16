"""
recursive approach


numberOfWays variable
recursive function(n, total):

    if total less than zero: return zero
    if n == 0 and total == 0: return 1
    elif n == 0 and total != 0 return 0

    for i in range(1, faces + 1):
        numberOfWays += recursive call(n-1, total - i)

    return numberOfWays

"""

def number_ways_DP(n, faces, total):

    dp = [[-1 for _ in range(total + 1)] for _ in range(n + 1)]

    def helper(n, total):
        numWays = 0
        if total < 0:
            return 0

        if n == 0:
            if total == 0: return 1
            else: return 0

        if dp[n][total] != -1: 
            #print(n, total, dp[n][total])
            return dp[n][total]

        for i in range(1, faces +1):
            numWays += helper(n-1, total-i )
        
        dp[n][total] = numWays
        return numWays
    
    return helper(n, total)


def number_ways(n, faces, total):

    def helper(n, total):
        numWays = 0
        if total < 0:
            return 0

        if n == 0:
            if total == 0: return 1
            else: return 0

        for i in range(1, faces +1):
            numWays += helper(n-1, total-i )

        return numWays
    
    return helper(n, total)


def number_waysBottomUp(n, faces, target):
    ways = [[0 for _ in range(target + 1)] for_  in range(n)]

    # Initialize the first row. With one die, there
    # is one way to make each number from 1 to
    # the number of faces and no ways after that
    # up to the target.
    for t in range(1, target + 1):
        ways[0][t] = 1 if t <= faces else 0

    for dice in range(1, n):
        for t in range(1, target + 1):
            for face in range(1, min(t, faces + 1)):
                ways[dice][t] += ways[dice - 1][t - face]

    return ways[-1][-1]


print(number_ways(2, 5, 8), "expect 3")
print(number_ways(1, 6, 3), "expect 1")
print(number_ways(3, 6, 7), "expect 15")
print(number_ways_DP(15, 6, 30), "expect 65372310")