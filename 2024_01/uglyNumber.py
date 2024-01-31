"""
263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
"""

def isUgly(n: int) -> bool:
  if n <= 0:
    return False
  if n == 1: 
    return True
  
  primeFactors = [2,3,5]
  if n in primeFactors: 
    return True
  
  for prime in primeFactors:
    if n%prime == 0:
      return isUgly(n//prime)

  return False

print(isUgly(6), "expect True")
print(isUgly(4), "expect True")
print(isUgly(1), "expect True")
print(isUgly(9), "expect True")
print(isUgly(14), "expect False")
print(isUgly(11), "expect False")
print(isUgly(7), "expect False")
print(isUgly(13), "expect False")