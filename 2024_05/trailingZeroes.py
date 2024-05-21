"""
172. Factorial Trailing Zeroes
Medium

3150

1948

Add to List

Share
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104
 

Follow up: Could you write a solution that works in logarithmic time complexity?
"""

def trailingZeroes(n) -> int:
        
  def factorial(n):
      
    if n == 0: return 1
    res = 1
    for i in range(1, n+1):
      res = res * i

    return res
  
  fac = factorial(n)
  counter = 0
  while fac %10 == 0:
      counter +=1
      fac //= 10
  return counter

def trailingZeroes2(n):
  result = 0
  while n >0:
    n //=5
    result+=n
  
  return result


print(trailingZeroes(5), "expect 1")
print(trailingZeroes2(5), "expect 1")

print(trailingZeroes(10), "expect 2")
print(trailingZeroes2(10), "expect 2")
