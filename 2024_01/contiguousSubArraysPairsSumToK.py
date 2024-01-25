'''
    Engineering Method
  1. Explore - Identify and Clarify problem
  2. Brainstorm - Possible solutions - happy paths / edge cases
  3. Plan - viable coding solutions before coding (psuedo code)
  4. Implement - code 
  5. Verify - test
'''

'''
Given an array of integers a, your task is to find how many of its contiguous subarrays of length m contain a pair of integers with a sum equal to k.

More formally, given the array a, your task is to count the number of indices 0 ≤ i ≤ a.length - m such that a subarray [a[i], a[i + 1], ..., a[i + m - 1]] contains at least one pair (a[s], a[t]), where:

* s ≠ t
* a[s] + a[t] = k

Assumptions/Observations: 
1. Pair of integers that sum to k don't necessarily have to be contiguous. 


Example:

* For a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7], m = 4, and k = 10, the output is 5.
* Let's consider all subarrays of length m = 4 and see which fit the conditions:
  * Subarray a[0..3] = [2, 4, 7, 5] doesn't contain any pair of integers with a sum of k = 10. Note that although the pair (a[3], a[3]) has the sum 5 + 5 = 10, it doesn't fit the requirement s ≠ t.
  * Subarray a[1..4] = [4, 7, 5, 3] contains the pair (a[2], a[4]), where a[2] + a[4] = 7 + 3 = 10.
  * Subarray a[2..5] = [7, 5, 3, 5] contains two pairs (a[2], a[4]) and (a[3], a[5]), both with a sum of k = 10.
  * Subarray a[3..6] = [5, 3, 5, 8] contains the pair (a[3], a[5]), where a[3] + a[5] = 5 + 5 = 10.
  * Subarray a[4..7] = [3, 5, 8, 5] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
  * Subarray a[5..8] = [5, 8, 5, 1] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
  * Subarray a[6..9] = [8, 5, 1, 7] doesn't contain any pair with a sum of k = 10.
* So the answer is 5, because there are 5 contiguous subarrays with at least one pair with a sum of k = 10.



EXAMPLE(S)
[2, 4, 7, 5, 3, 5, 8, 5, 1, 7], m = 4, and k = 10, result is 5

diff - [8, 6, 3, 5, 7, 5, 2, 5, 9, 3]
[2, 2, 2, 2, 2], m = 3, k = 6, result is 3 
[2], m = 1, k = 1, return 0
[2], m = 1, k = 2, return 0
[2], m = 2, k = 2, return 0
[2,2,2], n = 3

Approach: 

Brute Force: 
    using nested loops get subarray of size m 

    run this logic for each subarray of size m
        dictName = {} #(index, targetDifference)
        set approach:
             - check if the curr val is in the set
                if yes => found the pair 
                if no => add the diff 
        [4,5,6,5]
        set = (6, 5)

        count = 0
        targetDifference = k - element


FUNCTION SIGNATURE
function subarraysSumToK(array, k, m)
'''

def subarraysSumToK(array, k, m):
    
  numOfSubarrays = 0

  for i in range(len(array)):
    diffSet = set()
    subArray = array[i:i+m]
    if len(subArray) < m: break

    for j in range(m):
      if subArray[j] in diffSet:
        numOfSubarrays += 1
        break
      else:
        diffSet.add(k - subArray[j])

  return numOfSubarrays


print(subarraysSumToK([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 10, 4), " expect 5")
print(subarraysSumToK([2], 2, 1), " expect 0")
print(subarraysSumToK([2], 1, 1), " expect 0")
print(subarraysSumToK([2,2,3], 4, 3), " expect 1")
print(subarraysSumToK([2,2], 4, 2), " expect 1")
print(subarraysSumToK([2,2], 4, 3), " expect 0")
print(subarraysSumToK([2,2], 4, 1), " expect 0")




def subarraysSumToK2(array, k, m):

  diffArray = [None] * (m-1)
  subArrays = 0

  for i in range(len(array)):
    print(diffArray, ",", array[i])
    
    if array[i] in diffArray:
      subArrays +=1
    p = i % (m-1)
    diffArray[p] = k- array[i]
    print("count:", subArrays)

  return subArrays
                    #      s        e
#print(subarraysSumToK2([2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 10, 4), " expect 5")