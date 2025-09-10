"""
Given an array of ints, compute recursively the number of times that the value 6 
appears in the array. We'll use the convention of considering only the part of 
the array that begins at the given index. In this way, a recursive call can pass 
index+1 to move down the array. The initial call will pass in index as 0.

Example(s)
array6([1, 2, 6], 0) == 1
array6([6, 6], 0) == 2
array6([1, 2, 3, 4], 0) == 0
"""


def array6(nums: list[int], index: int) -> int:

    if len(nums) <= 0 or index >= len(nums):
        return 0

    if nums[index] == 6:
        return 1 + array6(nums, index+1)
    
    return array6(nums, index+1)

    

print(array6([1,2,3,4,5,6], 0), "expect 1")
print(array6([], 0), "expect 0")
print(array6([1], 0), "expect 0")
print(array6([6,6,6], 0), "expect 3")
print(array6([1, 2, 6], 0) == 1)
print(array6([6, 6], 0) == 2)
print(array6([1, 2, 3, 4], 0) == 0)
print(array6([1, 6, 3, 6, 6], 0) == 3)
print(array6([6], 0) == 1)
print(array6([1], 0) == 0)
print(array6([], 0) == 0)
print(array6([6, 2, 3, 4, 6, 5], 0) == 2)
print(array6([6, 5, 6], 0) == 2)