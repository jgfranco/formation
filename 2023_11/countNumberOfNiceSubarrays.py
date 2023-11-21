"""
https://leetcode.com/problems/count-number-of-nice-subarrays/
248. Count Number of Nice Subarrays
Medium

3526

74

Add to List

Share
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
"""


def numberOfSubarrays( nums, k: int) -> int:

  prefixSum = {}

  oddCount = 0

  for i, num in enumerate(nums):
    if num % 2 != 0: oddCount +=1
    prefixSum[i] = oddCount

  
  map = {}
  res = 0
  map[0] = 1
  
  for key,val in prefixSum.items():
      delta = val - k
      if map.get(delta): 
          res += map[delta]
      map[val] = map.get(val, 0) +1
      
  return res

print(numberOfSubarrays([1,1,2,1,1], 3), "expect 2")
print(numberOfSubarrays([2,4,6], 1), "expect 0")
print(numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2), "expect 16")