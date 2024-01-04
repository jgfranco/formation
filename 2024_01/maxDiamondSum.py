'''
❓ PROMPT
In a rectangular matrix, we can draw a diamond shape of various sizes surrounding any single location. For example, if we have the matrix:

0 0 0 4 0 0 0
0 0 4 3 4 0 0
0 4 3 2 3 4 0
4 3 2 1 2 3 4
0 4 3 2 3 4 0
0 0 4 3 4 0 0
0 0 0 4 0 0 0

Starting from the center of this matrix, location (3, 3), has a value 1 and is the single location at distance 1 from this point. The locations with the value 2 are the perimeter of the diamond shape at distance 2. The locations with the value 3 represent the perimeter of the diamond at distance 3. Similar for 4.

The distance function between two points defined as abs(r1 - r2) + abs(c1 - c2) + 1 where abs() is the absolute value.

Given a rectangular matrix and a distance, d, find the maximum total value of all of the locations at distance, d or less, for all diamonds with a radius of d. Each diamond you consider should fit completely in the matrix and not be truncated by the bounds of the matrix.

Example(s)
const m3 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

const m4 = [
  [1, 2, 3, 1],
  [4, 5, 6, 1],
  [7, 8, 9, 1],
  [1, 1, 1, 1],
];

const m5 = [
  [1, 2, 3, 1, 1],
  [4, 5, 6, 1, 1],
  [7, 8, 9, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
];

maxDiamondSum(m3, 1) => 9
maxDiamondSum(m3, 2) => 25 (5 is the center with the diamond sum 2+4+5+6+8)
maxDiamondSum(m4, 1) => 9
maxDiamondSum(m4, 2) => 30 (8 is the center with the diamond sum 5+7+8+9+1)
maxDiamondSum(m4, 3) => 0
maxDiamondSum(m5, 3) => 45 (9 is the center)
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function maxDiamondSum(m, d) // returns a number
def max_diamond_sum(m: list, d: int) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.
'''

def maxDiamondSum(m, d):
  
  height = len(m)
  width = len(m[0])

  diamondHeightAndWidth = (d*2) -1

  if height < diamondHeightAndWidth or width < diamondHeightAndWidth:
    return 0

  if d == 1:
    return max(max(m))
  
  maxSum = 0

  def getDiamondSum(r, c):
    offset = 0
    reverse = False
    sum = 0
    for row in range(r-d+1, r+d):
      for col in range(c-offset, c+offset+1):
        sum += m[row][col]
        if row == r:
          reverse= True
      if reverse:
        offset-=1
      else: offset +=1
    
    return sum

  for row in range(d-1, height-d+1):
    for col in range(d-1, width-d+1):
      maxSum = max(maxSum, getDiamondSum(row, col))
  return maxSum
m3 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

m4 = [
  [1, 2, 3, 1],
  [4, 5, 6, 1],
  [7, 8, 9, 1],
  [1, 1, 1, 1],
]

m5 = [
  [1, 2, 3, 1, 1],
  [4, 5, 6, 1, 1],
  [7, 8, 9, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1],
]
print(maxDiamondSum(m3, 1))
print(maxDiamondSum(m3, 2))
print(maxDiamondSum(m4, 1))
print(maxDiamondSum(m4, 2))
print(maxDiamondSum(m4, 3))
print(maxDiamondSum(m5, 3))