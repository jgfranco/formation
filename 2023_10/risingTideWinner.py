'''
❓ PROMPT
Given an array of Fellows representing nominations for a Rising Tide Award at Formation, 
return the name of the winning Fellow with the most number of nominations

Example(s)
risingTideWinner(["oliver", "pixel", "pinky", "pixel"]) == "pixel"
 

🔎 EXPLORE
List your assumptions & discoveries:
  we need to traverse the whole list, because the winner could be determined by the last vote
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: use a map to save all the votes, sort it at the end and return the person with the most votes
Time: O(n) where n is the number of votes
Space: O(p) where p represents the number of fellows that were nominated. 

📆 PLAN
Outline of algorithm #: 

initialize a dictionary
traverse the nominations:
  save each nomination in the dictionary

sort the dictionary descending
return the first fellow in the sorted dictionary
 
🛠️ IMPLEMENT
function risingTideWinner(nominations) {
'''
def risingTideWinner(nominations: list[str]) -> str:
  fellowMap = {}

  for nomination in nominations:
    fellowMap[nomination] = fellowMap.get(nomination, 0) + 1
  
  sortedFellows = sorted(fellowMap.items(), key = lambda x: x[1], reverse=True)
  return sortedFellows[0][0]

'''

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

print(risingTideWinner(["roman", "pinky", "kendall", "pinky"]), "expect pinky")
print(risingTideWinner(["roman", "pinky", "kendall", "roman", "greg"]), "expect roman")
print(risingTideWinner(["roman", "pinky", "kendall", "tom", "greg", "tom"]), "expect tom")