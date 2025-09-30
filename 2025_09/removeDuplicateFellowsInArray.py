"""
Problem Prompt
A bug in the Formation session tool accidentally duplicated some Fellows in sessions. Given an array of names representing Fellows in a session, return an array of the distinct Fellows. The array must be in the same order as the input.
Follow-up question:
How would removing the Fellows in place, instead of using a new output array, affect the algorithm's runtime?

Example:
["oliver", "pixel", "oliver", "pinky"] => ["oliver", "pixel", "pinky"]
"""

def removeDuplicateFellows(fellows: list[str]) -> list[str]:

    simplifiedList = set()

    for fellow in fellows:

        if fellow not in simplifiedList:
            simplifiedList.add(fellow)
        
    return list(simplifiedList)



print(set(removeDuplicateFellows(["oliver", "pixel", "oliver", "pinky"]))
== set(["oliver", "pixel", "pinky"]))
print(removeDuplicateFellows([]) == [])
print(set(removeDuplicateFellows(["Oliver", "oliver"]))
== set(["Oliver", "oliver"]))
print(removeDuplicateFellows(["pinky"]) == ["pinky"])
print(removeDuplicateFellows(["pinky", "pinky", "pinky"]) == ["pinky"])
print(set(removeDuplicateFellows(["pinky", "paavo"])) == set(["pinky", "paavo"]))
