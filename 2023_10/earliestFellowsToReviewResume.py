
'''
❓ PROMPT
We have Fellows at Formation that are waiting for their resume 
to be reviewed. Given an input dictionary mapping from Fellow 
name to an integer representing the timestamp they requested a 
review, return an array of Fellows that arrived earliest (at the exact same time)

Example(s)
fellowTimes = {"oliver": 3, "tobey": 3}
earliestFellows(fellowTimes) == ["oliver", "tobey"]

fellowTimes = {"oliver": 3, "pinky": 4, "pixel": 2, "tobey": 1}
earliestFellows(fellowTimes) == ["tobey"]
 

🔎 EXPLORE
List your assumptions & discoveries:
  I have to determine the earliest time and if also keep stored all of the people that fall in that timeslot =



🧠 BRAINSTORM
What approaches could work?
  keep an array of people at the earliest time
  reset array wheneve we find a smaller timestamp
Algorithm 1:
  use a earliestTime variable to keep track of the earlist Time
  Keep an array of people (at the earliest Time) 
  empty array whenever we find a smaller timestamp and store the current person
Time: O(n): we need to traverse the whole list of fellowTImes in order to determine the earliest Fellow(s)
Space: O(n): worst case scenario all the fellows in the list arrived at the same time
 

📆 PLAN
Outline of algorithm #: 

  set earliestTime as a +infinity number
  initialize a earliestFellows array
  traverse felloWTimes:
    if the fellwTime is smaller than earliestTime:
      update earlistTime to the current fellowTime
      empty array and store current fellow
    ignore timestamps that are larger than tue current earlies time
    if the fellow time is the same to the earlist time:
      append fellow to the array

  return array
 

🛠️ IMPLEMENT
function earliestFellows(fellowTimes) {
'''
def earliestFellows(fellowTimes: dict) -> list[str]:
  earliestTime = float("inf")
  earliestFellows = []

  for fellow, time in fellowTimes.items():
    if time < earliestTime:
      earliestTime = time
      earliestFellows = []
      earliestFellows.append(fellow)
    elif time == earliestTime:
      earliestFellows.append(fellow)
  return earliestFellows


'''

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
fellowTimes = {"oliver": 3}
print(earliestFellows(fellowTimes) == ["oliver"])

fellowTimes = {"oliver": 3, "tobey": 3}
print(earliestFellows(fellowTimes) == ["oliver", "tobey"])

fellowTimes = {"oliver": 3, "pinky": 4, "pixel": 2, "tobey": 1}
print(earliestFellows(fellowTimes) == ["tobey"])

fellowTimes = {"oliver": 3, "pinky": 1, "pixel": 2, "tobey": 1}
print(earliestFellows(fellowTimes) == ["pinky", "tobey"])

fellowTimes = {"tony": 3, "jess": 1, "paavo": 2, 
"zoe": 1, "ariel": 2, "jono": 1, "angus": 3}
print(earliestFellows(fellowTimes) == ["jess", "zoe", "jono"])