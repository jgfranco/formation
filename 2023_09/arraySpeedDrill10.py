"""
Q. Given an array of integers where all but one adjacent pair has been swapped (unsorted), fix the array by swapping back the broken pair.

Example:
Input: [1, 2, 3, 5, 4, 6]
Output: [1, 2, 3, 4, 5, 6]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] array.integer
"""
def solution(array):
    
  for i in range(len(array)):
    if i +1 != array[i]:
      array[i], array[i+1] = array[i+1], array[i]
      break
            
  return array


"""Q. Given an array, stack each element by adding the sum of the previous elements.

Example:
Input: [1, 2, 3, 0]"
Output: [1, 3, 6, 6] // ["1", "1+2", "1+2+3", "1+2+3+0"]

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] array.integer"""

def solution(array):

    prevSum = 0
    for i in range(len(array)):
        curr = array[i]
        array[i] += prevSum
        prevSum  += curr
    return array

"""Q. Given an array of integers and a target integer, return indices of the two numbers such that they add up to the target.

You may assume there is one unique solution pair, and the same element cannot be used twice.
You must return a solution pair sorted in ascending order.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[input] integer target

[output] array.integer"""
def solution(array, target):

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            
            if array[i] + array[j] == target:
                return [i,j]
                
    return None

"""Q. Given two integer arrays of equal length, merge them into one by taking the maximum value at the each index.

Example:
Inputs: [1, 2, 3, 4, 5] and [5, 4, 3, 2, 1]
Output:[5, 4, 3, 4, 5] // at the index 0, 5 is bigger than 1. Thus, take 5 as the first element.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer a1

[input] array.integer a2

[output] array.integer"""

def solution(a1, a2):

    for i in range(len(a1)):
        a1[i] = max(a1[i], a2[i])
        
    return a1

"""Given an array of n distinct integers in the range of [0, n] (including 0 and n), find the missing number in the range from the array.

Example:
Input: [0,1]
Output: 2 // n = 2 since there are 2 elements in the input array. So the missing number from the range [0, 2] is 2.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] integer"""

def solution(array):

    complete = [x for x in range(len(array)+1)]
    
    return sum(complete) - sum(array)

"""
Q. Given an array of integers, move all 0's to the end of the list while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,1]
Output: [1,3,1,0,0]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] array.integer


"""


def solution(array):

    zeroes = []
    non = []
    
    for i in range(len(array)):
        num = array[i]
        if num ==0: zeroes.append(0)
        else: non.append(num)
        
    return non+zeroes
            