'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given coins of different denominations (e.g. cent, dime, quarter in U.S. currency) and a total amount of money, calculate the number of combinations to make up the target amount. You may assume there are infinite number of each kind of coin.

Examples:
• Given: amount = 2, coins = [1, 2, 3] // returns 2
• Possible Combinations: (2 = 2), (2 = 1+1)
• Given amount = 5, coins = [1, 2, 5] // returns 4
• Possible Combinations: (5 = 1 + 1 + 1 + 1 + 1), (5 = 2 + 1 + 1 + 1), (5 = 2 + 2 + 1), (5 = 5)
     1         
 1    2

 
this problem could be solved recursively and with the use of bactracking 

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
'''
def numberOfWays(amount, coinValues):

  combinations = 0
  def helper(amount, coinValues, pointer, sumSoFar):
    nonlocal combinations

    if amount == sumSoFar:
      combinations +=1
      return 
    if sumSoFar > amount or pointer >= len(coinValues): return

    coin = coinValues[pointer]
    sumSoFar += coin
    helper(amount, coinValues, pointer, sumSoFar)
    helper(amount, coinValues, pointer+1, sumSoFar-coin )

  helper(amount, coinValues, 0, 0)

  return combinations

print(numberOfWays(5, [1,2,3]))


"""
using dp

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
      
        dp = [0 for _ in range(amount + 1)]
        # There's only one way to reach an amount of 0 - no coins
        dp[0] = 1

        for coin in coins:
            for i in range(1, amount + 1):
                if i - coin >= 0:
                    dp[i] += dp[i-coin]

        return dp[amount]
"""