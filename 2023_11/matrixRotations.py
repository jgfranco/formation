"""
Exploration of how to rotate and flip matrices

Q. Given two square matrices m and target, determine if m can become target by rotating it in either direction (clockwise or counter-clockwise).

Examples:
Given:
m:

[
    [1, 1],
    [0, 1]
]
target:

[
    [1, 1],
    [1, 0]
]
returns true

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.array.integer m

[input] array.array.integer target

[output] boolean
"""
def solution(m, target):
    if m == target: return True
    
    cw = True
    ccw = True
    full = True
    for i in range(len(m)):
        for j in range(len(m[0])):

            if m[i][j] != target[j][-i-1]: cw = False

            if m[i][j] != target[-j-1][i]: ccw =  False
            
            if m[i][j] != target[-i-1][-j-1]: full =  False
             
    print(cw, ccw, full)
    return cw or ccw or full

#print(solution([[1,2,3], [4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]])) # clock-wise
#print(solution([[1,2,3], [4,5,6],[7,8,9]], [[3,6,9],[2,5,8],[1,4,7]])) # counter
print(solution([[1,2,3], [4,5,6],[7,8,9]], [[9,8,7],[6,5,4],[3,2,1]])) # two turns