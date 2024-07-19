'''
Question :

In most spreadsheets, the rows are named with numbers (starting at 1), and the columns are given names that are strings of capital letters. The first column is 'A', the second is 'B' up to the 26th which is 'Z'. At that point, they progress to 'AA' for 27, then 'AB' for 28, etc.

As part of our new product, we need functions to convert between these column header strings and their ordinal values, and vice versa!

Start out with the column-header-to-ordinal direction. If you get that working, do the inverse!

The challenges arise from our labeling system not having a character that represents zero. This problem will make you thankful that ancient Babylonian, Chinese, and other civilizations came up with the idea of zero.
 

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

Edge cases/Assumptions/Observations : 
1. no wierd characters, and only uppercase, noempty strings
2. Ordinal cannot be 0

Approach : 
ord('A') : gives ordinal value of 'A'

 

FUNCTION SIGNATURE
function columnToOrdinal(headerStr)
function ordinalToColumn(ord)
'''

# def getOrd():
#     print(ord('A'))

# getOrd()

#  26 ^ 1 = 26 +  26 ^ 0 = 1
# A A

   
# B A = 53
# (26^ 1) *2 + (26^ 0) * 1


# Decimal number
# 175 = 100*1 + 10*7 + 1*5
#     = 10^2 * 1 + 10^1 * 7 + 10^0*5

def columnToOrdinal(headerStr):

    multiplier = len(headerStr) - 1
    result = 0
    for char in headerStr:
        ordValue = ord(char) - 64
        result += (26 ** multiplier) * ordValue
        multiplier -= 1
    
    return result

# print(columnToOrdinal("AZ"))

def ordinalToColumn(ordinal):

    
    column = ""

    while ordinal > 0:
        ordinal -= 1
        char  = chr((ordinal % 26) +65)
        column  = char + column
        ordinal = ordinal // 26

    return column


# print(ordinalToColumn(26))
# print(ordinalToColumn(53))

# chr(()
# 1 - 26 
 # 1 +64 = 65

 # 52 //26

# print(52/26)
# 27  = AA

# 27 // 26 = 1
# 1 // 26 = 0
 

# 1-- = 0
# 0+ord('A')
# = A

"""
51 % 26
0 + 65 = A
0 + 65 = A

52-1 = 51
1 = A
25 % 26  = Z
51/26 = 25


"""

print(columnToOrdinal("A") , 1)
print(columnToOrdinal("J") ,10)
print(columnToOrdinal("Z") , 26)
print(columnToOrdinal('AA') , 27)
print(columnToOrdinal('AB') ,28)

print(ordinalToColumn(1),"A")
print(ordinalToColumn(26) , "Z")
print(ordinalToColumn(27) , "AA")
print(ordinalToColumn(52) , "AZ")
