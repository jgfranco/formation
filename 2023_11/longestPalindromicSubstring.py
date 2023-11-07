'''
n this version, you must use a helper function to solve the problem. This helper function takes the input string and an index. You should expand from the center from the index and return the longest palindromic substring centered around that index. Your code should roughly look like this (translated into your language):

func lps(input: String) -> String {
    let longest = ""
    for i in range(input.length) {
        result = lpsHelper(input, i)
        longest = result.length > longest ? result : longest
    }
    return longest
}

func lpsHelper(input: String, index: i) -> String {
     // Your code
}

console.log(longestPalindromicSubstring("racecar"), "racecar")
console.log(longestPalindromicSubstring("cbabbabd") , "babbab")
console.log(longestPalindromicSubstring("abcdfefgh") , "fef")

"cbabbabd"
index: 1 , b
option 1: odd number --  xbx
option 2: even number  --> xb  --> yxby
'''

def lps(input):
  longest = ""
  for i in range(len(input)):
    result = lpsHelper(input, i)
    if len(result) > len(longest):
      longest = result
    
  return longest

# cbabba
def lpsHelper(str, idx):
  if len(str) ==1: return str
  if len(str) ==2 and str[0] == str[1]: return str
  p1 = p2 = idx
  
  if idx >1 and idx +1 < len(str) and str[idx-1] != str[idx+1]:
    if str[idx+1] == str[idx]:
      p2=idx+1
    else:
      return str[idx]


  print(idx, p1, p2)
  while(p1 >= 0  and p2 < len(str) and str[p1] == str[p2]):
    p1 -=1
    p2 +=1
  
  
  print(p1+1, p2)
  return str[p1+1:p2]


print(lps("abb") , "bb")
"""
print(lps("racecar"), "racecar")
print(lps("cbabbabdh") , "babbab")
print(lps("cbabbabd") , "babbab")
print(lps("abcdfefgh") , "fef")
print(lps("aaa") , "aaa")
print(lps("aa") , "aa")

print(lps("") , "")
print(lps("a") , "a")
"""