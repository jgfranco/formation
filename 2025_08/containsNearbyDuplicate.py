def containsNearbyDuplicate(nums, k):
    if k == 0: return False
    # dictionary of numbers and their index
    # if we encounter a repeated number we calculate their distance (between indices) and return True if it is less or equal to k
    seen = {}

    for idx, num in enumerate(nums):

        if num in seen and (idx - seen[num]) <= k:
            return True

        seen[num] = idx
    
    return False

print(containsNearbyDuplicate([1, 2, 3, 1], 3) == True)
print(containsNearbyDuplicate([1, 0, 1, 1], 1) == True)
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False)
print(containsNearbyDuplicate([], 0) == False)
print(containsNearbyDuplicate([1], 1) == False)