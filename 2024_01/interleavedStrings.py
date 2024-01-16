'''
❓ PROMPT
You have have seen this problem before as a backtracking problem. We'll now look at optimizing this using dynamic programming.

Given two strings *s1* and *s2* we can create an interleaving by repeatedly taking the first character of either and appending the characters together to form a new string, s3. Specifically, valid interleavings will have these properties:

1. len(s3) == len(s1) + len(s2)
2. *s3 - s1 = s2* and *s3 - s2 = s1* meaning that removing the characters in *s1* from the interleaving will produce *s2* and vice versa.
3. s1 and s2 both appear as subsequences in the interleaving, s3. The order of characters in s1 and s2 are preserved in s3.

Given *s1*, *s2*, and *s3*, write a function that determines whether *s3* is a valid interleaving of *s1* and *s2*.

Example(s)
These are some valid interleaving using the strings *ABC* and *BCD*:

isInterleaving("ABC", "BCD", "BABCCD") == True
Explanation:
 x:             AB C
 y:            B  C D
 interleaving: BABCCD

isInterleaving("ABC", "BCD", "ABCBCD") == True
Explanation:
 x:            ABC
 y:               BCD
 interleaving: ABCBCD

isInterleaving("ABC", "BCD", "BCDABC") == True
Explanation:
 x:               ABC
 y:            BCD
 interleaving: BCDABC

isInterleaving("ABC", "BCD", "BCABDC") == True
Explanation:
 x:              AB C
 y:            BC  D
 interleaving: BCABDC

isInterleaving("ABC", "BCD", "BABCDD") == False
Explanation:
BABCDD cannot be created from the any combination of the sequences ABC & BCD
 

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
function isInterleaving(x, y, s) {
def is_interleaving(x: str, y: str, s: str) -> bool:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def isInterleaving(x,y,s):
  m,n,l = len(x), len(y), len(s)
  if m+n != l:
    return False
  
  dp = [[False] * (n+1) for _ in range(m+1)]

  dp[0][0] = True
  #print(dp)

  for i in range(1, m +1):
    dp[i][0] = dp[i-1][0] and x[i-1] == s[i-1]
  print(dp)
  for j in range(1, n+1):
    dp[0][j] = dp[0][j-1]and y[j-1] == s[j-1]
  print(dp)
  for i in range(1, m+1):
    for j in range(1, n+1):
      dp[i][j] = (dp[i-1][j] and x[i-1] == s[i+j-1]) or (dp[i][j-1] and y[j-1] == s[i+j-1])

  return dp[m][n]


"""
print(isInterleaving("ABC","DEF", "ADBECF"))


print(isInterleaving("XXXXX", "YYYYY", "shorter") == False)
print(isInterleaving("X", "Y", "longer") == False)
print(isInterleaving("X", "Y", "XY") == True)
print(isInterleaving("X", "Y", "YX") == True)
print(isInterleaving("X", "Y", "XX") == False)
print(isInterleaving("X", "Y", "YY") == False)

print(isInterleaving("ABC", "D", "ABCD") == True)

print(isInterleaving("ABC", "D", "ABDC") == True)
print(isInterleaving("ABC", "D", "ADBC") == True)
print(isInterleaving("ABC", "D", "DABC") == True)
print(isInterleaving("AABCC", "DBBCA", "AADBBCBCAC") == True)
"""
print(isInterleaving("ABC", "BCD", "BABCCD") == True)
"""
print(isInterleaving("ABC", "BCD", "ABCBCD") == True)
print(isInterleaving("ABC", "BCD", "BCDABC") == True)
print(isInterleaving("ABC", "BCD", "BCABDC") == True)
print(isInterleaving("ABC", "BCD", "BABCDD") == False)
print(isInterleaving("ABC", "BCD", "ABBCCD") == True)
print(isInterleaving("ABC", "BCD", "DCCBBA") == False)
print(isInterleaving("ABC", "BCD", "ABBDCC") == False)
print(isInterleaving("ABC", "BCD", "ACBBCD") == False)
"""