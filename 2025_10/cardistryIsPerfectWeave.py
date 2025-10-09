"""
Problem Prompt
You're practicing the Faro shuffle in cardistry (https://www.youtube.com/watch?v=A-tSm8g-_pw&t=30s). You start with red cards in one hand and black cards in the other and try to interweave them perfectly, meaning the colors alternate every card once you merge them into a single deck.
You build a machine that accepts a deck of cards to automatically determine if a deck is a perfect interweave. Currently, it can interpret the card's color; you need to write the algorithm.

Example(s)
isPerfectWeave(["B", "B", "R", "B", "R"]) is false
isPerfectWeave(["R", "B", "R", "B", "B"]) is false
isPerfectWeave(["R", "B", "R", "B", "R", "B", "R", "B", "R", "B", "R", "B"]) is true

Signature/Prototype
function isPerfectWeave(deck) {
def isPerfectWeave(deck: list[str]) -> bool:
"""


def isPerfectWeave(deck: list[str]) -> bool:

    for i in range(1, len(deck)):
        if deck[i] == deck[i-1]: return False

    return True

print(isPerfectWeave(["R", "R", "R", "R", "R"]) == False)
print(isPerfectWeave(["R", "B", "R", "R", "R"]) == False)
print(isPerfectWeave(["B", "B", "R", "B", "R"]) == False)
print(isPerfectWeave(["R", "B", "R", "B", "B"]) == False)
print(isPerfectWeave(["B", "R", "B", "R", "B", "R", "B", "R", "B", "R"]))
print(isPerfectWeave(["R", "B", "R", "B", "R", "B", "R", "B", "R", "B", "R", "B"]))
