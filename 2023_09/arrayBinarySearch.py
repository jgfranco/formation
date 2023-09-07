"""
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a sorted array of unique positive integers and a target integer, check if the array contains a target using binary search and return its index. If the array does not contain the target, return -1.

Note:
• Indexes (indices) follow the zero-based numbering rule (i.e. the index of the first element of an array is 0, not 1).
• Other versions of this problem sometimes return true or false, the item being found in the array or not.

Examples:
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 1 // returns 0
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 200 // returns 8
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 154 // returns -1

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
"""

def binarySearch(array: [int], target: int) -> int:
  def helper(left, right):
    if left > right: return -1
    mid = (left + right) //2

    if array[mid] == target: return mid
    elif array[mid] > target: return helper(left, mid-1)
    else: return helper(mid+1, right)




  return helper(0, len(array)-1)

# Test Cases
""" 0,8 mid = 4
    0,3 mid = 1
    2,3 mid = 2
    3,3 mid = 3 
"""
array = [1, 2, 3, 6, 8, 13, 113, 153, 200]
print(binarySearch(array, 1)) # 0
print(binarySearch(array, 200)) # 8
print(binarySearch(array, 6)) # 3
print(binarySearch(array, 154)) # -1
