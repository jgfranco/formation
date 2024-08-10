'''
Longest Substring No Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
 

EXAMPLE(S)
Input: "abcabcbb"
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
func longestSubstringLength(input: String) -> Int

Constaints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

Brainstorm:
    Naive -> Create every possible substring and iterate through all to check

    More optimal Naive ->
        Double for loop iterating while no duplicate is found

    two pointer -> iterate through string adding each char to a hashmap
        -> If we find a char that already exists in the hashmap
        -> check length for new max
        -> iterate left pointer removing chars from hashmap until there is no dup
    continue until end
    max length

Psuedo - Code
init left pointer, max_seen
init seen set
iterate through all chars using enumerate (r, char)
    if char in seen:
        check max_seen versus current
    while char in seen:
        seen.remove(s[l])
        l+=1
    seen.add(char)
check max_seen versus current
return max_seen
 
p w w k e w
      l
           r
seen = {k, e}
seen_max = r-l
'''

def longestSubstringLength(s):
    left = max_seen = 0
    seen = set()

    for r, char in enumerate(s):
        if char in seen:
            max_seen = max(max_seen, len(seen))
        while char in seen:
            seen.remove(s[left])
            left += 1
        seen.add(char)
    max_seen = max(max_seen, len(seen))
    return max_seen

print(longestSubstringLength('abcabcbb') == 3)

print(longestSubstringLength('bbbbb') == 1)

print(longestSubstringLength('abcd') == 4)

print(longestSubstringLength('a') == 1)

print(longestSubstringLength('pwwkew') == 3)

print(longestSubstringLength('') == 0)

print(longestSubstringLength("abcabcbb") == 3)
print(longestSubstringLength("bbbbb") == 1)
print(longestSubstringLength("pwwkew") == 3)
print(longestSubstringLength("") == 0)
print(longestSubstringLength("abcdefghijklmnopqrstuvwxyz") == 26)
'''
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def length_of_longest_substring(s):
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