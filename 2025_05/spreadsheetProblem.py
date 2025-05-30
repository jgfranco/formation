


'''
In most spreadsheets, the rows are named with numbers (starting at 1), and the columns are given names that are strings of capital letters. The first column is 'A', the second is 'B' up to the 26th which is 'Z'. At that point, they progress to 'AA' for 27, then 'AB' for 28, etc.

As part of our new product, we need functions to convert between these column header strings and their ordinal values, and vice versa!

Start out with the column-header-to-ordinal direction. If you get that working, do the inverse!

The challenges arise from our labeling system not having a character that represents zero. This problem will make you thankful that ancient Babylonian, Chinese, and other civilizations came up with the idea of zero.
 

Engineering method:
Explore
Brainstorm
Implement
Verify

Questions:
- Upper limit: whatever the python upper limit is for an int


similar to int to binary (convert to and from base26)

no zero means we need to offset value by 1


ABC = 3 * 26 ^ 0 + 2 * 26 ^ 1 + 1 * 26 ^ 2


xxxx = sum (value of x represent * 26 ^ digit), digit here from 0 to the (length of the given string - 1),
ord('x')  - ord('A') + 1 value of x represent.


ex1: 
A = 1
Z = 26
AA = 27
AB 
AC
AZ = 27 + 26 - 1 = 52
...
ZA
ZB
...
ZZ = (val of z * 26 ^ 1) + (val of z * 26 ^ 0), val = ord('Z') - ord('A') + 1 = 25 + 1 = 26
   = 26 * 26 + 26 * 1 = 702

_____

ordinalToColumn:
initialize a string 
ordinal -=1
 char = chr((ordinal % 26) + ord('A'))

result = char + result





EXAMPLE(S)
columnToOrdinal("A") => 1
columnToOrdinal("J") =>10
columnToOrdinal("Z") => 26
columnToOrdinal('AA') => 27
columnToOrdinal('AB') =>28

ordinalToColumn(1) =>"A"
ordinalToColumn(26) => "Z"
ordinalToColumn(27) => "AA"
ordinalToColumn(52) => "AZ"
 

FUNCTION SIGNATURE
function columnToOrdinal(headerStr)
function ordinalToColumn(ord)
'''


def columnToOrdinal(input):

   for c in input:
      if ord(c) < ord('A') or ord(c) > ord('Z'):
         print("invalid input")
         return -1

   count = 0
   power = 0
   for i in range(len(input) - 1, -1, -1):
      c = input[i]
      val = ord(c) - ord('A') + 1
      count += val * (26 ** power)
      power += 1
      #print(f"c = {c}, val = {val}, count = {count}, power = {power}")
   
   return count

"""
print(columnToOrdinal("A"))
print(columnToOrdinal("J"))
print(columnToOrdinal("Z"))
print(columnToOrdinal("AA"))
print(columnToOrdinal("AB"))
print(columnToOrdinal("ZZ"), "702")
"""

print(columnToOrdinal("99999"))

def ordinalToColumn(ordinal):
   result = ""

   while ordinal > 0:
      ordinal -= 1
      char = chr((ordinal % 26) + ord('A'))
      result = char + result
      ordinal //= 26
   
   return result

print(ordinalToColumn(1))
print(ordinalToColumn(26))
print(ordinalToColumn(27))
print(ordinalToColumn(52))
print(ordinalToColumn(702))


def validation(input: str):
   check = (input == ordinalToColumn(columnToOrdinal(input)))
   print(check)

   return 


validation("A")
validation("ZZ")

def toOneThousand():
   for i in range(1, 10_001):
      if  i != columnToOrdinal( ordinalToColumn(i)): return False
   
   return True
      

print(toOneThousand())