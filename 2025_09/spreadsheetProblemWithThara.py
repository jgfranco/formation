
'''
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id.
 

EXAMPLE(S)
1 => "A"
26 => "Z"   
27 => "AA"
AB
AC
         
123456789ABCDEF

base 26 


A  A
   26~0 = 1 
26~1 = 26   

use a map A:1
          B:2

chr()
ord()

pass 1.                pass 2
28%26 = 2 (B).        1 %26 = 1 (A)
27 // 26 = 1          1 // 26 = 0
25%26  = 25

n-1//2 
n-1%2 

1

0 => A
1 => 

1000-1%26 = 11 (L)
1000-1  // 26
38-1 % 26. = 11(L)
38-1 //26 = 1
1-1 % 26 = 0 (A)
1// 26 

ALL



FUNCTION SIGNATURE
func spreadsheetRep(_ columnNumber: Int) -> String

'''

def spreadsheetRep(columnNumber):
    result = ""

    while columnNumber > 0:
        columnNumber -= 1
        digit = columnNumber % 26       
        letter = chr(ord('A') + digit)
        result = letter + result
        columnNumber //= 26

    return result



print(spreadsheetRep(1))
print(spreadsheetRep(26))
print(spreadsheetRep(27))
print(spreadsheetRep(1000))




# https://www.dailycodingproblem.com/solution/212?token=391d7b796696a9bfc060292e2f8935e4f599a95a7269e58009cb4ae099ddb84f70e68702