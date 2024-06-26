
"""
https://leetcode.com/problems/gray-code/
89. Gray Code

An n-bit gray code sequence is a sequence of 2n integers where:

Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00,10,11,01].
- 00 and 10 differ by one bit
- 10 and 11 differ by one bit
- 11 and 01 differ by one bit
- 01 and 00 differ by one bit
Example 2:

Input: n = 1
Output: [0,1]

"""

def grayCode(n: int):
        
  if n == 0: return [0]
  if n == 1: return [0,1]
                     
  seed = ["0", "1"]
        
  for _ in range (2, n +1):
    firstHalf = seed
    secondHalf = ["x"] * len(firstHalf)
    for i in range(len(firstHalf)):
      firstHalf[i], secondHalf[-i-1] = "0" + firstHalf[i], "1" + firstHalf[i]
                
    seed = firstHalf + secondHalf
        
  return [int(x,2) for x in seed]


print(grayCode(2), "expect [0, 1, 3, 2]")