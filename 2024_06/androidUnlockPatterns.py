'''
Question : 

Given a 3x3 lock screen in the following arrangement:

1 2 3
4 5 6
7 8 9

count the total number of unlock patterns that use N numbers.

A pattern is valid if the following criteria are met:
- no number is used more than once
- a path from one number to another does not directly pass through an unused number. eg:
  - 2 -> 1 -> 3 is valid, 
  but 1 -> 3 is not valid because it directly passes through the unused number 2

NOTE: It is possible to go from 2 to 9 (or 3 to 4) because the pattern may move between rows and colunns on diagonals.
 
2 -> 1 -> 3 is valid, 
1 -> 3 is not valid 

EXAMPLE(S)
1 2 3
4 5 6
7 8 9


Bridges : 

   1   2   3   4   5   6   7   8   9
1  0   0   2   0   0   0   4   0   5
2  0   0   0   0   0   0   0   5   0
3  2   0   0   0   0   0   5   0   6
4  0   0   0   0   0   5   0   0   0
5  0   0   0   0   0   0   0   0   0
6  0   0   0   5   0   0   0   0   0
7  4   0   5   0   0   0   0   0   8    
8  0   5   0   0   0   0   0   0   0 
9  5   0   6   0   0   0   8   0   0


bridge[x][y] = z where z must be already visited in the pattern if we have to go from x to y. 


Number of K-digit patterns starting from 1 = Number of K-digit patterns starting from 3 =  Number of K-digit patterns starting from 7 = Number of K-digit patterns starting from 9 


Number of K-digit patterns starting from 2 = Number of K-digit patterns starting from 4 =  Number of K-digit patterns starting from 6 = Number of K-digit patterns starting from 8 


Answer += Number of K-digit patterns starting from 1 * 4
Answer += Number of K-digit patterns starting from 2 * 4
Answer += Number of K-digit patterns starting from 5 


How do we find Number of N-digit patterns starting from D ?

numberOfKeys = 3
start with  = 1


totalPatternsFromD(visit, bridges, numberOfKeys, digit)
 Let's identify the base case : 
   if numberOfKeys == 0 return 1

loop through possibile next digit (1-9)
 depending upon checks, we will recursively call the function 




4 -> 1 -> 3 -> 6 is invalid because 1 -> 3 passes through the unused 2

2 -> 4 -> 1 -> 3 -> 6 is valid
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 is valid
 

FUNCTION SIGNATURE
function countPatterns(numberOfKeys) {
def countPatterns(numberOfKeys: int) -> int:

Test cases : 

print(countPatterns(1) == 9)
print(countPatterns(2) == 56)
print(countPatterns(3) == 320)
print(countPatterns(4) == 1624)
print(countPatterns(5) == 7152)
print(countPatterns(6) == 26016)
print(countPatterns(7) == 72912)
print(countPatterns(8) == 140704)
print(countPatterns(9) == 140704)

'''

def countPatterns(N): 
    bridges = [
        [],
        [0, 0, 0, 2, 0, 0, 0, 4, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
        [0, 2, 0, 0, 0, 0, 0, 5, 0, 6],
        [0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 4, 0, 5, 0, 0, 0, 0, 0, 8],
        [0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 6, 0, 0, 0, 8, 0, 0],
    ]

    visited = [False]*10
    answer = 0
    symetric_positions_1_3_7_9 = 4 * totalPatternsFromD(visited, bridges, N - 1, 1)
    symetric_positions_2_4_6_8 = 4 * totalPatternsFromD(visited, bridges, N - 1, 2)
    center_position = totalPatternsFromD(visited, bridges, N-1, 5)
    answer = symetric_positions_1_3_7_9 + symetric_positions_2_4_6_8 + center_position
    return answer




def totalPatternsFromD(visited, bridges, numberOfKeys, digit):
    if numberOfKeys == 0: 
        return 1
        
    visited[digit] = True
    count = 0
    for i in range(1, 10):
      if not visited[i] and (bridges[digit][i] == 0 or visited[bridges[digit][i]]):
        count +=  totalPatternsFromD(visited, bridges, numberOfKeys-1, i)
        
    visited[digit] = False
    return count

'''
Follow up : 
https://leetcode.com/problems/max-points-on-a-line/description/

'''


print(countPatterns(1) == 9)
print(countPatterns(2) == 56)
print(countPatterns(3) == 320)
print(countPatterns(4) == 1624)
print(countPatterns(5) == 7152)
print(countPatterns(6) == 26016)
print(countPatterns(7) == 72912)
print(countPatterns(8) == 140704)
print(countPatterns(9) == 140704)