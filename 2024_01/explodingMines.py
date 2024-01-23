'''
Question : 

Given an array of mines where each mine has an *x* and *y* position and 
blast radius *1*, determine how many mines will explode given an 
initial mine by index that will explode.

When a mine explodes, it triggers all unexploded mines that are as for 
as or closer than its blast radius.

After coming up with a working solution, discuss how this can be 
optimized further. Accurate pseudo code or explanation is acceptable. 
Code is ideal.
 

EXAMPLE(S)
const mines = [
  { x: 1.0, y: 0.0 },
  { x: 1.0, y: 1.0 }, // index 1
  { x: 1.0, y: 2.0 },
  { x: 1.0, y: 3.0 },
  { x: 2.0, y: 2.0 },
  { x: 3.0, y: 0.0 } // index 5
]
(Note: X/Y positions can have decimal values such as 0.5 or 0.25)

4 |
3 |  X
2 |  X  X
1 |  X
0 |__X_____X___
  0  1  2  3

  (1,1) - (1,3)
  (1,1) - (1,2) which then triggers an explosion in (1,3)

Triggering the mine at index 1 will explode 5 mines in total becuase they are within 1 distance radius away:
* x: 1.0, y: 0.0
* x: 1.0, y: 1.0
* x: 1.0, y: 2.0
* x: 1.0, y: 3.0
* x: 2.0, y: 2.0

Trigger the mine at index 5 will explode 1 mine in total because no other mines are within 1 distance radius away.
 * x: 3.0, y: 0.0
 

Edge cases/Assumptions/Observations/Questions : 
- no two mines will have same co-ordinates
- distance formula
sqrt((x_1 - x_2) ^ 2 + (y_1 - y_2) ^ 2) <= 1
- explosions cascade 
- fractional are allowed 

Approach : 

#1 DFS
- go through each mine and keep track of the ones that we already exploded
    - add mine to exploded set
    - for each mine,
        if the mine hasn't been exploded and the distance is within 1, then recur on the mine


#2 bucketing as an optimization
values      bucketKey
0.25,0.25 -> 0,0 
0.15,0.20 ->
0.05,0.10 ->

bucketing is being used to quicken up the neighbor lookup 



FUNCTION SIGNATURE
function getNumExplosions(mines, mineIndex): number
'''

# mine {
#     x,y;
# }

import math

class Mine:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

def isInRange(explodedMine, otherMine):
    #
    distance = math.sqrt((explodedMine.x - otherMine.x) **2 + (explodedMine.y - otherMine.y) ** 2)
    return distance <= 1

def getBucketKey(x, y):
    return f"({math.floor(x)}, {math.floor(y)})"

    
def addToBucket(mine, bucket):
    bkey = getBucketKey(mine.x, mine.y)
    if bkey not in bucket:
        bucket[bkey] = []
    bucket[bkey].append(mine)
    
    
     
def getNeighbors(mine, mineIndex, buckets):
    neighbours = []
    

    lookups = [
        getBucketKey(mine.x + 1, mine.y),
        getBucketKey(mine.x, mine.y + 1),
        getBucketKey(mine.x - 1, mine.y),
        getBucketKey(mine.x, mine.y - 1),
    ]

    potential_neighbours = []
    for lookup in lookups:
        if lookup in buckets:
            potential_neighbours.extend(buckets[lookup])

    for idx, neighbour_mine in enumerate(potential_neighbours):
        if idx == mineIndex:
            continue
        
        if isInRange(mine, neighbour_mine):
            neighbours.append(idx)
    return neighbours
     
     
def getNumExplosions(mines, mineIndex) -> int:
    buckets = {}
    # we need to add mines to bucket
    
    for mine in mines:
        addToBucket(mine, buckets)
    
    def explodeMine(mine_index, exploded_mines) -> None:
        # if we already exploded the mine, do nothing
        if mine_index in exploded_mines:
            return

        exploded_mines.add(mine_index)

        mine = mines[mine_index]
        neighbors = getNeighbors(mine, mine_index, buckets)

        for neighbor_mine_index in neighbors:
            if neighbor_mine_index not in exploded_mines:
                explodeMine(neighbor_mine_index, exploded_mines)


    exploded_mines = set()
    explodeMine(mineIndex, exploded_mines)
    
    return len(exploded_mines)
