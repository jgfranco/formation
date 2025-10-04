
def printNameFreq(names: str) -> str:
    if names == "": return "nobody appeared."

    from collections import Counter

    names = names.split(", ")
    counter = Counter(names)

    printString = []
    for name, count in counter.items():
        printString.append(f"{name} appeared {count} time{'s' if count > 1 else ''}.")

    return "\n".join(printString)



print(printNameFreq("") == "nobody appeared.")

print(printNameFreq("Tony") == "Tony appeared 1 time.")

print(printNameFreq("Tony, Jessica") == 
"Tony appeared 1 time.\n\
Jessica appeared 1 time.")

print(printNameFreq("Tony, Tony, Tony") == "Tony appeared 3 times.")

print(printNameFreq("Tony, Jessica, Paavo, Zoe") == 
"Tony appeared 1 time.\n\
Jessica appeared 1 time.\n\
Paavo appeared 1 time.\n\
Zoe appeared 1 time.")

print(printNameFreq("Tony, Jessica, Paavo, Jessica, Tony, Zoe") == 
"Tony appeared 2 times.\n\
Jessica appeared 2 times.\n\
Paavo appeared 1 time.\n\
Zoe appeared 1 time.")
