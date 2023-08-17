'''
❓ PROMPT
Given an array of Fellows representing nominations for a Rising Tide Award at Formation, return the name of the winning Fellow with the most number of nominations

Example(s)
risingTideWinner(["oliver", "pixel", "pinky", "pixel"]) == "pixel"

🔎 EXPLORE
List your assumptions & discoveries:
 
Insightful & revealing test cases:

'''
'''

🧠 BRAINSTORM
What approaches could work? 
keep a dictionary of appereances
and also a variable to store the Fellow with the most nominations 

Algorithm 1:
Time: O(n) where n is the number of fellows
Space: O(f) we will have a dictionary the lenght of the number of fellows by the end
 
📆 PLAN
Outline of algorithm #: 

initialize dictionary
initialize risingTideWinner with None and -inf

traverse list of  nominations:
    add or update nominated person count 
    update the winner if the current count surpasses the risingTideWinner's count

return risingTideWinner


🛠️ IMPLEMENT
function risingTideWinner(nominations) {
def risingTideWinner(nominations: list[str]) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def risingTideWinner(nominations):

    tally = {}
    risingTideWinner = (None, float("-inf"))
    for nom in nominations:

        tally[nom] = count =  tally.get(nom, 0) +1

        if count >  risingTideWinner[1]:
            risingTideWinner = (nom, count)

    return risingTideWinner[0]

print(risingTideWinner(["oliver", "pixel", "pinky", "pixel"]) == "pixel")
print(risingTideWinner(["oliver", "pixel", "pinky", "pixel", "pinky", "pinky"]) == "pinky")
print(risingTideWinner(["oliver", "pixel", "pinky", "oliver"]) == "oliver")


