
'''
0-1 Knapsack

Given weights and values of items, put these items in a knapsack of capacity c to get the maximum total value possible with a weight that does not exceed c.

• You are given two array of integers values and weights which represent values and weights of given items respectively and c which represents knapsack capacity.
• You cannot include a fraction of an item nor include the same item multiple times. Each item can be taken or left.
 

EXAMPLE(S)
{1: 4, 2: 5, 3: 6, 5: 10}, 5 => 11
{1: 4, 2: 5, 3: 6, 5: 10}, 6 => 15

weights   values
[1,2,3,5] [4,5,6,10]

FUNCTION SIGNATURE
function knapsack(values, weights, limit)
def knapsack(values, weights, limit):
'''


def knapsack01(n, values, weights, limit):

    if n <= 0: #we have run out of options
        return 0
    elif limit <= 0: # we have run out of capacity
        return 0
    elif weights[n-1] > limit: #skip the current number if we exceed capacity
        return knapsack01(n-1, values, weights, limit)
    
    else:
        valueIfWeTake = values[n-1] + knapsack01(n-1, values, weights, limit- weights[n-1])
        valueIfWeSkip = knapsack01(n-1, values, weights, limit)
        return max(valueIfWeSkip, valueIfWeTake)

def knapsack(values, weights, limit):
    n = len(values)
    return knapsack01(n, values, weights, limit)


print(knapsack([99], [3], 3) == 99)
print(knapsack([99], [10], 3) == 0)
print(knapsack([99], [3], 10) == 99)
print(knapsack([6, 9, 13], [1, 2, 3], 5) == 22)
print(knapsack([6, 9, 13], [1, 2, 3], 3) == 15)
print(knapsack([6, 10, 12, 15, 1], [1, 2, 3, 4, 5], 10) == 43)
print(knapsack([20, 5, 10, 40, 15, 25], [1, 2, 3, 8, 7, 4], 10) == 60)
print(knapsack([4, 5, 6, 10], [1, 2, 3, 5], 5) == 11)
print(knapsack([4, 5, 6, 10], [1, 2, 3, 5], 6) == 15)
print(knapsack([4, 5, 6, 10], [1, 2, 10, 5], 5) == 10)
print(knapsack([4, 5, 6, 10], [20, 2, 10, 5], 5) == 10)
print(knapsack([20, 5, 10, 40, 15, 25], [1, 2, 3, 8, 7, 4], 9) == 60)
