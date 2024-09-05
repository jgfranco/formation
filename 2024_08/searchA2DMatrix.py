"""
https://leetcode.com/problems/search-a-2d-matrix/submissions/1366121854/

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

"""

def search2DMatrix(matrix, target):
  rows = len(matrix)
  cols = len(matrix[0])

  left = 0
  right = rows * cols - 1

  while left <= right:
    mid = (left + right) //2
          
    value = matrix[mid //cols][mid%cols]
    if value == target:
      return True
    elif value > target:
      right = mid-1
    elif value < target:
      left = mid + 1
  return False
    

    
