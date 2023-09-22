"""
Q. Given two integer arrays of equal length, merge them into one by taking the maximum value at the each index.

Example:
Inputs: [1, 2, 3, 4, 5] and [5, 4, 3, 2, 1]
Output:[5, 4, 3, 4, 5] // at the index 0, 5 is bigger than 1. Thus, take 5 as the first element.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer a1

[input] array.integer a2

[output] array.integer
"""

def solution(a1, a2):
    
    for i in range(len(a1)):
        a1[i] = max(a1[i], a2[i])
        
    return a1

"""

Q. Given a sorted array of integers and a target number, insert it after the first number that matches it, if no number matches it, do nothing.

Examples:
Input1: array = [1, 2, 3, 4, 5, 6], target =3
Output1: [1, 2, 3, 3, 4, 5, 6]

Input2: array = [1, 5, 7, 8], target = 7
Ouput2: [1, 5, 7, 7, 8]

Input3: array = [1, 5, 7, 8], target = 9
Output3: [1, 5, 7, 8]
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[input] integer target

[output] array.integer
"""
def solution(array, target):
    arr = []
    
    for e in array:
        if e == target:
            arr.append(e)
            arr.append(target)
        else:
            arr.append(e)
    
    return arr

"""
Q. Given an array of integers, find the pivot index, which is defined as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index (excluding the value at the index). If a pivot index does not exist, return -1. If there are multiple pivot indices, return the left-most one.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] integer

"""
def solution(array):
    if len(array) < 3: return -1
    i = 0
    j = len(array) -1
    
    leftSum = array[i]
    rightSum = array[j]
    
    while i< j:
        if leftSum == rightSum and i +1 == j-1:
            return j-1
        
        if leftSum >= rightSum:
            j -= 1
            rightSum += array[j]
        elif leftSum < rightSum:
            i += 1
            leftSum += array[i]

    return -1
            
    
"""Given an array of integers, check if there is a triplet (a, b, c) that satisfies a^2 + b^2 = c^2.

Input: array: [1, 2, 4, 2, 5, 3]
Output: true // [3, 4, 5]

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] boolean

"""

def solution(array):
    doubled = [x*x for x in array]
    
    print(doubled)
    
    for i in range(len(doubled)):
        for j in range(i+1, len(doubled)):
            if doubled[i] + doubled[j] in doubled:
                return True
    
    return False

"""
Q. Given a sorted array of integers and a target integer, check if the array contains a target using binary search.

The array may contain duplicate values.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[input] integer target

target value to be checked

[output] boolean
"""
def solution(array, target):
    if len(array) == 0: return False

    def binarySearch(left, right):
        
        if left > right: return False
        
        mid = (left + right ) //2
        
        if array[mid] == target: return True
        
        if array[mid]< target:
            return binarySearch(mid+1, right)
        elif array[mid]> target:
            return binarySearch(left, mid-1)
        
    
    return binarySearch(0, len(array))

"""
Given an array of n distinct integers in the range of [0, n] (including 0 and n), find the missing number in the range from the array.

Example:
Input: [0,1]
Output: 2 // n = 2 since there are 2 elements in the input array. So the missing number from the range [0, 2] is 2.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] integer
"""
def solution(array):
    complete = [x for x in range(len(array)+1)]
    
    return sum(complete) - sum(array)