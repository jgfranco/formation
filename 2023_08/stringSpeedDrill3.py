"""
Given a string, find the character that appears most frequently. You may assume there is only one most frequent character.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] char
"""

def solution(string):
    
    charMap = {}
    mostFreq = (None, float('-inf'))
    
    for char in string:
        charMap[char] = count = charMap.get(char, 0) +1
        
        if count > mostFreq[1]:
            mostFreq = (char, count)
            
    
    return mostFreq[0]


"""
Given a string, capitalize the letters at odd positions. The first position of the letter in a string is 1.

Example:
Input: form ation
output: FoRm AtIoN

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] string
"""
def solution(string):
    
    nstring = ""
    spaces = 0
    for i, char in enumerate(string):
        if char == " ": 
            spaces +=1
            nstring += char
            continue
        if (i+1-spaces) %2 != 0:
            nstring += char.upper()
        else:
            nstring += char
            
    return nstring
            
"""
Given a string, remove any extra spaces between words (or other non-space characters), keeping only one. You must also remove any trailing or leading spaces so that the first and last character in the resulting string is not a space.

Example:
Input: " Hello World! "
Output: "Hello World!"
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] string
"""

def solution(string):

    wordsArray = string.split(" ")
    filteredWords = filter(lambda x: x != "", wordsArray )    
    
    return " ".join(filteredWords)

"""
Given a sentence, find the first occurring longest word excluding punctuation marks (e.g. , . ! ?).

Example:
Input: "Look! I am flying"
Output: "flying"

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string string

[output] string
"""

def solution(string):

    words = string.split(" ")
    print(words)
    longestWord = (None, 0)
    excluded = [',', '.', '!', '?']
    
    for word in words:
        
        if len(word) >= longestWord[1]:
            counter = 0
            for char in word:
                if char not in excluded:
                    counter +=1
                    
            if counter > longestWord[1]:
                longestWord = (word, counter)
    
    if not longestWord[0]: return ""
    return longestWord[0]

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
    newString = ""
    for char in string:
        if char == " ":
            newString += " "
        else:
            if char not in visited:
                visited.add(char)
                newString+= char
    
    return newString