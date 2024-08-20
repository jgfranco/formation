"""
// Given an input string s, reverse the order of the words.

// A word is defined as a sequence of non - space characters.The words in s will be separated by at least one space.

// Return a string of the words in reverse order concatenated by a single space.

// Note that s may contain leading or trailing spaces or multiple spaces between two words.The returned string should only have a single space separating the words.Do not include any extra spaces.



//   Example 1:

// Input: s = "the sky is blue"
// Output: "blue is sky the"
// Example 2:

// Input: s = "  hello world  "
// Output: "world hello"
// Explanation: Your reversed string should not contain leading or trailing spaces.
//   Example 3:

// Input: s = "a good   example"
// Output: "example good a"
// Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


//   Constraints:

// 1 <= s.length <= 104
// s contains English letters(upper -case and lower -case), digits, and spaces ' '.
// There is at least one word in s.

"""
def reverseWords(s):

    words = s.split(" ")

    if len(words) <= 1: return s

    result = []
    for word in words:
        if word != "":
            result.append(word)
    
    return " ".join(result[::-1])


print(reverseWords("the sky is blue"))
print(reverseWords("a good   example"))
print(reverseWords("  hello world  "))


# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
 
# [-10,-2, 1,2,3,4]

# -10 * -2 * 4
# the three largest numners 2*3*4


# Constraints:

# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000

def maximumProductOfThree(array):

    array = sorted(array)
    firstTwoLastOne = array[0] * array[1] * array[-1]  
    largest = array[-1] * array[-2] * array[-3]

    return max(firstTwoLastOne, largest)


print(maximumProductOfThree([1,2,3])) # 6
print(maximumProductOfThree([1,2,3, 4])) # 24
print(maximumProductOfThree([-10,-2, 1,2,3,4])) # 80


# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

"""


    longestSoFar = 2
    visited set(p,w)
  12 
"pwwkew"
"""
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces. 

def longestSubstring(s):

    if s == "": return 0

    longestSoFar = 1
    visited = set()
    i = 0

    while i < len(s):
        visited.add(s[i])
        j = i+1
        while j < len(s) and s[j] not in visited:
            visited.add(s[j])
            j+=1
        longestSoFar = max(longestSoFar, len(visited))
        visited = set()
         
        i +=1
    
    return longestSoFar
        
print(longestSubstring("")) #0
print(longestSubstring("bbbbbb")) # 1
print(longestSubstring("abcabcbb")) # 3
print(longestSubstring("pwwkew")) # 3