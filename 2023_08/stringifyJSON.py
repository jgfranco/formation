'''
❓ PROMPT
You will be implementing a function called stringify which will take in a Javascript Object and return the JSON representation of the object as a string. This function is actually built into Javascript as `JSON.stringify(object)` but you have to write yours from scratch!

You may want to take a moment to review the rules for [JSON syntax](https://www.w3schools.com/js/js_json_syntax.asp).

Example(s)
anObj = {"x": 5, "y": "Oliver"}
stringify(anObj)
Output: {"x": 5, "y": "Oliver"}

aList = [1, "hello", "null", {"x": 5, "y": "Oliver"}]
stringify(aList)
Output: [1, "hello", "null", {"x": 5, "y": "Oliver"}]
 

🔎 EXPLORE
List your assumptions & discoveries:

types of objects:
  string
  number
  dictionary
  list
  None
 

Insightful & revealing test cases:
stringify({"key1": "value1", "key2": "null", "key3": {"subkey": 42}}) # we can have nested dictionaries or nested lists
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: recursive function, so we can handle nested objects

Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function stringify(obj) {
'''
def stringify(obj):
    if not obj: return None

    if type(obj)== int or type(obj)== float:
        return f'{obj}'
    elif type(obj) == str:
        return f'"{obj}"'
    elif type(obj) == list:
        result = []
        for element in obj:
            result.append(stringify(element))
        return f'[{", ".join(result)}]'
    elif type(obj) == dict:
        result = []
        for key, val in obj.items():
            result.append(f'"{key}": {stringify(val)}')
        return f'{{{", ".join(result)}}}' 
'''
🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

print(stringify(None) == None)

print(stringify("hello") == "\"hello\"")

print(stringify(42) ==  "42")

print(stringify(3.14) == "3.14")

print(stringify({"x": 5, "y": "Oliver"}) == "{\"x\": 5, \"y\": \"Oliver\"}")

# # Test list input
print(stringify([1, "hello", "null", {"x": 5, "y": "Oliver"}]) ==
   "[1, \"hello\", \"null\", {\"x\": 5, \"y\": \"Oliver\"}]")

# # Test dictionary input
print(stringify({"key1": "value1", "key2": "null", "key3": {"subkey": 42}}) ==
   "{\"key1\": \"value1\", \"key2\": \"null\", \"key3\": {\"subkey\": 42}}")