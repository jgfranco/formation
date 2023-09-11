"""
https://leetcode.com/problems/next-greater-element-i/submissions/

496. Next Greater Element I

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""

class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
    stack = []
    nextGreater = {}
        
    for num in nums2:
      if stack and num > stack[-1]:
        nextGreater[stack.pop()] = num
      stack.append(num)
      
    return [nextGreater.get(num, -1) for num in nums1]