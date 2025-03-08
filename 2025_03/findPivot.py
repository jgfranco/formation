
'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand. Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.
 

EXAMPLE(S)
For example, given [5, 7, 10, 3, 4], return 3.
 
               _
2 3 4 5 1 1.2 1.3 1.4 


l r  
5 1 2 3 4

      l r
2 3 4 5 1

l   c   r
1 2 3 4 5   edge

FUNCTION SIGNATURE
func findPivot(input: [Int]) -> Int
'''

def findPivot(array):

      if len(array) == 1: return array[0]
      
      l = 0
      r = len(array) - 1 
      c = (l + r) // 2 

      # pivot at 0
      if array[l] < array[r]:
            return array[l]
      
      while l != r-1:
            if array[l] < array[c]:
                  l = c
            else:
                  r = c
            c = (l + r) //2
               

      return array[r]



print(findPivot([1,2,3,4]))
print(findPivot([2,3,4,1]))
print(findPivot([5,1,2,3,4]))

print(findPivot([5,1]))
print(findPivot([5,1,2]))
print(findPivot([5]))

