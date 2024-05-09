
'''
Longest Increasing Subsequence

Given an array of integers, return an array representing the longest increasing subsequence.
 

EXAMPLE(S)
[1, 2, 3] => 3 (whole array)
[5, 1, 4, 2, 3] => 3 ([1, 2, 3] is the longest increasing subsequence)
 

FUNCTION SIGNATURE
function longestIncreasingSubSequenceLength(sequence: [Int]) -> Int:


[5]
[1]
  [1, 4]
  [1, 2]
  [1, 2, 3]
[4]
[2]
  [2,3]
[3]

- iterate through the array input
- stack the increasing element 



at current number
  use it  (recursive calls)  [5]
     (we only use when  larger than  at stack[-1])
  not use it (recursive calls) [] 

'''

def longestIncreasingSubSequenceLength(array):

  result = []
    
  def helper(stack, index): 
    nonlocal result
    if index == len(array):
      if len(stack) > len(result):
        result = stack.copy()
      return
      
    # use it
    if not stack or stack[-1] < array[index]:
      newStack = stack.copy()
      newStack.append(array[index])
      helper(newStack, index+1)
      return
    elif len(stack) > len(result):
      result = stack.copy()

    
    # not use it

    stack.pop()
    helper(stack, index)
   


  helper([],0)

  return result


"""
             i
[5, 1, 4, 2, 3]
          j 

subsequences = [[1,2]]
"""
print(longestIncreasingSubSequenceLength([5, 1, 4, 2, 3]), "expect: [1, 2, 3]")
print(longestIncreasingSubSequenceLength([4, 5, 6, 7, 1, 2, 3]), "expect: [4, 5, 6, 7]")
print(longestIncreasingSubSequenceLength([1, 2, 3]), "expect: [1, 2, 3]")

def LIS(array):
  dp = [1] * len(array)
           
  # [5, 1, 4, 2, 3]
  # [1, 1, 1, 1, 1]
  for i in range(1, len(array)):
    for j in range(i):
      if array[i] > array[j]:
        dp[i]= max(dp[i], dp[j]+1)
  
  return max(dp)

print(LIS([5,1,4,2,3]))