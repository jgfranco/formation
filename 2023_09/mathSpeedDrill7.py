"""
Q. Given an integer, determine if it is a power of two. Do not use built-in functions or operators to solve this problem.

Examples:

Given: 27 // returns false
Given: 256 // returns true
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer num

[output] boolean
"""
def solution(num):
    if num ==1: return True
    while num >= 2:
        if num ==2: return True
        if num %2 != 0: return False
        num /=2
    return False


"""
Q. Given a positive decimal integer, convert it to a binary form.

Examples:

Given: 13, returns 1101
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

[output] integer

"""
def solution(n):
    
    result = 0
    unit = 1
    while n >0:
        result += (n%2) * unit 
        n//=2
        unit = unit* 10
    
    return result


"""
Q. Return true if and only if num is a prime number.

A prime number is a positive integer greater than 1 that is only evenly divisible by 1 and itself:
Prime numbers: 2, 3, 5, 7, 11, ...
Not prime numbers: 1, 4, 6, 8, 9, 10, ...
Approach:

Iterate through all the numbers starting from 2 to (num/2) using a for loop.
For every number check if there exists any number that divides num.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer num

[output] boolean

true if and only if num is prime
"""

def solution(num):
    if num < 0: return False
    if num == 1: return False
    
    for i in range(2, num//2):
        if num%i ==0: return False
        
    return True



"""
A happy number is a number defined by the following process: Start with any positive integer and replace the number with the sum of the squares of its digits. Repeat this process until the number equals 1, at which point it will stay 1, or it loops endlessly in a cycle that does not include 1. A number for which this process ends in 1 is happy.

Write an algorithm to determine whether or not a number is happy.

Example

For n = 19, the output should be solution(n) = true.

Following the process outlined above:

12 + 92 = 82;
82 + 22 = 68;
62 + 82 = 100;
12 + 02 + 02 = 1.
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
1 ≤ n ≤ 231 - 1.

[output] boolean

Return true if the number is happy, otherwise return false.
"""


def solution(n):

    times = 30
    while times >0:
        sum = 0
        while n >0:
            
            digit = n %10
            sum += digit* digit
            n = n //10
        if sum == 1: return True
        
        n = sum
        times -=1
        
    return False

"""
    Q. Given a positive integer, return it with its digits reversed. Do not use strings to solve this problem.

Examples:

Given: 123 // returns 321
Given: 1 // returns 1
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer num

[output] integer
"""
import math
def solution(num):
    
    length = 0
    if num == 0: 
        length = 1
    else: 
        length = int(math.log10(num) +1)
    
    unit = 10 ** (length-1)
 
    reversed = 0
    
    while num >0:
        digit = num %10
        print(reversed, unit, digit)
        reversed += unit * digit
        unit //=10
        num //=10
    
    return reversed
"""
Q. Given a positive decimal integer, convert it to a hexadecimal form as a string.

Examples:

Given: 13, returns "D"
Given: 132, returns "84"
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

[output] string
"""
def solution(n):

    if n < 10: return str(n)
    
    hexNumbers = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F", }
    if n < 16:
        return hexNumbers[n]

    return solution(n//16)+ solution(n%16)