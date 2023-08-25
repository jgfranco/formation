'''
Reverse Stack In-Place

Given a stack, recursively reverse it using only standard-library operations for that data type. Your solution should be achieved in-place/using the input data structure.

For stacks, these are: push(), pop(), peek(), size().

EXAMPLE(S)
The stack [1, 9, 3, 4] should return [4, 3, 9, 1]
The stack [1] should return [1]

FUNCTION SIGNATURE
def reverseStackInPlace(stack)
'''


def placeBackIntoStack(stack, elem):
    if not stack:
        stack.append(elem)
        return

    top = stack.pop()
    placeBackIntoStack(stack, elem)
    stack.append(top)

def reverseStackInPlace(stack):
    if not stack:
        return

    elem= stack.pop() # 4,3,9,1
    reverseStackInPlace(stack)# [1,9,3], [1,9], [1], []

    placeBackIntoStack(stack, elem)

s0 = [] # empty
s1 = [1] # single
s2 = [1,2,3,4,5] # linear
s3 = [1, 9, 2, 4] # random

reverseStackInPlace(s0)
reverseStackInPlace(s1)
reverseStackInPlace(s2)
reverseStackInPlace(s3)

print(s0, 'expect []')
print(s1, 'expect [1]') 
print(s2, 'expect [5, 4, 3, 2, 1]')  
print(s3, 'expect [4, 2, 9, 1]')