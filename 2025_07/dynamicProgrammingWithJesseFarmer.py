# Dynamic Programming

## Official Definition (Not Interesting, but for completion's sake)
# It's a technique that works on problems which have two features:
#   1. Overlapping subproblems
#   2. Optimal 

## How To Recognize
# 1. Your spidey-sense says that maybe a greedy algorithm will work
# 2. You think of a greedy algorithm and realize that one won't work
# 3. You think of maybe another greedy algorithm and, alas, that too won't work
# 4. Screw this, I bet it's a dynamic programming problem

## 0-1 Knapsack Problem
# Most-expensive first
# 1 painting that weighs 90 pounds and is worth $1,000,000
# 10 paintings that weight 20 pounds each and are worth $500,000

# Least-heavy first
# 
# 

## Counting Stairs / Staircase Problem
# Imagine a staircase with N stairs. If it's easier, imagine a specific number like N=100 or N=10.

# Your legs are long enough that you can climb the stairs by going up one step or by skipping a step and going up two steps.

# How many ways are there to get to the top of the stairs?

## If you're practicing, you should be focused on the top-down or recursive approach
## Any top-down down approach can be translated mechanically/thoughtlessly into a bottom-up approach. The opposite is a little less true, but it only requires a little thought.

from functools import lru_cache

@lru_cache(maxsize=3)
def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

@lru_cache
def stairs(n):
    if n == 1:
        return 1
    
    if n == 2:
        return 2

    if n == 3:
        return 4

    return stairs(n-1) + stairs(n-2) + stairs(n-3)

# function fibBottomUp(n) {
#   let fib = [];

#   for (let i = 0; i <= n; i++) {
#     if (i === 0) {
#       fib[i] = 0;
#       continue;
#     }

#     if (i === 1) {
#       fib[i] = 1;
#       continue;
#     }

#     if (i > 1) {
#       fib[i] = fib[i-1] + fib[i - 2];
#       continue;
#     }
#   }

#   return fib[n];
# }

# print(stairs(40))

def longest_common_subsequence(left, right):
    """
    Find the length of the longest common subsequence between two strings.

    :param left: First string
    :param right: Second string
    :return: Length of the longest common subsequence

    Example:
    longest_common_subsequence(
        ['A', 'B', 'C', 'B', 'E', 'C'],
        ['B', 'D', 'C', 'A', 'E', 'A']
    ) # => returns 4 because ['B', 'C', 'E', 'A'] is the LCS
    """
    # TODO: Implement the longest common subsequence algorithm
    n = len(left)
    m = len(right)

    if (n == 0):
        return 0
    
    if (m == 0):
        return 0

    last_left = left[n - 1]
    last_right = right[m - 1]

    rest_left = left[0:n-1]
    rest_right = right[0:m-1]

    if (last_left == last_right):
        return 1 + longest_common_subsequence(rest_left, rest_right)
    else:
        return max(
            longest_common_subsequence(left, rest_right),
            longest_common_subsequence(rest_left, right)
            # longest_common_subsequence(rest_left, rest_right)
        )

def longest_common_subsequence_ref(left, right, n=None, m=None):
    # Other languages allow a dynamic default value, e.g., n = len(left)
    if n is None:
        n = len(left)
    if m is None:
        m = len(right)

    if n == 0 or m == 0:
        return 0

    last_left = left[n - 1]
    last_right = right[m - 1]

    if last_left == last_right:
        return 1 + longest_common_subsequence_ref(left, right, n - 1, m - 1)
    else:
        return max(
            longest_common_subsequence_ref(left, right, n, m - 1),
            longest_common_subsequence_ref(left, right, n - 1, m)
        )

def longest_common_subsequence_bottom_up(left, right):
    # Create an (n+1)-by-(m+1) array. The +1 is there because we
    # paramaterize over the length of the subsequences, i.e.,
    # LCS[0][0] corresponds to the empty subsequence
    LCS = [[None for _ in range(len(right) + 1)] for _ in range(len(left) + 1)]

    for n in range(len(left) + 1):
        for m in range(len(right) + 1):
            if n == 0 or m == 0:
                LCS[n][m] = 0
                continue

            last_left = left[n - 1]
            last_right = right[m - 1]

            if last_left == last_right:
                LCS[n][m] = 1 + LCS[n - 1][m - 1]
                continue
            else:
                LCS[n][m] = max(
                    LCS[n][m - 1],
                    LCS[n - 1][m]
                )
                continue

    return LCS[len(left)][len(right)]

# print(longest_common_subsequence(list('abcd'), list('abcd')))

print(longest_common_subsequence(
        ['A', 'B', 'C', 'B', 'E', 'C', 'A'],
        ['B', 'D', 'C', 'A', 'E', 'A']
    ))

def knapsack_01(n: int, capacity: int, weights: List[int], values: List[int]) -> int:
    """
    Given a bag with a capacity and a list of items with weights and values,
    return the maximum value that can be carried by the bag. There is only
    one copy of each item.
    
    Args:
        n: Number of items available
        capacity: Maximum weight capacity of the knapsack
        weights: List of item weights
        values: List of item values
        
    Returns:
        Maximum value that can be achieved within the weight capacity
    """
    if n <= 0:
        # If we have no items, there's nothing to take
        return 0
    elif capacity <= 0:
        # If we have no capacity, we can't take anything
        return 0
    elif weights[n - 1] > capacity:
        # If the item weighs more than our capacity, we can't take it
        # It's as if that item wasn't included to begin with
        return knapsack_01(n - 1, capacity, weights, values)
    else:
        # We now have a choice whether to take the item or not
        # If we take then our total value is the value of the item,
        # plus the value in a world where that item didn't exist but we had less capacity
        value_if_we_take = values[n - 1] + knapsack_01(n - 1, capacity - weights[n - 1], weights, values)
        value_if_we_skip = knapsack_01(n - 1, capacity, weights, values)
        
        # Return the maximum value between taking or skipping the current item
        return max(value_if_we_take, value_if_we_skip)


# https://github.com/jfarmer/exercises-js-dynamic-programming
