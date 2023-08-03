"""
Given a string s, return the index of the first non-repeating character. If there is no unique character, return -1.

Example:

Given "Formation" return 0 ("F" is the first non-repeating character).
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] integer
"""

def solution(string):

    charMap = {}
    deleted = []
    for idx, char in enumerate(string):
        
        if char in charMap:
            deleted.append(char)
            del charMap[char]
        else:
            if char not in deleted:
                charMap[char] = idx
         
    if len(charMap) ==0: return -1   
    indices = sorted(charMap.values())
    print(indices)
    return indices[0]
        
"""
Given an array of strings, find the longest common prefix amongst those strings. If there is none, return "".

Example:

Given ["Formation", "Form", "Formal"] returns "Form"
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.string strs

[output] string
"""
def solution(strs):
    prefix = strs[0]
    
    
    def getPrefix(str1, str2):
        
        p1 = p2 = 0
        prefix = ""
        while p1<len(str1) and p2 < len(str2):
            if str1[p1] == str2[p2]:
                prefix += str1[p1]
                
            p1+=1
            p2 +=1
        return prefix
    for i in range(1, len(strs)):
        
        prefix = getPrefix(prefix, strs[i])
        if prefix == "": return prefix
        
    return prefix


"""
Given two sentences, merge them into one by alternating words separated by a space. Start with a word from the first sentence.

Example:
Inputs: string1: "Happy Birthday", string2: ""Look! I am flying!"
Output: "Happy Look! Birthday I am flying!"

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string1

[input] string string2

[output] string
"""


def solution(string1, string2):
    
    if string1 == "" and string2 == "": return ""
    if string1 == "": return string2
    if string2 == "": return string1
    
    string1 = string1.split(" ")
    string2 = string2.split(" ")
    
    string3 = []
    
    p1 = 0
    p2 = 0
    
    while p1 < len(string1) and p2 < len(string2):
        string3.append(string1[p1])
        string3.append(string2[p2])
        
        p1 +=1
        p2 +=1
        
    while p1 < len(string1):
        string3.append(string1[p1])
        p1 +=1
    
    while p2 < len(string2):
        string3.append(string2[p2])
        p2 +=1
    
    
    return " ".join(string3)


"""
Given a string s containing "(", ")", "{", "}", "[", "]" only, determine if the input string follows:

Open brackets must be closed by the same pair:
e.g. "{" pairs with "}".
closed means "()", not ")(".
Open brackets must be closed in the correct order:
e.g. "({})" returns true.
"({)}" returns false.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string s

[output] boolean
"""
    

def solution(s):

    stack = []
    opening = {'}':'{', ')':'(', ']':'['}
    for char in s:
        
        if char in opening.values():
            stack.append(char)
        else:
            if stack and stack[-1]== opening[char]:
                stack.pop()
            else: return False
            
    return len(stack) == 0


"""
Given a string s of alphanumeric characters, determine if it is a palindrome. This should be agnostic of character casing and ignore spaces.

Examples:

Given "Formation", returns False
Given "FormrOf", returns True
Given "", returns True
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string s

[output] boolean
"""

def solution(s):
    
    s = s.split(" ")
    s = "".join(s)
    x = 0
    y = len(s) -1
    
    while x < y:
        
        if s[x].lower() != s[y].lower(): return False
        
        x += 1
        y -= 1
        
    return True


"""
Given a string, reverse it by character blocks of k.

Examples:

Input: string = "Formation", k = 3
Output: "roFtamnoi"  // Since k is 3, divide the string by a block of 3 characters: "For", "mat", and "ion" and reverse it by blocks.

If k doesn't evenly divide, just reverse last block left.
Input: string = Fellow, k = 4
Output: "lleFwo" // "Fell" and "ow"

If k exceeds the length of the array, do nothing.
Input: string = "Fellow, k = 7
Output: "Fellow"
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[input] integer k

[output] string
"""

def solution(string, k):
    if k <=1 or k > len(string): return string
    
    newString = ""
    for i in range(0, len(string), k):
        sub = string[i: i+k]
        newString += sub[::-1]
        
    return newString
