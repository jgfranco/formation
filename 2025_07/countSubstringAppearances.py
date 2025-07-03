def strCount(word: str,  sub: str) -> int:
    
    subLen  = len(sub)
    if len(word) < subLen: return 0

    if word[:subLen] == sub:
        return 1 + strCount(word[subLen:], sub)

    return strCount(word[1:], sub)


print(strCount("catcowcat", "cat") == 2)
print(strCount("catcowcat", "cow") == 1)
print(strCount("catcowcat", "dog") == 0)
print(strCount("cacatcowcat", "cat") == 2)
print(strCount("xyx", "x") == 2)
print(strCount("iiiijj", "i") == 4)
print(strCount("iiiijj", "ii") == 2)
print(strCount("iiiijj", "iii") == 1)
print(strCount("iiiijj", "j") == 2)
print(strCount("iiiijj", "jj") == 1)
print(strCount("aaabababab", "ab") == 4)
print(strCount("aaabababab", "aa") == 1)
print(strCount("aaabababab", "a") == 6)
print(strCount("aaabababab", "b") == 4)