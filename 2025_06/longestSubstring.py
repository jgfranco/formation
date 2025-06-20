'''
Longest Substring No Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
 

EXAMPLE(S)
Input: "abcabcbb"
                |
                |


(a,b,c)
result = 3
"abcbbcbb"
   l
     xr

Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

FUNCTION SIGNATURE
function longestSubstringLength(input)
def longest_substring_length(input)

#if input == 1:
    return

iterate through input

    create a set
    while the right pointer is less than the length of the array
        if the value of the right pointer is within the set
            update the result length of the set
            while the left element is not equal to the right element
                keep incrementing until the values match 
                increase index + 1 of left
                remove character from the set. 
    
    return the result
        
'''

def longest_substring_length(input):
    left = max_seen = 0
    seen = set()

    for char in input:
        if char in seen:
            while char in seen:
                seen.remove(input[left])
                left += 1
        seen.add(char)
        max_seen = max(max_seen, len(seen))

    return max_seen
    
print(longest_substring_length("abcabcbb") == 3)
print(longest_substring_length("bbbbb") == 1)
print(longest_substring_length("pwwkew") == 3)
print(longest_substring_length("") == 0)
print(longest_substring_length("abcdefghijklmnopqrstuvwxyz") == 26)


def longest_substring_length(s):
    if len(s) < 2:
        return len(s)

    longest = 0
    char_set = set()
    start_index = 0

    for i, char in enumerate(s):
        if char in char_set:
            # Remove characters from the beginning until the duplicate is removed
            while s[start_index] != char:
                char_set.remove(s[start_index])
                start_index += 1
            start_index += 1  # Move past the duplicate
        else:
            char_set.add(char)

        # Update the length of the longest substring
        longest = max(longest, i - start_index + 1)

    return longest