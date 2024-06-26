'''
Given a sorted list of integers of length N, get the index of an element *x* in the list without performing any multiplication, division, exponent, or bit-shift operations. If the element is not found, return -1.

It can still be done in O(log N) time, but it doesn't look like a normal binary search!

This problem is very difficult, and problems like this should not come up in most interviews (unless you're interviewing for a position working on device drivers or other low-level areas). Treat this problem not as interview preparation but as a fun challenge to stretch your abilities. Success in this problem requires some creative thinking.
 

EXAMPLE(S)  [8, 4, 2, 1] - represents maximum jump lengths
findIndex([10, 20, 30, 40,50, 60, 70,80,90 100], 50) == 1
index 8 is 90
index 6 = 70
findIndex([10, 20, 30], 30) == 2
findIndex([10, 20, 30], 5) == -1
 

FUNCTION SIGNATURE
findIndex(arr: Array<number>, x: number): number:
'''
def findIndex(nums, target):
    exponents = [0]
    i = 1
    while i < len(nums):
        exponents.append(i)
        i +=i
    exponents = exponents[::-1]
    
    anchor = 0

    for i in range(len(exponents)):
        idx = anchor + exponents[i]
        value = nums[idx]
        if value == target:
            return idx
        elif value < target:
          anchor = idx


    
    return -1


print(findIndex([10, 20, 30, 40, 50, 60, 70, 80], 35), "index -1")
print(findIndex([10, 20, 30, 40, 50, 60, 70, 80], 10), "index 0")
print(findIndex([10, 20, 30, 40, 50, 60, 70, 80], 50), "index 4")
print(findIndex([10, 20, 30, 40, 50, 60, 70, 80], 70), "index 6")
print(findIndex([10, 20, 30, 40, 50, 60, 70, 80], 80), "index 7")