"""
Prompt
Given an array of integers, return a sub-array of 'Left Peaks'. A Left Peak is defined as an element that is greater or equal in value to all elements to its right.
Example(s)
find_left_peaks([1, 2, 5, 3, 1, 2]) => [5, 3, 2]
find_left_peaks([3, 2, 1]) => [3, 2, 1]

Signature/Prototype
function find_left_peaks(arr) {
def find_left_peaks(arr: list[int]) -> list[int]:

Brainstorm:
traverse the list of numbers for right to left
               
1, 2, 5, 3, 1, 2

"""

def find_left_peaks(arr):

    p = len(arr) - 1
    from collections import deque
    leftPeaks = deque([])
    largestSeen = float("-inf")

    while p >=0:
        num = arr[p]
        if num >= largestSeen:
            leftPeaks.appendleft(num)
            largestSeen = num
        p -=1
    
    return list(leftPeaks)


print(find_left_peaks([1, 2, 5, 3, 1, 2]) , "[5, 3, 2]")
print(find_left_peaks([3, 2, 1]) , "[3, 2, 1]")

print(find_left_peaks([1, 3, 2, 0]) , "[3, 2, 0]")

print(find_left_peaks([]) , "[]")


print(find_left_peaks([]) == [])
print(find_left_peaks([1, 2, 5, 3, 1, 2]) == [5, 3, 2])
print(find_left_peaks([3, 2, 1]) == [3, 2, 1])
print(find_left_peaks([1, 2, 3]) == [3])
print(find_left_peaks([10, 4, 6, 3, 5]) == [10, 6, 5])
print(find_left_peaks([1,2,3,5,5,5,4,5,3,2,1]) == [5, 5, 5, 5, 3, 2, 1])
print(find_left_peaks([1,2,3,5,5,5,4,6,5,3,2,1]) == [6, 5, 3, 2, 1])
print(find_left_peaks([5,5,5,5,5]) == [5, 5, 5, 5, 5])