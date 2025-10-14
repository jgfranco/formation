"""
Problem Prompt
Given an array, return the first element that is repeated if you were to traverse the array from left to right, low index to high index.
  Example(s)
firstRepeatedElement([1, 2, 3, 2, 1, 1]) == 2
Signature / Prototype
function firstRepeatedElement(arr) {
def firstRepeatedElement(arr: list[int]) -> int: 
"""

def firstRepeatedElement(arr: list[int]) -> int:
  visitedElements = set()

  for element in arr:
    if element in visitedElements: return element
    else: visitedElements.add(element)
  
  return  None

print(firstRepeatedElement([]) == None)
print(firstRepeatedElement([5]) == None)
print(firstRepeatedElement([5,5]) == 5)
print(firstRepeatedElement([5,10]) == None)
print(firstRepeatedElement([1, 2, 3, 4]) == None)
print(firstRepeatedElement([1, 2, 1, 3]) == 1)
print(firstRepeatedElement([7, 7, 1, 1]) == 7)
print(firstRepeatedElement([2, 8, 8, 8]) == 8)
print(firstRepeatedElement([1, 2, 3, 2, 1, 1]) == 2)
