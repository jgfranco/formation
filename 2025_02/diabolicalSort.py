
'''
come up with the worst way to sort an array'''

from random import randint
def isSorted(nums):
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

def evilSort(nums):
    
    n = len(nums)
    sorted = False
    counter = 0
    while not sorted:
        for i in range(n-1):
            j = randint(i, n-1)
            nums[i], nums[j] = nums[j], nums[i]

        sorted = isSorted(nums)
        counter +=1
    return nums, counter
  
print(evilSort([3,2,10,2,4,6,8,9]))

            
"""
def generate_permutations(arr, l, r, results):
    if l == r:
        results.append(arr[:])  # Store a copy of the current permutation
        return
    
    for i in range(l, r + 1):
        arr[l], arr[i] = arr[i], arr[l]  # Swap
        generate_permutations(arr, l + 1, r, results)  # Recur
        arr[l], arr[i] = arr[i], arr[l]  # Swap back (backtrack)

"""