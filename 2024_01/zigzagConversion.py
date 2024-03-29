"""
6. Zigzag Conversion
Medium

7151

13986

Add to List

Share
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

class Solution:
  def convert(self, s: str, numRows: int) -> str:
    """
    approach 1: use the rows as buckets
    """
    if numRows ==1: return s
    
    top = 0
    bottom = numRows -1
    direction = 1
    pointer = 0
    
    rows = [[] for _ in range(numRows)]

    for char in s:
      rows[pointer].append(char)
      if pointer == bottom: 
          direction = -1
      if pointer == top:
          direction = 1
      
      pointer += direction 
    
    for i in range(numRows):
      rows[i] = "".join(rows[i])
        
    return "".join(rows)
    
    