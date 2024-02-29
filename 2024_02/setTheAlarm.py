
'''
❓ PROMPT
You're exhausted after a long day and heading to bed, 
but you still have to set the alarm clock on your phone. 
You already have one you set the day before, so all you have to do is update it.

To set your alarm, the hours and minutes are set independently, each by scrolling upwards or downwards. One shift changes an hour or minute value by one, up or down. The values are organized cyclically, which means that dragging 0 minutes downwards turns it into 59, and dragging 59 upwards turns it into 0 (similarly, 0 hours can become 23 in one shift and vice versa).

Given the time of the previous alarm and the new desired time, what is the minimum number of scroll moves to set the new time?

Example(s)
For setTime = "07:30" and timeToSet = "08:00", the output should be
minScrollToSet(oldTime, newTime) = 31.

Shifting hours upwards once will change the alarm to "08:30", 
and shifting minutes 30 times downwards will change it to "08:00".

minScrollToSet("7:30", "8:00") === 31
minScrollToSet("7:00", "6:31") === 30
minScrollToSet("7:00", "6:25") === 26
 

🔎 EXPLORE
List your assumptions & discoveries:
assert minScrollToSet("7:00", "6:31") == 30
assert minScrollToSet("7:00", "6:25") == 26
assert minScrollToSet("7:30", "8:00") == 31
assert minScrollToSet("7:00", "8:00") == 1
assert minScrollToSet("8:00", "8:00") == 0
assert minScrollToSet("6:59", "7:01") == 3
assert minScrollToSet("22:00", "2:00") == 4
assert minScrollToSet("12:00", "00:00") == 12
assert minScrollToSet("23:59", "00:00") == 2

distance to 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function minScrollToSet(oldTime, newTime) {
def minScrollToSet(oldTime: str, newTime: str) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

assert minScrollToSet("7:00", "6:31") == 30
assert minScrollToSet("7:00", "6:25") == 26
assert minScrollToSet("7:30", "8:00") == 31
assert minScrollToSet("7:00", "8:00") == 1
assert minScrollToSet("8:00", "8:00") == 0
assert minScrollToSet("6:59", "7:01") == 3
assert minScrollToSet("22:00", "2:00") == 4
assert minScrollToSet("12:00", "00:00") == 12
assert minScrollToSet("23:59", "00:00") == 2

'''


def minScrollToSet(oldTime, newTime):

  oldTimeHour, oldTimeMinutes = oldTime.split(":")
  newTimeHour, newTimeMinutes = newTime.split(":")
  oldTimeHour, oldTimeMinutes = int(oldTimeHour), int(oldTimeMinutes)
  newTimeHour, newTimeMinutes = int(newTimeHour),int( newTimeMinutes)

  # shortest distance to 00  or 24 for hours
  # shortest distance to 00 or 60 for minutes
  
  shortestHourDistance = abs(oldTimeHour - newTimeHour)
  
  oldHourDistanceToZero = min((oldTimeHour),(24 - oldTimeHour))
  newHourDistanceToZero = min((newTimeHour),(24 - newTimeHour))
  shortestHourDistance = min(shortestHourDistance, (oldHourDistanceToZero + newHourDistanceToZero))

  shortestMinuteDistance = abs(oldTimeMinutes - newTimeMinutes)

  oldMinutesDistanceToZero = min((oldTimeMinutes),(60 - oldTimeMinutes))
  newMinutesDistanceToZero = min((newTimeMinutes),(60 - newTimeMinutes))
  shortestMinuteDistance = min(shortestMinuteDistance, (oldMinutesDistanceToZero + newMinutesDistanceToZero))

  return shortestHourDistance + shortestMinuteDistance

print( minScrollToSet("7:00", "6:31") )# 30
print( minScrollToSet("7:00", "6:25") )# 26
print( minScrollToSet("7:30", "8:00") )# 31
print( minScrollToSet("7:00", "8:00") )# 1
print( minScrollToSet("8:00", "8:00") )# 0
print( minScrollToSet("6:59", "7:01") )# 3
print( minScrollToSet("22:00", "2:00") )# 4
print( minScrollToSet("12:00", "00:00") )# 12
print( minScrollToSet("23:59", "00:00") )# 2

