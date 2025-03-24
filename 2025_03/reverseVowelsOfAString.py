'''
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