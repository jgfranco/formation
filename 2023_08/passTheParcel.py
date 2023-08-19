'''
❓ PROMPT
In this game, a group of players stands in a circle and passes a parcel around.
When the game starts, a player is chosen to hold the parcel.
The players then pass the parcel to their adjacent player in clockwise order.
At a random point in time, a timer goes off, and the player holding the parcel is removed from the circle.
The passing continues until only one player is left.

Example(s)
We have a list  ["Alice", "Bob", "Charlie", "David", "Eve"]
Assume we have a timer value of 3.
Iteration 1: David removed
Iteration 2: Charlie removed
Iteration 3: Eve removed
Iteration 4: Bob Removed
Winner: Alice.
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
use a pointer
move pointer n times forward
delete element at pointer and reset pointer to 0 to keep within bounds
Algorithm 1:
Time: O()
Space: O()
 
'''
'''
📆 PLAN
Outline of algorithm #: 


run until players holds just one player


  pop element at 0, append it to the end of the array, do this timer times

  pop element at 0


return player at 0
 

🛠️ IMPLEMENT
function passTheParcel(players, timer) {}
def passTheParcel(players, timer):
'''
def passTheParcel(players, timer):
  localPlayers = players.copy()

  while len(localPlayers) > 1:

    for _ in range(timer):
      localPlayers.append(localPlayers.pop(0))
    
    localPlayers.pop(0)

  return localPlayers[0]
'''

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

players = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Test Case 1: Timer less than the number of players
timer1 = len(players) - 1
winner1 = passTheParcel(players, timer1)
print(winner1 == "Bob")

# Test Case 2: Timer equal to the number of players
timer2 = len(players)
winner2 = passTheParcel(players, timer2)
print(winner2 == "David")

# # Test Case 3: Timer greater than the number of players
timer3 = len(players) + 2
winner3 = passTheParcel(players, timer3)
print(winner3 == "Alice")

# # Test Case 4: Timer less than 1
timer4 = 0
winner4 = passTheParcel(players, timer4)
print(winner4 == "Eve")