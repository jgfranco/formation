
'''
❓ PROMPT
Given an array of numbers, return an array of the three largest values. 

Example(s)
findThreeLargest([1, 2, 3, 4])
findThreeLargest([1, 2, 3, 27, 4, 5, 35, 6])

 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work? use a deque as a queue to organize the resulting numbers
  
Algorithm 1:

Time: O(n) where n is the lenght of the nums list
Space: O(r) where r is the lenght of the results list
 

📆 PLAN
Outline of algorithm #: 
traverse nums list
  if the deque is empty, add first number
  otherwise check if the current number is larger than the last number in the queue
  if it is append number to queue (pop from left if queue exceeds the lenght)
  if its not
    traverse the queue backwards until you find a number that is less than the current number
    replace such number with the current number (if we are replacing number in the middle, save the original number to the beginning of the results list)
 

🛠️ IMPLEMENT
function findThreeLargest(nums) {
def find_three_largest(nums):
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def findThreeLargest(nums):
  from collections import deque
  if len(nums) < 4: return nums

  result = deque()
  #     _
  # [1, 2, 3, 27, 4, 5, 35, 6]
  #[1]
  #[1, 2]
  #[1, 2, 3]
  #[2, 3, 27]
  #[3, 4, 27]
  #[4, 5, 27]
  #[5, 27, 35]
  #[6, 27, 35]

  for num in nums:
    if len(result) == 0:
      result.append(num)
      continue

    if num >= result[-1]:
      result.append(num)
      if len(result) > 3:
        result.popleft()
      continue
    
    for i in reversed(range(len(result)-1)):
      if result[i] < num:
        if i == 1:
          result[0] = result[1]
        result[i] = num
        break

  return list(result)
      
print(findThreeLargest([]))
print(findThreeLargest([1]))
print(findThreeLargest([1, 2]))
print(findThreeLargest([1, 2, 3]))
print(findThreeLargest([1, 2, 3]))
print(findThreeLargest([1, 2, 3, 4]))
print(findThreeLargest([1, 2, 3, 27, 4, 5, 35, 6]))  

