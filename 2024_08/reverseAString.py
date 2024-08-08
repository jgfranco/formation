'''
❓ PROMPT
Because strings are immutable, this problem takes more work than it does for an array. With an array, we can move individual values around and assign them into different locations. But with a string, we need to actually create an entirely new one.

Yes, in many modern languages this can be done with built in methods, but here we're working on basic coding patterns and coding fluency. We're going to mostly write this out.

Example(s)
reverseString("noitamroF") => "Formation"
 

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
function reverseString(s)
def reverseString(s):
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
def reverseString(s):
  result = ""

  for char in s:
    result = char + result
  return result

def reverseString2(s):
  result = []
  for i in range(len(s)-1, -1, -1):
    result.append(s[i])
  
  return "".join(result)

def reverseString3(s):
  
  array = [*s]

  for i in range(0, len(s)//2):
    array[i], array[-i-1] = array[-i-1], array[i]
  
  return "".join(array)


print(reverseString("noitamroF"))
print(reverseString2("noitamroF"))
print(reverseString3("noitamroF"))
print(reverseString3("tset"))
print(reverseString3("xaM"))

print(reverseString3("MP"))

print(reverseString3("K"))