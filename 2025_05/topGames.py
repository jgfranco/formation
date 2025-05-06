'''
You are tasked with building a screen that shows the top games being played on a classic board game app. To prevent the games from jumping around on the screen, you must write a function with the following constraints:

Given two arrays, 'oldIDs' and 'newIDs', return an array that meets the following criteria:
- result contains all values from newIDs
- all new ids that currently exist in oldIDs are in the same index as they were in oldIDs
 

EXAMPLE(S)
Example 1: 4 is a new value
oldIDs: [1, 2, 3]
newIDs: [2, 3, 4]
result: [4, 2, 3]

Example 2: the same! as oldIds == newIds
oldIDs: [1, 2, 3, 4]
newIDs: [4, 3, 2, 1]
result: [1, 2, 3, 4]

Example 3: first two values do not appear in newIds / can replace
oldIDs: [1, 2, 3]
newIDs: [3, 4, 5]
result: [4, 5, 3] or [5, 4, 3]
 

FUNCTION SIGNATURE
function preserveIndices(oldIDs: [string], newIDs: [string]) => result: [string]

Explore:
- duplicate values within same array?
No duplicates.
- What are the expected sizes of the input arrays?
SAME LENGTH.
- Input arrays can be in any order.
- Order does not matter for result

Approaches:

1)  Create Map of oldIds where <Id, Index>
Iterate over newIds, checking if the id exists in the oldIdMap.
For Ids in newIds that don't exist in the Map
    Add to result.
Example
oldIds [1,2,3] newIDs: [2, 3, 4]

oldIdMap 
    0: 1
    1: 2
    2: 3
res = []
[2,3,4]
 ^ 
range 0

2) 

OnlyNewIdSet

oldIds
newIds
onlyNewIdSet = newIds.filter(newId -> !oldIds.contains(newId))

iterate over the old array
    check if oldVal is present in newIds
        add it to result
    else
        pop from onlynewIdSet and add to result

N = values in oldIds
TC: O(2N) => O(N)
SC: O(N) => N for the oldIdSet/newIdSet

3) Is there an in-place solution?



'''



def topGames(oldIds, newIds):

    """
    oldIDs: [1, 2, 3]
    newIDs: [3, 4, 5]

    set = {4,5}
    """
    oldIdSet = set(oldIds)
    newIdSet = set(newIds)
    onlyNewIdSet = set(newIds)
    result = []

    for id in oldIdSet:
        if id in onlyNewIdSet:
            onlyNewIdSet.remove(id)
    
    for id in oldIdSet: 
        if id not in newIdSet: 
            result.append(onlyNewIdSet.pop())
        else:
            result.append(id)
    
    return result


print(topGames([1,2,3], [2,3,4]))
print(topGames([1, 2, 3, 4], [4, 3, 2, 1]))
print(topGames([1, 2, 3],[3, 4, 5]))