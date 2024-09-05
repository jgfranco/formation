

def columnToOrdinal(str):
    power = len(str) -1
    result = 0

    for char in str:
        value = ord(char) - ord('A') + 1
        result += value * (26**power)
        power -=1

    return result
print(columnToOrdinal("A"), 1)
print(columnToOrdinal("J"), 10)
print(columnToOrdinal("Z"), 26)
print(columnToOrdinal('AA'), 27)
print(columnToOrdinal('AB'), 28)
print(columnToOrdinal('AAA'), 703)


def ordinalToColumn(ordinal):
    result = ""

    while ordinal > 0:
        ordinal -=1
        char = chr(ordinal % 26 + ord('A'))
        result = char + result
        ordinal //= 26
    
    return result

print(ordinalToColumn(0) ,"")
print(ordinalToColumn(1) ,"A")
print(ordinalToColumn(26) , "Z")
print(ordinalToColumn(27) , "AA")
print(ordinalToColumn(52) , "AZ")
print(ordinalToColumn(703), "AAA")
print(ordinalToColumn(1), "A")
print(ordinalToColumn(25), "Y")
print(ordinalToColumn(26), "Z")
print(ordinalToColumn(27), "AA")
print(ordinalToColumn(52), "AZ")
print(ordinalToColumn(53), "BA")
print(ordinalToColumn(675), 'YY')
print(ordinalToColumn(676), 'YZ')
print(ordinalToColumn(677), 'ZA')
print(ordinalToColumn(701), "ZY")
print(ordinalToColumn(702), "ZZ")
print(ordinalToColumn(703), "AAA")