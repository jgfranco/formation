def countX(word: str) -> int:
    if len(word) == 0:
        return 0
    
    if word[0] == 'x':
        return 1 + countX(word[1:])
    
    return countX(word[1:])

print(countX("xxhixx") == 4)
print(countX("xhixhix") == 3)
print(countX("hiX") == 0)
print(countX("XXXhXXX") == 0)
print(countX("x") == 1)
print(countX("") == 0)
print(countX("hihi") == 0)
print(countX("hiAAhi12hi") == 0)