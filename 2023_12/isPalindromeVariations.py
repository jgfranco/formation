def isPalindrome1(text):
    return text == text[0:len(text):-1]


def isPalindrome2(text):
    start = 0
    end  = len(text) - 1

    while start < end:
        if text[start] != text[end]:
            return False
        
        start += 1
        end -= 1

    return True


def findLongestOddPalindromeAt(text, index):
    start = end = index

    while start >= 0 and end < len(text) and  text[start] == text[end]:
        start -= 1
        end += 1
    
    return end - start -1


def isPalindromeRecursive(text):
    
    def helper(offset):
        start = offset 
        end = len(text) - offset - 1

        if start >= end: return True
        if text[start] != text[end]: return False

        return helper(offset+1)
    
    return helper(0)


#                  r-1 r
#              l   
#      7 4 2 2 3 6 1 1 9 9 9 
#      0 1 2 3 4 5 6 7 8 9 A
#          ------^----
#    r - l - 1
#
#      1 1 2 2 3 6 1 1 0 0 
#     l                    r

def findMountainWidth(numbers, index): 
    right = index + 1
    left = index - 1

    while True:
        if left < 0: break
        if numbers[left] > numbers[left + 1]: break
        left -= 1

    while True:
        if right >=  len(numbers): break
        if numbers[right] > numbers[right - 1]: break
        right += 1

    return right - left - 1
