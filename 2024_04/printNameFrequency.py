'''
❓ PROMPT
You're given a comma-separated string of names, and you want to print how 
many times each name appeared. For each person that appears, you should 
print a string *{name} appeared {x} times.*, in order of appearance.

To properly compare results in the test suite, return an array of strings 
joined by a newline as the result of your method.

return myArr.join("\n") // js
return "\n".join(myArr) # py

Example(s)
printNameFreq("Tony, Jessica, Paavo, Jessica, Tony, Zoe") ==
Tony appeared 2 times.
Jessica appeared 2 times.
Paavo appeared 1 time.
Zoe appeared 1 time.

printNameFreq("") == "Nobody appeared."
 

🔎 EXPLORE
List your assumptions & discoveries:
 
Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work? use a map as a count keeper
Algorithm 1:
Time: O(nlogn) where n is the amount of people, the log n is for the sorting
 of the map
Space: O(n) we will use a map to sort the algorithm
 

📆 PLAN
Outline of algorithm #: 

create a map, use names as keys, store the count as value
traverse the list of people update the map accordingly
  if the person is not in the map, store it in the map set count to 1
  otherwise, increment the count

  

create a result array
traverse the map:
  format and store the strings in the array

return result array


🛠️ IMPLEMENT
function printNameFreq(names) {
def printNameFreq(names: str) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def printNameFreq(names):
  if not names: return 'nobody appeared.'
  names = names.split(", ")
  nameCounter = {}

  for name in names:
    nameCounter[name] = nameCounter.get(name, 0) + 1
  
  result = []

  for name,count in nameCounter.items():
    sentence  = ""
    if count ==1:
      sentence = f'{name} appeared {count} time.'
    else:
      sentence = f'{name} appeared {count} times.'
    result.append(sentence)
  
  return "\n".join(result)


# test suite
print(printNameFreq("") == "nobody appeared.")
print(printNameFreq("Tony") == "Tony appeared 1 time.")
print(printNameFreq("Tony, Jessica") == 
"Tony appeared 1 time.\n\
Jessica appeared 1 time.")
print(printNameFreq("Tony, Tony, Tony") == "Tony appeared 3 times.")
print(printNameFreq("Tony, Jessica, Paavo, Zoe") ==
"Tony appeared 1 time.\n\
Jessica appeared 1 time.\n\
Paavo appeared 1 time.\n\
Zoe appeared 1 time.")
print(printNameFreq("Tony, Jessica, Paavo, Jessica, Tony, Zoe") == 
"Tony appeared 2 times.\n\
Jessica appeared 2 times.\n\
Paavo appeared 1 time.\n\
Zoe appeared 1 time.")