'''
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a sorted array of unique positive integers and a target integer, 
check if the array contains a target using binary search and return its 
index. If the array does not contain the target, return -1.

Note:
• Indexes (indices) follow the zero-based numbering rule (i.e. the index of the first element of an array is 0, not 1).
• Other versions of this problem sometimes return true or false, the item being found in the array or not.

Examples:
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 1 // returns 0
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 200 // returns 8
• Given an array: [1, 2, 3, 6, 8, 13, 113, 153, 200], target: 154 // returns -1

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def binarySearch(array: [int], target: int) -> int:
  # Write your code here.

  def binarySearchHelper(left, right):
    if left > right: return -1
    mid = (left+right) // 2

    if array[mid] == target: return mid
    elif array[mid] > target: 
      return binarySearchHelper(left, mid-1)
    else:
      return binarySearchHelper(mid+1, right)
  return binarySearchHelper(0, len(array))

# Test Cases
array = [1, 2, 3, 6, 8, 13, 113, 153, 200]
print(binarySearch(array, 1)) # 0
print(binarySearch(array, 200)) # 8
print(binarySearch(array, 8)) # 4
print(binarySearch(array, 154)) # -1