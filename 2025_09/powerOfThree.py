
# Python
def isPowerOfThree(n: int) -> bool:
    if n < 1: return False

    if n == 1: return True
    
    while n % 3 == 0:
        n = n//3
    
    return n == 1


# Basic positives
assert isPowerOfThree(1) is True
assert isPowerOfThree(3) is True
assert isPowerOfThree(9) is True
assert isPowerOfThree(27) is True

# Non-powers
assert isPowerOfThree(0) is False
assert isPowerOfThree(2) is False
assert isPowerOfThree(45) is False

# Large values
assert isPowerOfThree(1162261467) is True
assert isPowerOfThree(1162261466) is False

print('All Python tests passed!')
