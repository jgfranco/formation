'''
You are tasked with building a screen that shows the top games being played on a classic board game app. To prevent the games from jumping around on the screen, you must write a function with the following constraints:

Given two arrays, 'oldIDs' and 'newIDs', return an array that meets the following criteria:
- result contains all values from newIDs
- all new ids that currently exist in oldIDs are in the same index as they were in oldIDs
 

EXAMPLE(S)
oldIDs: [1, 2, 3]
newIDs: [2, 3, 4]
result: [4, 2, 3]

oldIDs: [1, 2, 3, 4]
newIDs: [4, 3, 2, 1]
result: [1, 2, 3, 4]

oldIDs: [1, 2, 3]
newIDs: [3, 4, 5]
result: [4, 5, 3] or [5, 4, 3]
 
Brainstorm: 
- oldIDset
- newIDset 
- onlyNewIDSet = filtered set of things unique to newIDset 

- for loop through old ID's: 
  - if old ID at index is in new ID: 
    - if so, just place that value into results array at same index 
  - else: 
    - place value from filtered set (.pop(), increment index)
    
- return result 

oldIDs: [1, 2, 3]   fs {4,5}
newIDs: [3, 4, 5]
         

O(2n)
 |
O(n^2)


FUNCTION SIGNATURE
function preserveIndices(oldIDs: [string], newIDs: [string]) => result: [string]
'''
def preserveIndices(oldIds, newIds):
    oldIdsSet = set(oldIds)
    newIdsSet = set(newIds)
    onlyNewIDSet = set()
    result = []
    
    for game in newIds:
        if game not in oldIdsSet:
            onlyNewIDSet.add(game)

    for game in oldIds:
        if game in newIdsSet:
            result.append(game)
        else:
            result.append(onlyNewIDSet.pop())
    
    return result


print(preserveIndices([1,2,3], [2,3,4]) == [4,2,3])
print(preserveIndices([1,2,3,4], [4,3,2,1]) == [1,2,3,4])
print(preserveIndices([1,2,3], [3,4,5]) == [4,5,3])
    