'''
❓ PROMPT
Given an input dictionary mapping from the name of Fellows to their numerical skill rating, return the skill rating with the highest number of Fellows.

Example(s)
{"oliver": 3, "pixel": 1, "pinky": 3} => 3
 

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
function highestSkillOverlap(fellowSkills) {
'''
def highestSkillOverlap(fellowSkills: dict) -> int:
  skillMap = {}
  highestSkill = (None, 0)
  
  for rate in fellowSkills.values():
    skillMap[rate] = current =  skillMap.get(rate, 0)+1

    if current > highestSkill[1]:
      highestSkill = (rate, current)

  
  return highestSkill[0]

'''
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

print(highestSkillOverlap({"oliver": 3, "pixel": 1, "pinky": 3}), "expect 3")
print(highestSkillOverlap({"oliver": 1, "pixel": 1, "pinky": 3}), "expect 1")
print(highestSkillOverlap({"oliver": 1, "pixel": 1, "pinky": 3, "ken": 3, "roman": 3 }), "expect 3")