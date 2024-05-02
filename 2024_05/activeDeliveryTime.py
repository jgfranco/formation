
"""
You are given a series of inputs representing delivery events. Each event is represented by an array of length 3:

[1, 1591846068, 0]

- The first number is an order number
- The second number is the timestamp
- The third number is either

                 0 (representing a pickup) 
                 
                  or 
                 
                 1 (representing a dropoff)

Given a series of events, return the total active time, calculated by the period of time where they have 

      an active delivery (if they've dropped everything off, 
      
      they are not considered active until they pick something up again).

**Follow-up**
Now, let's say the input is not guaranteed to be valid. What are some ways that the input could be invalid?

- Timestamps are not increasing ****
- A pickup is dropped off an incorrect number of times (0 or 2+ times)
- A dropoff occurs before a pickup, or the pickup does not exist

For any pickups and dropoffs that are invalid, ignore them entirely. Add one restriction at a time and have their code test for that condition.
 

EXAMPLE(S)
Input: 
[2, 1591846050, 0] 
[1, 1591846055, 1] bad
[1, 1591846068, 0]
[2, 1591846070, 0] bad
[1, 1591846071, 1]
[2, 1591846080, 1] 
[3, 1591846090, 0] 
[3, 1591846102, 1]
[3, 1591846107, 1] bad

Ignore conditions:
- Dropoff before pickup
- Duplicate pickups
- Duplicate drop offs

Option 1:
order input, track pickup and dropoff in set

Option 2:
use a dictionary, track pickup and dropoff for each order
to validate times

Output: 24
 
FUNCTION SIGNATURE
function activeDeliveryTime(events) {
def activeDeliveryTime(events: [int]) -> int:
"""

"""
- pick up order 1 - start timer
- pick up order 2 - 2 active orders
- drop off order 1 - 1 active order
- drop off order 2 - 0 active orders and i calculate time spents to far and add to active_time var
- pick up order 3 - start timer
- drop off order 3 - calculate diff and add to active_time
"""

"""
Approach
start_time = None
active_order_count = 
total_active_time = 
- looping through ordered array of orders

FOR EACH ORDER PROCESSED

** ORDER PICKUP LOGIC
- check order status... if pickup, and no active orders, then initialize start_time 
- increment active_order_count

** ORDER DROPOFF LOGIC
- check order status and if dropoff, and only one active order, calculate time diff
- add diff to active time
- decrement active order count
- 
"""

def activeDeliveryTime(events):

  startTime = None
  activeOrderCount = 0
  TotalActiveTime = 0

  for event in events:
    orderNumber, timestamp, eventType = event
    if eventType == 0:
      if activeOrderCount == 0:
        startTime = timestamp
      activeOrderCount +=1
    elif eventType == 1:
      if activeOrderCount ==1:
        TotalActiveTime += timestamp -  startTime 
      activeOrderCount -=1

  return TotalActiveTime

events = [
  [1, 1591846068, 0],
  [2, 1591846070, 0], 
  [1, 1591846071, 1],
  [2, 1591846080, 1],
  [3, 1591846090, 0],
  [3, 1591846102, 1]
]
print(activeDeliveryTime(events))




"""
- Dropoff before pickup
- Duplicate pickups
- Duplicate drop offs

"""

def activeDeliveryTime2(events): 
  
  tracker = set()
  startTime = None
  TotalActiveTime = 0

  for event in events:
    orderNumber, timestamp, eventType = event
    if eventType == 0 and orderNumber not in tracker: #pickup
      if len(tracker) == 0:
        startTime = timestamp
      tracker.add(orderNumber)
    
    elif eventType == 1 and orderNumber in tracker:
      if len(tracker) == 1:
        TotalActiveTime += timestamp -  startTime 
      tracker.remove(orderNumber)
    
  return TotalActiveTime


events2 = [
  [2, 1591846050, 0],
  [1, 1591846055, 1],
  [1, 1591846068, 0],
  [2, 1591846070, 0],
  [1, 1591846071, 1],
  [2, 1591846080, 1],
  [3, 1591846090, 0], 
  [3, 1591846102, 1]
]

print(activeDeliveryTime2(events2))