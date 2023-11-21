"""
96. Unique Binary Search Trees
Medium

10031

385

Add to List

Share
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

 

Example 1:

1
    3
   2

   
1
  2
    3

       
  2
1   3


    3
  2
1


    3
1
  2

Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1

"""


def numTrees(n):
  """
  :type n: int
  :rtype: int
  """
  G = [0]*(n+1)
  G[0], G[1] = 1, 1

  for i in range(2, n+1): # i = 2
      for j in range(1, i+1): # j = 1
          G[i] += G[j-1] * G[i-j]
        #G[2] += 1 * 

  return G[n]

#using Catalan Numbers

def numTreesCN(n):
  C = 1
  for i in range(0, n):
    C = C * 2*(2*i+1)/(i+2)
  return int(C)


print(numTrees(3))
print(numTreesCN(3))