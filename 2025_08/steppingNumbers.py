def isSteppingNumber(n):
    if n < 10: return True

    prev = float('-inf')

    while n > 0:
        
        digit = n % 10

        if prev == float("-inf"):
            prev = digit
            n //=10
            continue

        #print(prev,digit)
        if abs(prev-digit) != 1:
            return False
        prev = digit
        n//= 10

    return True

# formation's solution 
def is_stepping_number(n):
    while n >= 10:
        a = n % 10
        n = n // 10
        b = n % 10
        if abs(a - b) != 1:
            return False
    return True


assert isSteppingNumber(1) == True, 'Test Case 1 Failed'
assert isSteppingNumber(10) == True, 'Test Case 2 Failed'
assert isSteppingNumber(11) == False, 'Test Case 3 Failed'
assert isSteppingNumber(12) == True, 'Test Case 4 Failed'
assert isSteppingNumber(23) == True, 'Test Case 5 Failed'
assert isSteppingNumber(21) == True, 'Test Case 6 Failed'
assert isSteppingNumber(25) == False, 'Test Case 7 Failed'
assert isSteppingNumber(101) == True, 'Test Case 8 Failed'
assert isSteppingNumber(210) == True, 'Test Case 9 Failed'