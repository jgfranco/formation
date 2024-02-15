"""

isPalindrome

- two pointers, start and end, move them toward one another and check that they match
- reverse the string, then walk through both together
- push string into stack, then pop things out comparing against initial string
- recursive function takes an index from edge, checks current indexes against one another, then recurses with index + 1

"""

def isPalindrome(string):
    return string == string[::-1]

    
def isPalindrom2(text):
    start = 0
    end = len(text) - 1

    while(start < end):
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1

    return True


def isPalindrome3(text):
    if len(text) <= 1: return True

    if text[0] != text[-1]:
        return False
    
    return isPalindrome3(text[1:-1])

def isPalindrome4(text, sindex, eindex):
    if(sindex > eindex):
        return True
    if text[sindex] != text[eindex]:
        return False
    return isPalindrome4(text, sindex+1, eindex-1)

def isPalindrome5(text):
    def isPalindromePrivate(sindex, eindex):
        if(sindex > eindex):
            return True
        if text[sindex] != text[eindex]:
            return False
        return isPalindromePrivate(sindex+1, eindex-1)
    
    return isPalindromePrivate(0, len(text) -1)

# asdfghjjkl      1111aaabbbcccbbbaaa0000         bbbcccbbbaaa0000     1234554321
#      ^              -------^-------             ----^----                 ^
#                                                 012345678

def findLongestPalindromeAt(text: str, index: int, isEven: bool = False) -> int:

    start = end = index
    
    if isEven:
        start = index - 1

    while  start >= 0 and end < len(text):
        if text [start] != text[end]:
            break
        start -= 1
        end += 1

    return end - start + 1

def isPalindrome6(text):

    length = len(text)

    if length % 2 == 0: # Even
        return findLongestPalindromeAt(text, length//2, True)
    else: # Odd
        return findLongestPalindromeAt(text, length//2, False)


def isPalindrome7(text):
    length = len(text)
    isEven = length % 2 == 0
    
    return findLongestPalindromeAt(text, length // 2, isEven)
