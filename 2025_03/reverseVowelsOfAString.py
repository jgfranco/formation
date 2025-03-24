'''
https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

'''


def reverseVowels(s: str) -> str:
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    letters = list(s)
    i = 0
    j = len(s)-1
    
    while i<j:
        if letters[i] in vowels and letters[j] in vowels:
            letters[i], letters[j] = letters[j], letters[i]
            i +=1
            j -=1
        elif letters[i] not in vowels:
            i +=1
        elif letters[j] not in vowels:
            j -=1
            
    return "".join(letters)

print(reverseVowels("hello"), "holle") # holle
print(reverseVowels("leetcode"), "leotcede") # leotcede    
print(reverseVowels("aA"), "Aa") # Aa