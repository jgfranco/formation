def biggestMistake(deck: list[str]) -> int:

    biggestMistake = 0
    prev = ""
    count = 1
    for char in deck:
        if char == prev:
            count += 1
            biggestMistake = max(biggestMistake, count)
        else:
            count = 1
        prev = char

    return biggestMistake

print(biggestMistake(["B", "B", "R", "B", "R"])) # 2
print(biggestMistake(["R", "B", "R", "B", "B"])) # 2
print(biggestMistake(["R", "B", "R", "B", "R", "B", "R", "B", "R", "B", "R"]))# 0

print(biggestMistake(["R"]) == 0)
print(biggestMistake(["B"]) == 0)
print(biggestMistake(["R", "B"]) == 0)
print(biggestMistake(["B", "R"]) == 0)
print(biggestMistake(["R", "R"]) == 2)
print(biggestMistake(["B", "B"]) == 2)
print(biggestMistake(["R", "R", "R", "R", "R"]) == 5)
print(biggestMistake(["R", "B", "R", "R", "R"]) == 3)
print(biggestMistake(["B", "B", "R", "B", "R"]) == 2)
print(biggestMistake(["R", "B", "R", "B", "B"]) == 2)
print(biggestMistake(["B", "B", "R", "R", "B", "B", "R", "R", "B", "R"]) == 2)
print(biggestMistake(["R", "B", "R", "B", "B", "B", "R", "R", "B", "B", "R"]) == 3)
print(biggestMistake(["B", "R", "B", "R", "B", "R", "B", "R", "B", "R"]) == 0)
print(biggestMistake(["R", "B", "R", "B", "R", "B", "R", "B", "R", "B", "R"]) == 0)