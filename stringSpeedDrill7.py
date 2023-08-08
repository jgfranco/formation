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
    vowels = ['a', 'e', 'i', 'o' ,'u', 'A', 'E', 'I', 'O' ,'U']
    stack = []
    
    for char in s:
        if char in vowels:
            stack.append(char)
            
    newString = ""
    for char in s:
        if char in vowels:
            newString += stack.pop()
        else: newString += char
        
    
    return newString
"""
Given a string s consisting of Latin letters and digits, change each of its digit to the corresponding number of ones.

Example

For s = "abc5bc3", the output should be solution(s) = "abc11111bc111".

We change digit 5 to five ones and digit 3 to three ones.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string s

The string consisting of Latin letters and digits.

Guaranteed constraints:
1 ≤ s.length ≤ 100.

[output] string

The input string with digits replaced to the corresponding number of ones.
"""
def solution(s):
    
    nString = ""
    for char in s:
        if char.isdigit():
            for _ in range(int(char)):
                nString+= "1"
        else:
            nString += char
    
    return nString
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
    nString = ""
    
    for char in string:
        if char == " ": 
            nString += char
            continue
        if char not in visited:
            visited.add(char)
            nString +=  char
        
    return nString
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
    count =0
    
    for char in s:
        if char in vowels:
            count +=1
        else:
            count +=2
            
    return count
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
    s3 = ""
    
    p1 = p2 = 0
    
    remainder = 0
    while p1 < len(s1) and p2 < len(s2):
        
        currSum = int(s1[p1]) + int(s2[p2]) + remainder
        remainder = 0
        
        if currSum > 9:
            s3 += str(currSum % 10)
            remainder = currSum // 10
        else:
            s3 +=str(currSum)
            
        p1 +=1
        p2 +=1
    
    while p1 < len(s1):
        
        currSum = int(s1[p1]) + remainder
        remainder = 0
        
        if currSum > 9:
            s3 += str(currSum % 10)
            remainder = currSum // 10
        else:
            s3 +=str(currSum)
        
        p1 +=1
            
    while p2 < len(s2):
        
        currSum = int(s2[p2]) + remainder
        remainder = 0
        
        if currSum > 9:
            s3 += str(currSum % 10)
            remainder = currSum // 10
        else:
            s3 +=str(currSum)
            
        p2 +=1
    
    print(remainder)
    if remainder != 0: 
        s3 += str(remainder)
        
    return s3[::-1]

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
    if string1 == "": return string2
    if string2 == "": return string1

    words1 = string1.split(" ")
    words2 = string2.split(" ")
    
    p1 = p2 = 0
    words3 = []
    while p1 < len(words1) and p2 < len(words2):
        words3.append(words1[p1])
        words3.append(words2[p2])
        p1 +=1
        p2 +=1
        
    while p1 < len(words1) :
        words3.append(words1[p1])
        p1 +=1
        
    while p2 < len(words2) :
        words3.append(words2[p2])
        p2 +=1
        
    return " ".join(words3)