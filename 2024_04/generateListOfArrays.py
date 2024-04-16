'''
❓ PROMPT
Given a target integer *X*, iterate from 1 to *X* and return a matrix sequence where each array starts with 1 and goes up to the current iteration. Each iteration should increment the array size and values until it reaches *X*.

[
[1],
[1, 2], 
[1, 2, 3],
[1, 2, 3, 4],
[1, 2, 3, 4, 5],
...
...
...
[1, 2, 3, ..., X]
]

Example(s)
generateSequence(2) == [[1], [1,2]]
generateSequence(3) == [[1], [1,2], [1,2,3]]
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: use nested for loops, the first one to create the inner arrays, the second one to populate them 
Time: O(N**2) 
Space: O(N**2)
 

📆 PLAN
Outline of algorithm #: 

create a result array
traverse from 1 to target + 1 as i
  create an empty array
  traverse from 1 to i + 1 as j
    append j to array
  append array to result array

return result array
 

🛠️ IMPLEMENT
function generateSequence(target) {
def generateSequence(target: int) -> list[list[int]]:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def generateSequence(target):

  result = []
  #2
  for layer in range(1, target+1):# 1,2
    array = []
    for num in range(1, layer+1):
      array.append(num)
    result.append(array)

  return result

print(generateSequence(0))
print(generateSequence(1))
print(generateSequence(2))
print(generateSequence(5))


print(generateSequence(0) == [[]] or generateSequence(0) == [])
print(generateSequence(1) == [[1]])
print(generateSequence(2) == [[1], [1,2]])
print(generateSequence(3) == [[1], [1,2], [1,2,3]])
print(generateSequence(4) == [[1], [1,2], [1,2,3], [1,2,3,4]])