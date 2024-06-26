
def findIndex(nums, target):
    exponents = [0]
    i = 1
    while i < len(nums):
        exponents.append(i)
        i +=i
    exponents = exponents[::-1]
    
    anchor = 0

    for i in range(len(exponents)):
        idx = anchor + exponents[i]
        value = nums[idx]
        if value == target:
            return idx
        elif value < target:
          anchor = idx


    
    return -1


print(findIndex([10, 20, 30, 40, 50, 60, 70, 80], 35), "index -1")
print(findIndex([10, 20, 30, 40, 50, 60, 70, 80], 10), "index 0")
print(findIndex([10, 20, 30, 40, 50, 60, 70, 80], 50), "index 4")
print(findIndex([10, 20, 30, 40, 50, 60, 70, 80], 70), "index 6")
print(findIndex([10, 20, 30, 40, 50, 60, 70, 80], 80), "index 7")