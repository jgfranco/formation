

def pairStars(word: str) -> str:

    stack = []
    for char in word:
        if stack and stack[-1] == char:
            stack.append("*")
        stack.append(char)

    return "".join(stack)


print(pairStars("hello") == "hel*lo")
print(pairStars("xxyy") == "x*xy*y")
print(pairStars("aaaa") == "a*a*a*a")