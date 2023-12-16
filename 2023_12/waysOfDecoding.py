
'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of unique ways to decode it.
 

EXAMPLE(S)
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Input: "102"
Output: 1
Explanation: It can only be decoded as "JB" (10 2).
 
1234
1 02


leading zeroes should be ignored

100 -> 0


227


     2      22
   2  27   7   #
7    #


POINTER = 0


_
26 6

FUNCTION SIGNATURE
func decodeWays(input: String) -> Int


valid paths counter 

recursive function (input, pointer)
    base case pointer is out of bounds:
        increment valid paths
        return

    check if char at pointer is a valid letter
        recursive call on pointer+1
    else: 
        return 
    check if chars at pointer and pointer +1 is valid
        recursive call on pointer2
    else:
        return

'''

def decodeWays(input: str) -> int:
    
    #check for empty string
    if len(input) == 0: return 0
    validWays = 0

    def decodeWaysRec(input, p):
        nonlocal validWays
        if p >= len(input):
            validWays +=1
            return
        
        #not taking 0 into account 


        """
        input 12
        pointer =1
        """

        if int(input[p]) >0: 
            decodeWaysRec(input, p+1)
        else: return
            
        if p+2 <= len(input) and int(input[p:p+2]) <=26:
            decodeWaysRec(input, p+2)
        else: return 

    decodeWaysRec(input, 0)
    return validWays

# O(n) time & space
def numDecodings(self, s: str) -> int:
    # if input is invalid return 0 right away
    if not s or s[0] == '0': return 0
    
    # create a memo to cache the number of ways to reach each position in the string
    memo = [0 for _ in range(len(s))]
    # only one way to reach the first position
    memo[0] = 1
    
    for i in range(1, len(s)):
        # if s[i] is not 0, it can be replaced by a letter encoded by a digit between 1 and 9
        if 1 <= int(s[i]) <= 9:
            memo[i] += memo[i-1]
        # if the position can be reached by a letter encoded by 2 digits, add the number of ways to reach position i-2
        if 10 <= int(s[i-1:i+1]) <= 26:
            memo[i] += memo[i-2] if i-2 >= 0 else 1
    
    return memo[len(s)-1]




assert decodeWays("0") == 0
assert decodeWays("01") == 0
assert decodeWays("31") == 1
assert decodeWays("102") == 1
assert decodeWays("12") == 2
assert decodeWays("226") == 3
assert decodeWays("102") == 1
    