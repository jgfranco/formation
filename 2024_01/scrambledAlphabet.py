'''
❓ PROMPT
Imagine you arrive in a place with a very different language. As part of learning the language, you want to understand how words and letters are ordered. Unfortunately, you don't have a dictionary in this language that would give you the ordering of the characters, but you have been given a list of words that are in order, sorted [lexicographically](https://en.wikipedia.org/wiki/Lexicographic_order).

Given a list of words (strings) that are guaranteed to be in dictionary order, write a function that determines the order of letters. Return this as an array of single characters.

Example(s)
findLetterOrder(["gje", "ghf", "fe", "fh", "je", "ef"]) -> ["g", "f", "j", "e", "h"]
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function findLetterOrder(words)
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


def findLetterOrder(words):

  letterIdx = 0
  wordIdx = 0
  alphabet = []
  while words:
    if letterIdx >= len(words[wordIdx]):
      del words[wordIdx]
      if wordIdx >= len(words): wordIdx = 0
      continue
     
    letter = words[wordIdx][letterIdx]
    if letter not in alphabet:
      alphabet.append(letter)
    wordIdx +=1
    if wordIdx >= len(words):
      wordIdx = 0
      letterIdx +=1

  return alphabet


print(findLetterOrder(["gje", "ghf", "fe", "fh", "je", "ef"]))
print(findLetterOrder(["a", "be", "ebb"]) ==  [ 'a', 'b', 'e' ])
print(findLetterOrder(["a", "be", "beef", "ebb", "fab"]) == [ 'a', 'b', 'e', 'f' ])
print(findLetterOrder(["a", "ace", "be", "beef", "cab", "ebb", "fab"]) == [ 'a', 'b', 'c', 'e', 'f' ])
print(findLetterOrder(["a", "ace", "at", "be", "beef", "cab", "cat", "ebb", "fab", "tea"]) == [ 'a', 'b', 'c', 'e', 'f', 't' ])
print(findLetterOrder(["zoo", "yeti", "to", "too", "on", "no", "ney", "iota", "ion", "eno"])==  ['z', 'y', 't', 'o', 'n', 'i', 'e', 'a'])