'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.
 

EXAMPLE(S)
For example, given [5, 7, 10, 3, 4], return 3.
 
2341 


(N)
min so far

1234 * edge case * special
           s
[5, 7, 10, 3, 4]


FUNCTION SIGNATURE
func findPivot(input: [Int]) -> Int


12345


l and right pointer
mid pointer 

 
34512 * happy 
  _
45123

m  
l r   
5 1 2 3 4


    m
l       r    

2 3 4 5 1


1 2 3 4 5


'''

def findPivot(input):
    if len(input) ==0: return -1
    
    l = 0
    r = len(input) - 1

    while l < r:
        mid = (l + r) // 2

        if input[l] > input[mid]:
            r = mid -1
        elif input[r] < input[mid]:
            l = mid + 1
        else:
            return input[l]
    
    return input[l]


print(findPivot([]))
print(findPivot([1,2,3]))
print(findPivot([5,1,2,3,4]))
print(findPivot([2,3,4,5,1]))
print(findPivot([2,1]))
print(findPivot([1]))


import math

def helper(arr, low, high):
    if high == low:
        return low

    mid = math.floor((high + low) / 2)
    if arr[mid] < arr[high]:
        high = mid
    else:
        low = mid + 1
    return helper(arr, low, high)

def find_pivot(arr):
    if len(arr) == 0:
        return -1
    low, high = 0, len(arr) - 1
    return helper(arr, low, high)