'''
❓ PROMPT
Given a nested array where each element may be 1) an integer or 2) an array, whose elements may be integers or other arrays, compute the sum of all the integers in the nested array.

What is the shape or pattern of this nested array structure?

As a follow-up, modify this code to multiply each list sum by its depth in the nesting. [1, 2] returns 3 since (1 + 2) is only inside one array.

However, [4, [2, 3]] returns 14 because the depth of [2, 3] is 2, so (2+3) * 2 = 10.
4 is added at the end to get 10 + 4 = 14.
While [4, [2, [3]]] returns 26 because the depth of [3] is 3 so 3 * 3 = 9. 
Then the depth of [2, 9] is 2 so (2+9) * 2 = 22.
4 is added at the end to get  22 + 4 = 26.

Example(s)
sumNestedList([1, 2, 3]) == 6
sumNestedList([1, [1, 2, 3], 3]) == 10
sumNestedList([1, [1, [1, [1, [1]]]]]) == 5

sumNestedListWithDepth([4, [2, 3]]) == 14 because 4 + (2+3)*2
sumNestedListWithDepth([4, [2, [3]]]) == 26 because 4+(2+ (3*3))*2
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work? recursive function 
Algorithm 1:
Time: O(n) where n is the number of elements on the array
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 
 
initialize a variable to store the sum

for every element in the array:
  check if its an array: call recursively on the function
  else accumulate on the sum

return sum

🛠️ IMPLEMENT
function sumNestedList(list) {
function sumNestedListWithDepth(list) {
'''
def sumNestedList(array):
    result = 0

    for el in array:
        if type(el) == list:
            result += sumNestedList(el)
        else:
            result += el
    return result

def sumNestedListWithDepth(array):
  
  def helper(array, depth):
    result = 0

    for el in array:
        if type(el) == list:
            result += helper(el, depth+1)
        else:
            result += el
    return result * depth

  return helper(array, 1)      
    


'''

def sumNestedList(nestedList: list[int]) -> int:
def sumNestedListWithDepth(nestedList: list[int]) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
print(sumNestedList([1,2,3]) == 6)
print(sumNestedList([1,[2,3]]) == 6)
print(sumNestedList([1,[2,[3]]]) == 6)
print(sumNestedList([1,[1,2,3],3]) == 10)
print(sumNestedList([1,[1,[1,[1,[1]]]]]) == 5)
print(sumNestedList([1,[1,[2],[],[],[],3],3]) == 10)
print(sumNestedList([1,[1,[2],[],[[[[]]]],[],3],3]) == 10)
print(sumNestedList([1]) == 1)
print(sumNestedList([[1]]) == 1)
print(sumNestedList([[[1]]]) == 1)
print(sumNestedList([[[[1]]]]) == 1)
print(sumNestedList([[[[]]]]) == 0)

print(sumNestedListWithDepth([1,2,3]) == 6)
print(sumNestedListWithDepth([1,[2,3]]) == 11)
print(sumNestedListWithDepth([1,[2,[3]]]) == 23)
print(sumNestedListWithDepth([1,[1,2,3],3]) == 16)
print(sumNestedListWithDepth([1,[1,[1,[1,[1]]]]]) == 153)
print(sumNestedListWithDepth([1,[1,[2],[],[],[],3],3]) == 24)
print(sumNestedListWithDepth([1,[1,[2],[],[[[[]]]],[],3],3]) == 24)
print(sumNestedListWithDepth([1]) == 1)
print(sumNestedListWithDepth([[1]]) == 2)
print(sumNestedListWithDepth([[[1]]]) == 6)
print(sumNestedListWithDepth([[[[1]]]]) == 24)
print(sumNestedListWithDepth([[[[]]]]) == 0)