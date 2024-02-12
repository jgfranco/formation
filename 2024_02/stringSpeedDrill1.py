"""
Q. Given a string, remove any extra spaces between words (or other non-space characters), keeping only one. You must also remove any trailing or leading spaces so that the first and last character in the resulting string is not a space.

Example:
Input: " Hello World! "
Output: "Hello World!"
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] string
"""
def solution(string):
    string = string.split(" ");

    s = []
    
    for word in string:
        if word != "": s.append(word)
        
    return (" ").join(s)


"""
Q. Given a substring sub and an input string full, remove all non-overlapping occurrences of sub from full.

Input: full: "abc" & sub: "ab"
Expected Output: "c"
Input: full: "ababab" & sub: "b"
Expected Output: "aaa"
Input: full: "abcabcabcabcabc" & sub: "abcba"
Expected Output: "abcabcabcabcabc"
because "abcba" doesn't appears in the 'full' string.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string full

[input] string sub

[output] string

"""

"""Q. Given a string, capitalize all lower case letters.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] string

[Python 3] Syntax Tips
"""


def solution(string):

    newS = ""
    for i, char in enumerate(string):
        if string[i].islower():
            newS += char.upper()
        else:
            newS += char
    return newS
        

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
    vowelStack = []
    
    vowels = ["A", "a","E","e","I","i","O","o","U","u"]
    
    for char in s:
        if char in vowels:
            vowelStack.append(char)
            
    newString = ""
    for char in s:
        if char in vowels:
            newString += vowelStack.pop()
        else:
            newString += char
            
    return newString

"""
Q. Given a string and a target string, count the number of times the target string shows up in the input string. String parts that were already counted cannot be counted again (no overlapping allowed).

Example:
Input: "111", target = "11"
Output: 1 (if the overlapping was allowed, the answer would be 2)

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[input] string target

[output] integer
"""

def solution(string, target):
    if target == "": return 0
    lTarget = len(target)
    
    pointer = 0
    counter = 0
    while pointer < len(string):
        if string[pointer: pointer + lTarget] == target:
            pointer += lTarget
            counter += 1
        else:
            pointer +=1
    return counter 
