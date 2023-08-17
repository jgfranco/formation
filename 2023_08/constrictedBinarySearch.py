"""
Given a sorted list of integers of length N, get the index of an element x in the list without performing any multiplication, division, exponent, or bit-shift operations. If the element is not found, return -1.

It can still be done in O(log N) time, but it doesn't look like normal binary search!

This problem is very difficult and problems like this should not come up in most interviews (unless you're interviewing for a position working on device drivers or other low level areas). Treat this problem not as interview preparation but rather as a fun challenge to stretch your abilities. Success on this problem requires some creative thinking.

# Examples

findIndex([10, 20, 30], 20) -> 2
findIndex([10, 20, 30], 30) -> 3
findIndex([10, 20, 30], 5) -> -1

[]

a
              p
1 2 3 4 5 6 7 8 9 11 12 13 14 15 16
                  
target = 11


anchor = 7
increment = 8
pointer = 7
"""

def findIndex(numbers, target):
  
  pointer = 0
  increment = 2
  anchor = 0

  while pointer < len(numbers):

    #print(numbers[pointer])
    #print(f'p: {pointer}, a: {anchor}, i: {increment}')
    if pointer ==0 and numbers[pointer] > target: return -1
    if numbers[pointer] == target: return pointer

    if anchor + increment >= len(numbers) or numbers[anchor + increment] > target:
      increment = 2
      pointer = anchor + 1
      continue
    
    anchor = pointer
    pointer = anchor + increment
    increment += increment

  return -1
    

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
#                                          p

print(findIndex(numbers, 11), 'expect 10')
print(findIndex(numbers,  2), 'expect 1')  
print(findIndex(numbers,  0), 'expect -1')  
print(findIndex(numbers, 17), 'expect -1')
print(findIndex(numbers, 15), 'expect 14')