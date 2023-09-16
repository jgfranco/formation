
'''
🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: selection sort
Time: O(n squared)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 
traverse the array, i index:
  initialize current minimum idx with i
  traverse the array from the next position to the end of the array, j index: 
    if the number at j is smaller than the current minumn. update minimum

  if the minimum idx is different than i idx:
    swap elements
return array

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def sortArray(nums):
  
  for idx in range(len(nums)):
    minimum  = idx

    for j in range(idx+1, len(nums)):
      if nums[j] < nums[minimum]:
        minimum = j
    
    if minimum != idx:
      nums[idx], nums[minimum] = nums[minimum], nums[idx]
  
  return nums

# tests

print(sortArray([5,4,3,8,4,6,1]))
print(sortArray([3,2,1]))
print(sortArray([3,3,3]))
print(sortArray([1,2,3]))

    