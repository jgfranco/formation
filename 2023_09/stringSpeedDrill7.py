"""
Write a function that takes a string as input and returns the string with only the vowels reversed.
Note: The letters "a", "e", "i", "o", and "u" are vowels. The letter "y" is not a vowel.

Example

For s = "hello, world", the output should be
solution(s) = "hollo, werld";
For s = "codesignal", the output should be
solution(s) = "cadisegnol";
For s = "eIaOyU", the output should be
solution(s) = "UOaIye".

"""

def solution(s):
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels = []
    newString= []
    
    for char in s:
        if char in VOWELS:
            vowels.append(char)
    
    for char in s:
        if char in VOWELS:
            newString.append(vowels.pop())
        else: newString.append(char)
    
    return "".join(newString)
"""
Given a string s consisting of Latin letters and digits, change each of its digit to the corresponding number of ones.

Example

For s = "abc5bc3", the output should be solution(s) = "abc11111bc111".

We change digit 5 to five ones and digit 3 to three ones.
"""
def solution(s):
    numbers = ['0','1','2','3','4','5','6','7','8', '9']

    newString = []
    for char in s:
        if char in numbers:
            for _ in range(int(char)):
                newString.append("1")
        else:
            newString.append(char)
            
    return "".join(newString)
"""            
Given a string, remove all future occurrences of a character after the first occurrence. However, it should preserve all spaces.

Example:

Input: "I am happy"
Output: "I am hpy"
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] string
"""
def solution(string):
    visited = set()
    newString = []
    for char in string:
        if char == " " or char not in visited:
            newString.append(char)
            visited.add(char)
    return "".join(newString)
"""
You are given a string s that consists of only lowercase English letters. If vowels ('a', 'e', 'i', 'o', and 'u') are given a value of 1 and consonants are given a value of 2, return the sum of all of the letters in the input string.

Example

For s = "a", the output should be
solution(s) = 1;

For s = "abcde", the output should be
solution(s) = 8.

The letters in s, converted to 1s and 2s and added together as described above: 1 + 2 + 2 + 2 + 1 = 8.
"""
def solution(s):
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    SUM = 0
    for char in s:
        if char in vowels:
            SUM +=1
        else:
            SUM += 2
            
    return SUM
"""
Q. Given two non-negative integers represented as string, return their sum

Examples:

Given "111" and "11" return "122"
Give "0" and "123" return "123"
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string s1

[input] string s2

[output] string
"""
def solution(s1, s2):

    s1 = s1[::-1]
    s2 = s2[::-1]
    
    p1 = p2 = 0
    remainder = 0
    result = []
    while p1 < len(s1) and p2 < len(s2):
        current = int(s1[p1]) + int(s2[p2]) + remainder
        remainder = 0
        
        if current < 10:
            result.append(str(current))
            
        else:
            result.append(str(current%10))
            remainder = current//10
        
        p1 +=1
        p2 +=1
    
    while p1 < len(s1):
        current = int(s1[p1]) + remainder
        remainder = 0
        
        if current < 10:
            result.append(str(current))
        else:
            result.append(str(current%10))
            remainder = current//10
        p1 +=1
    
    while p2 < len(s2):
        current = int(s2[p2]) + remainder
        remainder = 0
        
        if current < 10:
            result.append(str(current))
        else:
            result.append(str(current%10))
            remainder = current//10
        p2 +=1
        
    if remainder != 0:
        result.append(str(remainder))
        
    result = result[::-1]
    return "".join(result) 
"""      
Q. Given two sentences, merge them into one by alternating words separated by a space. Start with a word from the first sentence.

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
    elif string1 == "": return string2
    elif string2 == "": return string1
    string1 = string1.split(" ")
    string2 = string2.split(" ")
    string3 = []
    while len(string1) > 0 or len(string2) > 0:
        
        if len(string1) >0:
            string3.append(string1.pop(0))
        if len(string2) >0:
            string3.append(string2.pop(0))
            
    return " ".join(string3)