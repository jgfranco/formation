'''
1. isPalindrome
This is an easier version of the original problem. In this variation, simply return true if the string is a palindrome and false otherwise.
Ex.
“abcba” → true
“a” → true
“ab” → false


2. lmps function solution
In this version, you must use a helper function to solve the problem. This helper function takes the input string and an index. You should expand from the center from the index and return the longest palindromic substring centered around that index. Your code should roughly look like this (translated into your language):

func lps(input: String) -> String {
    let longest = ""
    for i in range(input.length) {
        result = lps(input, i)
        longest = result.length > longest ? result : longest
    }
    return longest
}
func lps(input: String, index: i) -> String {
     // Your code
}



3. Longest palindromic mountainous subsequence
A mountainous sequence is an array that monotonically increases to a peak and then monotonically decreases. A palindromic mountainous sequence increases for the same amount of time as it decreases. It must have a singular peak:


    l  _  r
[0, 2, 5, 3, 1] is valid
[1]
[1,5]
 [1] or [5] 

[0, 1, 2, 2, 1, 0] is not valid because it does not have a singular peak.
Given an array, find the longest palindromic mountainous subsequence:
Ex.
[1, 0, 2, 5, 3, 1, 4, 6, 1] returns [0, 2, 5, 3, 1]




4. Longest symmetric sum subsequence
A symmetric sum subsequence is one where pairs of numbers equidistant from the center sum to the center. Let’s take this sequence as an example:
[7, 2, 10, 8, 3]
In this sequence, 10 is the center element. The two numbers at distance 1 from it are 2 and 8, which sum up to 10. The two numbers at distance 2 from it are 7 and 3, which also sum up to 10, so it is a valid symmetric sum sequence.
Given an array, find the longest symmetric sum subsequence:
Ex.
[1, 1, 5, 5, 0, 4, 4, 6, 1] returns [1, 1, 5, 5, 0, 4, 4]
'''

def isPalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1

    return True
print(isPalindrome("a")) # true
print(isPalindrome("aba")) # true
print(isPalindrome("aac"))#false

"""
func lps(input: String) -> String {
    let longest = ""
    for i in range(input.length) {
        result = lps(input, i)
        longest = result.length > longest ? result : longest
    }
    return longest
}
func lps(input: String, index: i) -> String {
     // Your code
}
"""
def helper(s, i):
    if i == 0:
        return s[0]
    elif i==len(s)-1:
        return s[-1]

    l,r = i-1,i+1
    # print(i,l,r)
    while l>=0 and r<len(s):
        if s[l] != s[r]:
            return s[l+1:r] # s[l+1 : r]
            #s[1:2]
        l-=1
        r+=1

    return s


def lps(s):
    longest = ""
    for i in range(len(s)):
        result = helper(s, i)
        # print(i,result)
        longest = result if len(result) > len(longest) else longest
    return longest


# print(lps("a")) # a
# print(lps("aba")) # aba
print(lps("aac"))#a

# [1, 0, 2, 5, 3, 1, 4, 6, 1] returns [0, 2, 5, 3, 1]
def lpms(numbers):

    longest = [numbers[0]]
    for i in range(len(numbers)):
        temp = lmpshelper(numbers, i)
        if len(temp) > len(longest):
            longest = temp
    
    return longest
        

def lmpshelper(numbers, index):

    left = index - 1 
    right = index + 1

    while left>=0 and right < len(numbers):
        if numbers[left] > numbers[left +1] or numbers[right] > numbers[right -1]:
            return numbers[left+1:right]
        #continue if left<left+1 and right<right-1
    #negation is not (left<left+1 and right<right-1)    
        
        left -= 1
        right += 1 
    return numbers[left+1:right]

print(lpms([1, 0, 2, 5, 3, 1, 4, 6, 1]), [0, 2, 5, 3, 1])